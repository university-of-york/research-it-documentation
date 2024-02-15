Jupyter notebooks
=================

The `Jupyter notebook <https://docs.jupyter.org/en/latest/>`_ is a web-based notebook environment for interactive computing. Running a ``Jupyter notebook`` server remotely on Viking and connecting to it from your local web browser is certainly possible.
There are a few steps to ensure that your notebook is running on a compute node (not a login node) and you can remotely connect to it.

.. admonition:: The connection would look something like this:

    Your computer ➡️ Viking login node ➡️ Viking compute node ➡️ Jupyter notebook

One way to do this would be to start an interactive session on a compute node, from that session run the ``Jupyter`` notebook server:

.. code-block:: console
    :caption: you can adjust the 'cpus-per-task' and 'time' to suit your needs

    $ srun --nodes=1 --ntasks=1 --cpus-per-task=5 --time=08:00:00 --pty /bin/bash
    srun: job 76415 queued and waiting for resources
    srun: job 76415 has been allocated resources
    Creating user dir for 'Local Scratch'
    flight start: Flight Direct environment is already active.
    [abc123@node112[viking2] ~]$

Here we have an interactive ``bash`` session on the ``node112`` compute node, with five CPU cores, for eight hours. Next we load the ``Jupyter`` module and run the server:

.. code-block:: console
    :emphasize-lines: 16,17

    [abc123@node112[viking2] ~]$ module load {MOD_JUPYTER}
    [abc123@node112[viking2] ~]$ jupyter notebook --no-browser
    [I 15:01:51.756 NotebookApp] Writing notebook server cookie secret to /users/abc123/.local/share/jupyter/runtime/notebook_cookie_secret
    [I 2023-11-03 15:01:52.190 LabApp] JupyterLab extension loaded from /opt/apps/eb/software/JupyterLab/3.1.6-GCCcore-11.2.0/lib/python3.9/site-packages/jupyterlab
    [I 2023-11-03 15:01:52.190 LabApp] JupyterLab application directory is /opt/apps/eb/software/JupyterLab/3.1.6-GCCcore-11.2.0/share/jupyter/lab
    [I 15:01:52.194 NotebookApp] Serving notebooks from local directory: /users/abc123
    [I 15:01:52.194 NotebookApp] Jupyter Notebook 6.4.0 is running at:
    [I 15:01:52.194 NotebookApp] http://localhost:8888/?token=9b0f6d6918f238c0e8543257a842b65cd4671ee1b55a4e3c
    [I 15:01:52.194 NotebookApp]  or http://127.0.0.1:8888/?token=9b0f6d6918f238c0e8543257a842b65cd4671ee1b55a4e3c
    [I 15:01:52.194 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 15:01:52.198 NotebookApp]

        To access the notebook, open this file in a browser:
            file:///users/abc123/.local/share/jupyter/runtime/nbserver-2295028-open.html
        Or copy and paste one of these URLs:
            http://localhost:8888/?token=9b0f6d6918f238c0e8543257a842b65cd4671ee1b55a4e3c
         or http://127.0.0.1:8888/?token=9b0f6d6918f238c0e8543257a842b65cd4671ee1b55a4e3c

The server is running and listening on port ``8888``. We cannot access that port directly from our local computer so we set up the an ``ssh tunnnel`` to the login node then then from there to the compute node, where the ``Jupyter`` notebook server is actually running. You can do this with one command locally on your computer:

.. code-block:: console
    :caption: remember to change 'node112' to the node you are running Jupyter from

    $ ssh -L 8888:localhost:8889 viking.york.ac.uk ssh -N -L 8889:localhost:8888 node112

The above command opens up one ``ssh tunnel``, forwarding your local port ``8888`` to the Viking login node port ``8889``. Then it opens up another ``ssh tunnel`` from the login node's port ``8889`` to the compute node112's port ``8888`` - where the ``Jupyter`` server is listening.

Finally ``Ctrl + left mouse click``  on the link from the first terminal session on ``node112``, highlighted above. Either the ``http://localhost:8888/?token=...`` or the ``http://127.0.0.1:8888/?token=...`` links. Your browser should open and connected to the ``Jupyter`` server running on Viking.

