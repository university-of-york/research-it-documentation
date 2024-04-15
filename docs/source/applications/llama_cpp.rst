Llama.cpp
=========

The main goal of `llama.cpp <https://github.com/ggerganov/llama.cpp>`_ is to enable LLM inference with minimal setup and state-of-the-art performance on a wide variety of hardware - locally and in the cloud.

One of the extras included in ``llama.cpp`` is a fast, lightweight, pure C/C++ HTTP server to act as a front end. With the help of some extra ``ssh`` tunnels, this can allow you to easily interact with a LLM running on Viking through the web browser on your PC. Below is an example of this workflow.

To begin with you'll need to download an LLM to Viking, for example `mistral-7b-instruct-v0.2.Q4_K_M.gguf <https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF>`_. You can download this on Viking with the ``curl`` command for example:

.. code-block:: console

    $ curl -L https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf?download=true -o mistral-7b-instruct-v0.2.Q4_K_M.gguf


The ``llama.cpp`` module needs to be run an interactive session on the GPU partition, for example:

.. code-block:: console

    $ srun --nodes=1 --cpus-per-task=32 --partition=gpu --gres=gpu:1 --time=00:01:00 --pty /bin/bash

.. attention::

    Make a note of which GPU node you are allocated, for example ``gpu12``. You'll need this later on!

Once the resources have been allocated, load the module:

.. code-block:: console

    $ module load {MOD_LLAMA_CPP}


To run the server, you need to pass it the path to the LLM you downloaded, along with a few options you can customise:

.. code-block:: console

    $ server -m /path/to/mistral-7b-instruct-v0.2.Q4_K_M.gguf --n-gpu-layers 256 --ctx-size 2048

Here I've also set the ``n-gpu-layers`` option which allows offloading some layers to the GPU for computation. Generally results in increased performance, and the ``ctx-size`` is the size of the prompt context (the default is 512). More options are covered in the `README.md <https://github.com/ggerganov/llama.cpp/tree/master/examples/server>`_.

.. note::

    In the above command ``server`` is the name of the server which comes packaged with ``llama.cpp``.

Now you should get some output in the terminal and the model and server should be up and running in a short while.


Set up the ssh tunnels
----------------------

The ``llama.cpp`` server is running on a GPU compute node on Viking, behind the login node. This means you can't immediately load up a web browser and connect to it. But with *two* ``ssh`` tunnels, you can.

1. To forward from your local PC to the login node
2. To forward from the login node to the GPU compute node, where the server is running

On your local PC
^^^^^^^^^^^^^^^^

This will forward port ``8080`` on your local PC to port ``8081`` on ``viking-login1.york.ac.uk``

.. code-block:: console

    $ ssh -N -L 8080:localhost:8081 viking-login1.york.ac.uk

On Viking
^^^^^^^^^

In this case we are going to use Viking's login1 node (Viking has two login nodes in total, login1 and login2). First ``ssh`` into login1:

.. code-block:: console
    :caption: replace 'abc123' with your username

    $ ssh abc123@viking-login1.york.ac.uk

Once logged in run the second ``ssh`` tunnel. You'll need to know which GPU node your server is running on, in this example we use ``gpu12`` but yours will likely be different:

.. code-block:: console

    $ ssh -N -L 8081:localhost:8080 gpu12

This will forward port ``8081`` on ``viking-login1.york.ac.uk`` to port ``8080`` on ``gpu12``.

.. tip::

    To cancel either of these ``ssh`` tunnels, press ``Ctrl + c`` in the terminal where it is running.


Open the page in your browser
-----------------------------

If everything is working, you should now be able to connect to the server from your web browser on your PC:

`localhost:8080 <localhost:8080>`_


.. Note::

    The above two ``ssh`` tunnel commands can be done in one single command however, it will have the effect to leaving one of the ``ssh`` tunnels running on the login node after you have logged out which you should really kill when you're finished. If you're familiar with killing processes on Linux, an example command which you would only run in a terminal on your local PC (not on Viking) would be:

    .. code-block:: console

        $ ssh -L 8080:localhost:8081 viking-login1.york.ac.uk ssh -N -L 8081:localhost:8080 gpu12
