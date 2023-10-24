Program Specific How-Tos
========================

Here we will share some guides on getting started with some specific applications. In many cases there are multiple ways to accomplish things so you can treat this as a starting point. If you found a good guide elsewhere which you successfully followed or if you would like your own guide added please feel free to `let us know <itsupport@york.ac.uk>`_.


Jupyter Notebooks
-----------------

The `Jupyter notebook <https://docs.jupyter.org/en/latest/>`_ is a web-based notebook environment for interactive computing. Running a ``Jupyter notebook`` server remotely on Viking and connecting to it from your local web browser is certainly possible.
There are a few steps to ensure that your notebook is running on a compute node (not a login node) and you can remotely connect to it.

.. admonition:: The connection would look something like this:

    Your computer ➡️ Viking login node ➡️ Viking compute node ➡️ Jupyter notebook


One way to do this is with the interactive desktop sessions on Viking, following these steps:

    1. :doc:`Log into Viking <../getting_started/connecting_to_viking>`
    2. Start a :doc:`desktop session & connect via VNC <../using_viking/virtual_desktops>`
    3. Start an :ref:`interactive session <virtual_session_compute_node>` to get a compute node to run the notebook on
    4. Load the Jupyter module and start the notebook, **on the compute node**
    5. In a **new** terminal, forward a connection from the virtual desktop (login node) to the compute node
    6. Load a browser and connect to the notebook

Steps 1-3 is explained on the linked pages. Once you have an interactive session running the terminal should tell you *which* ``node`` it is running on. I'll paste in the output from my test below and highlight the the lines where you can see the ``node`` for clarity:

.. code-block:: console
    :emphasize-lines: 5,6

    [abc123@login2 [viking] ~]$ start-interactive-session.sh -N 1 -n 1 -c 10 -t 1:0:0
    srun: job 23721784 queued and waiting for resources
    srun: job 23721784 has been allocated resources
    Enabling login2 to accept our X-connection... node065 being added to access control list
    [abc123@node065 [viking] ~]$ module load tools/JupyterLab/3.1.6-GCCcore-11.2.0
    [abc123@node065 [viking] ~]$ jupyter notebook --no-browser

As you can see, I also loaded the ``Jupyter`` module and started the notebook. From here you can leave this terminal alone, and then open another new terminal and paste the following command:

.. code-block:: console

    $ ssh -N -L localhost:8888:localhost:8888 abc123@node065

This forwards the connection from the login node, where you are running the virtual desktop, to the compute node. You'll need to amend ``abc123`` to your username and ``node065`` to your own details which were displayed earlier.

Then, back to the first terminal where the notebook is running, there should be a link to click on to connect to the notebook eg:

.. code-block:: console
    :emphasize-lines: 3,4

    [I 09:26:03.233 NotebookApp] Serving notebooks from local directory: /users/nd996
    [I 09:26:03.233 NotebookApp] Jupyter Notebook 6.4.0 is running at:
    [I 09:26:03.233 NotebookApp] http://localhost:8888/?token=88fdcf3989e91e4fc684aedb5c238cf8ce70d06f16fa5415
    [I 09:26:03.233 NotebookApp]  or http://127.0.0.1:8888/?token=88fdcf3989e91e4fc684aedb5c238cf8ce70d06f16fa5415
    [I 09:26:03.233 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 09:26:03.240 NotebookApp]

``Ctrl + left mouse click`` on this link and the browser should load and connect to the notebook running on the compute node!


Jupyter Notebooks using VSCode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using some of the above guide as reference, another way to so this is with VSCode and it's similar, but you don't need to make a virtual desktop. If you're interested in this method it's similar to the above in many ways:

    1. Install the `Jupyter extension <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`_ in VSCode
    2. Remote ssh connect to Viking from VSCode's `terminal <https://code.visualstudio.com/docs/terminal/basics>`_
    3. Start an interactive session with ``srun`` eg ``srun -N 1 -n 1 -c 10 -t 4:0:0 --pty /bin/bash`` **in the terminal of VSCode**
    4. Once the interactive session is running, load the ``Jupyter`` module and run the notebook, like above
    5. In a **new** remote terminal on Viking, in VSCode, set up the ssh forwarding, like above (noting the ``node`` number from step 4.)
    6. In VSCode, open a new ``Jupyter`` notebook: ``(Ctrl+Shift+P)`` and type ``Jupyter: Create New Jupyter Notebook.``
    7. In VSCode, press ``select kernel`` in the top right then select ``Existing Jupyter server``
    8. Paste in the URL of the notebook, just like above, follow the prompts in VSCode to name the notebook and select the available kernel


VSCode
------

``VSCode`` is a modern text editor from Microsoft. It's possible to use many extensions with it to extend its capabilities but here we'll explain how to use it to connect to Viking over ``ssh`` and allow you to remotely edit text files, which can be very handy.


    1. Install `VSCode <https://code.visualstudio.com/>`_ for your operating system
    2. Follow the instructions to install the `Remote - SSH <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh>`_ extension in VSCode
    3. Follow the instructions to `getting started <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh#getting-started>`_ to connect to viking, the address is ``viking.york.ac.uk``
    4. Enter your password when prompted and you should soon be connected and be able to edit and save files through VSCode.

.. tip::

    ``Ctrl + ``` (backtick) Opens a terminal in ``VSCode``


.. tip::

    If you at some point VSCode refuses to connect and it's not obvious why, sometimes the files it installs on Viking have become corrupted. You can log into Viking in your ususal way without VSCode, and delete the following directory ``~/.vscode-server``. The next time VSCode connects to Viking it will reiinstall the files and hopefully will fix the problem.