.. tip::

    If you're using a personal computer, you'll need to tell Viking your username in the above command for example:

    .. code-block:: console

        ssh -L 8888:localhost:8889 abc123@viking.york.ac.uk ssh -N -L 8889:localhost:8888 node112

.. FIXME: below method not working.

..
.. Another way to do this is with the interactive desktop sessions on Viking, following these steps:
..
..     1. :doc:`Log into Viking <../getting_started/connecting_to_viking>`
..     2. Start a :doc:`desktop session & connect via VNC <../using_viking/virtual_desktops>`
..     3. Start an :ref:`interactive session <virtual_session_compute_node>` to get a compute node to run the notebook on
..     4. Load the Jupyter module and start the notebook, **on the compute node**
..     5. In a **new** terminal, forward a connection from the virtual desktop (login node) to the compute node
..     6. Load a browser and connect to the notebook
..
.. Steps 1-3 is explained on the linked pages. Once you have an interactive session running the terminal should tell you *which* ``node`` it is running on. I'll paste in the output from my test below and highlight the the lines where you can see the ``node`` for clarity:
..
.. .. code-block:: console
..     :emphasize-lines: 5,6
..
..     [abc123@login2 [viking] ~]$ start-interactive-session.sh -N 1 -n 1 -c 10 -t 1:0:0
..     srun: job 23721784 queued and waiting for resources
..     srun: job 23721784 has been allocated resources
..     Enabling login2 to accept our X-connection... node065 being added to access control list
..     [abc123@node065 [viking] ~]$ module load {MOD_JUPYTER}
..     [abc123@node065 [viking] ~]$ jupyter notebook --no-browser
..
.. As you can see, I also loaded the ``Jupyter`` module and started the notebook. From here you can leave this terminal alone, and then open another new terminal and paste the following command:
..
.. .. code-block:: console
..
..     $ ssh -N -L localhost:8888:localhost:8888 abc123@node065
..
.. This forwards the connection from the login node, where you are running the virtual desktop, to the compute node. You'll need to amend ``abc123`` to your username and ``node065`` to your own details which were displayed earlier.
..
.. Then, back to the first terminal where the notebook is running, there should be a link to click on to connect to the notebook eg:
..
.. .. code-block:: console
..     :emphasize-lines: 3,4
..
..     [I 09:26:03.233 NotebookApp] Serving notebooks from local directory: /users/nd996
..     [I 09:26:03.233 NotebookApp] Jupyter Notebook 6.4.0 is running at:
..     [I 09:26:03.233 NotebookApp] http://localhost:8888/?token=88fdcf3989e91e4fc684aedb5c238cf8ce70d06f16fa5415
..     [I 09:26:03.233 NotebookApp]  or http://127.0.0.1:8888/?token=88fdcf3989e91e4fc684aedb5c238cf8ce70d06f16fa5415
..     [I 09:26:03.233 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
..     [C 09:26:03.240 NotebookApp]
..
.. ``Ctrl + left mouse click`` on this link and the browser should load and connect to the notebook running on the compute node!
..

Jupyter notebooks using VSCode
------------------------------

Using some of the above guide as reference, another way to so this is with VSCode. You do it all in VSCode and the inbuilt terminals in VSCode. If you're interested in this method it's similar to the above in many ways:

    1. Install the `Jupyter extension <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`_ in VSCode
    2. Remote ssh connect to Viking from VSCode's `terminal <https://code.visualstudio.com/docs/terminal/basics>`_
    3. Start an interactive session with ``srun`` eg ``srun -N 1 -n 1 -c 10 -t 4:0:0 --pty /bin/bash`` **in the terminal of VSCode**
    4. Once the interactive session is running, load the ``Jupyter`` module and run the notebook, like above
    5. In a **new** remote terminal on Viking, in VSCode, set up the ssh forwarding, like above (noting the ``node`` number from step 4.)
    6. In VSCode, open a new ``Jupyter`` notebook: ``(Ctrl+Shift+P)`` and type ``Jupyter: Create New Jupyter Notebook.``
    7. In VSCode, press ``select kernel`` in the top right then select ``Existing Jupyter server``
    8. Paste in the URL of the notebook, just like the guide above, follow the prompts in VSCode to name the notebook and select the available kernel
