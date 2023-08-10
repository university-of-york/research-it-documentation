Program Specific How-Tos
========================

Here we will share some guides on getting started with some specific applications. In many cases there are multiple ways to accomplish things so this is just a set of certain example use cases. If you found a good guide elsewhere which you followed or if you would like your own guide added please feel free `let us know <itsupport@york.ac.uk>`_ so we can add it.


Jupyter Notebooks
-----------------

The `Jupyter notebook <Jupyter notebook>`_ is a web-based notebook environment for interactive computing. Running a ``Jupyter notebook`` server remotely on Viking and connecting to it from your local web browser is certainly possible. There are a few ways where this could be done, to utilise the compute nodes of Viking there would be a few steps to ensure that your ``Jupyter`` notebook is running on the compute node (not the login node) and you remotely connect to it.

.. admonition:: The connection would look something like this:

    Your laptop ➡️ Viking login node ➡️ Viking compute node ➡️ Jupyter notebook


One way to do this is with the interactive desktop sessions on Viking, following these steps:

    1. :doc:`Log into Viking <../getting_started/connecting-to-viking>`
    2. Start a :doc:`desktop session & connect via VNC <../using_viking/virtual-desktops>`
    3. Start an :ref:`interactive session <virtual-session-compute-node>` to get a compute node to run the notebook
    4. Load the Jupyter module and start the notebook, on the compute node
    5. In a new terminal, forward a connection from the virtual desktop (login node) to the compute node
    6. Load a browser and connect to the notebook

Steps 1-3 is explained on the linked pages. Once you have an interactive session running the terminal should tell you *which* ``node`` it is running on. I'll paste in the output from my test below and highlight the the lines where you can see the ``node`` for clarity:

.. code-block:: console
    :emphasize-lines: 5,6

    [nd996@login2 [viking] ~]$ start-interactive-session.sh -N 1 -n 10 -t 1:0:0
    srun: job 23721784 queued and waiting for resources
    srun: job 23721784 has been allocated resources
    Enabling login2 to accept our X-connection... node065 being added to access control list
    [nd996@node065 [viking] ~]$ ml tools/JupyterLab/3.1.6-GCCcore-11.2.0
    [nd996@node065 [viking] ~]$ jupyter notebook --no-browser

As you can see, I also loaded the ``Jupyter`` module and started the notebook. From here you can leave this terminal alone, and then open another new terminal and paste the following command:

.. code-block:: console

    $ ssh -N -L localhost:8888:localhost:8888 nd996@node065

This forwards the connection from the login node, where you are running the virtual desktop, to the compute node. You'll need to amend the ``username`` and ``node number`` to your own details which where displayed earlier.

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

This is one way of accomplishing this. I also quickly tested doing this in VSCode and it's similar, but you don't need to make a virtual desktop. If you're interested in this method it's similar to the above in many ways:

    1. Install the Jupyter extension on VSCode
    2. Remote ssh connect to Viking from VSCode
    3. Start an interactive session with ``srun`` eg ``srun -N 1 -n 40 -t 8:0:0 --pty /bin/bash`` in the terminal of VSCode
    4. Once the interactive session is running, load the Jupyter module and run the notebook, like above
    5. In a new remote terminal on Viking, in VSCode, set up the ssh forwarding, like above (noting the ``node`` number from step 4.)
    6. In VSCode, open a new Jupyter notebook, press ``select kernel`` in the top right, select ``Exisiting Jupyter server``
    7. Paste in the URL of the note book, just like above, follow the prompts in VSCode to name the notebook and select the available kernel


VSCode
------

``VSCode`` is a modern text editing program from Microsoft, it's possible to use many extensions with it to extend it capabilities but here we'll explain how to use it to connect to Viking over ``ssh`` and allow you to edit text files, which can be very handy.


TODO

1. get VSCode
2. get remoteserver
3. set it up
4. away we go

.. tip::

    ``Ctrl + ``` (backtick) Opens a terminal in ``VSCode``
