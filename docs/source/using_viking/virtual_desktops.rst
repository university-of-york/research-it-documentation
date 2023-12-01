Virtual desktops
================

.. warning::

    This page is being updated and the process of starting and connecting to a virtual desktop on Viking is being worked on. Some of this page may be inaccurate or not work at times.


You can create virtual desktop sessions to run graphical programs. There two main ways you can do this, on the login node and on a compute node.

.. attention::

    Remember, the login nodes are only for **light work** as mentioned in the :doc:`code of conduct <../getting_started/code_of_conduct>`, so if you need to use a GUI program for heavy work, then please ensure that is done on a compute node.


Login node
----------

Run the following line from within a login node

.. code-block:: console

    $ flight desktop start gnome

And you will be presented with information similar to mine below:

.. code-block:: console
    :emphasize-lines: 23

    Starting a 'gnome' desktop session:

    > ✅ Starting session

    A 'gnome' desktop session has been started.

    == Session details ==
          Name:
      Identity: 2c4611f2-bec8-4ae9-a997-185f306e96d8
          Type: gnome
       Host IP: 10.0.13.22
      Hostname: login2
          Port: 5906
       Display: :6
      Password: muAtEks5
      Geometry: 1024x768

    This desktop session is not directly accessible from outside of your
    cluster as it is running on a machine that only provides internal
    cluster access.  In order to access your desktop session you will need
    to perform port forwarding using 'ssh'.

    Refer to 'flight desktop show 2c4611f2' for more details.

    If prompted, you should supply the following password: muAtEks5


More details on the virtual desktop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need more info, from the output copy and run the command from the line highlighted above. In this example it's  ``flight desktop show 2c4611f2`` but for you the ``2c4611f2`` part will be different, please ensure you copy from the output on your session. As as example the output will look similar to this:

.. code-block:: console
    :emphasize-lines: 7,9,17

    == Session details ==
          Name:
      Identity: 2c4611f2-bec8-4ae9-a997-185f306e96d8
          Type: gnome
       Host IP: 10.0.13.22
      Hostname: login2
          Port: 5906
       Display: :6
      Password: muAtEks5
      Geometry: 1024x768

    This desktop session is not directly accessible from outside of your
    cluster as it is running on a machine that only provides internal
    cluster access.  In order to access your desktop session you will need
    to perform port forwarding using 'ssh':

      ssh -L 5906:10.0.13.22:5906 abc123@

    Once the ssh connection has been established, depending on your
    client, you can connect to the session using one of:

      vnc://abc123:muAtEks5@localhost:5906
      localhost:5906
      localhost:6

    If, when connecting, you receive a warning as follows, try again with
    a different port number, e.g. 5907, 5908 etc.:

      channel_setup_fwd_listener_tcpip: cannot listen to port: 5906

    If prompted, you should supply the following password: muAtEks5



.. tip::

    You can change the size of the virtual desktop 'display' once you're logged into the virtual desktop by clicking in the top right symbols, to the right of the time and date to open a small pop up menu. Then click on the spanner button, then the control panel will appear. Click on ``Devices`` then ``Displays`` and you can adjust the setting there but not all settings will be usable. Alternatively, you can set the ``geometry`` with the ``-g`` option when you run the ``flight`` command for example: ``flight desktop start gnome -g 1600x1200``.


Create the ssh tunnel
^^^^^^^^^^^^^^^^^^^^^

The virtual desktop isn't running on the login node, so we need a way to *tunnel* a connection from your computer to the login node, the command highlighted in the output above is incomplete but on Linux and MacOS from a terminal or in a PowerShell on an up to date Windows 10 or 11 system you would need to run the following:

.. code-block:: console
    :caption: substitute ``abc123`` for your actual username

    ssh -L 5906:10.0.13.22:5906 abc123@10.0.13.22

Notice we copied over the same ``10.0.13.22`` IP address and placed it after ``abc123@``, this is a temporary issue we will shortly correct. Please ensure you substitute in your own username in place of ``abc123`` and copy the IP address from your screen output as it may be different to this example. **Leave this terminal open**, it will function as our ``ssh tunnel``.


Connect to the virtual desktop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the appropriate application for your operating system (examples listed below), log into the virtual desktop. Note the ``port`` from the earlier output, in my case this was ``5906``, yours may be similar but will likely be different. It will ask for a password (in my example this is ``muAtEks5``), yours will be whatever was displayed in the previous step.

Windows
"""""""

On Windows you can connect using `TightVNC <https://www.tightvnc.com/download.php>`_. Using the above as an example, the ``Remote Host`` would be:

.. code-block:: console

    localhost:5906

Linux
""""""

`Remmina <https://remmina.org/how-to-install-remmina/>`_ is a good tool, run it and ensure you have ``VNC`` selected to the left of the address bar and use the same address:

.. code-block:: console

     localhost:5906


MacOS
""""""

 MacOS has built in support and you can use ``Finder`` for this, select ``Go`` and then ``Connect to server`` but the address is slightly different you must add ``vnc://`` to the beginning:

.. code-block:: console

    vnc://localhost:5906


.. _virtual_desktop:

Use the virtual desktop
^^^^^^^^^^^^^^^^^^^^^^^

You should soon be presented with a virtual desktop running on Viking. Click the ``Applications > System Tools > Terminal`` button to launch a terminal and you can load modules and programs as usual.

.. figure:: ../assets/img/virtual_desktop1.png
    :align: center
    :alt: a virtual desktop on Viking with the application menu open

    it's a virtual desktop, on a remote machine!


List sessions
^^^^^^^^^^^^^

List all the current virtual desktops you have running with the following command:

.. code-block:: console

    $ flight desktop list

And you'll be presented with a list similar to mine below:

.. code-block:: console

    ┌──────┬──────────┬───────┬───────────┬────────────┬────────────────┬──────────┬────────┐
    │ Name │ Identity │ Type  │ Host name │ IP address │ Display (Port) │ Password │ State  │
    ├──────┼──────────┼───────┼───────────┼────────────┼────────────────┼──────────┼────────┤
    │      │ 2c4611f2 │ gnome │ login2    │ 10.0.13.22 │ :6 (5906)      │ muAtEks5 │ Active │
    └──────┴──────────┴───────┴───────────┴────────────┴────────────────┴──────────┴────────┘


.. _kill_sessions:

Kill sessions
^^^^^^^^^^^^^

To kill a session you need to use the ``Identity`` code from the output above, use it with the following command:

.. code-block:: console

    $ flight desktop kill 2c4611f2

Your ``Identity`` code will be different to mine, this is just an example.


.. attention::

    It's important to ``kill`` any unused virtual desktops not just log out / close down the connection. They will still be running in the background using resources (remember the :doc:`code of conduct <../getting_started/code_of_conduct>`) so it's really important that you ``kill`` them after you are finished. If you leave too many running you will not be able to start a fresh one and will negatively impact other users.

.. _virtual_session_compute_node:

Compute node
-------------

The above method is great for light work like checking results but if you want to do heavier work with a graphical application then you need to use a compute node. When you've logged into the the virtual desktop :ref:`like above <virtual_desktop>`, you then request resources on a compute node using the `salloc <https://slurm.schedmd.com/salloc.html>`_ command. This takes the same options as the ``srun`` and ``sbatch`` commands so this should be familiar, here is an example:

.. code-block:: console
    :caption: this describes one node, one tasks and eight CPU cores for four hours

    $ salloc --nodes=1 --ntasks=1 --cpus-per-task=8 --time=04:00:00

You'll have to wait for the resources but when they are allocated you'll get output similar to that below:

.. code-block:: console

    [abc123@login2[viking2] ~]$ salloc --nodes=1 --ntasks=1 --cpus-per-task=8 --time=04:00:00
    salloc: Pending job allocation 689814
    salloc: job 689814 queued and waiting for resources
    salloc: job 689814 has been allocated resources
    salloc: Granted job allocation 689814
    flight start: Flight Direct environment is already active.
    [abc123@login2[viking2] ~]$


ssh into the compute node
^^^^^^^^^^^^^^^^^^^^^^^^^

There is an extra step, after requesting resources we need to manually ``ssh`` into the node where the resources have been allocated and ensure we use the ``-X`` option, we can easily do this using the ``$SLURM_NODELIST`` variable which Slurm sets for us:

.. code-block:: console

    [abc123@login2[viking2] ~]$ ssh -X $SLURM_NODELIST

Very shortly you'll be logged into the compute node, with all the login welcome text and then your prompt should look something like this:

.. code-block:: console

    [abc123@node064[viking2] ~]$

In this example I'm logged into ``node064``.


Run your program
^^^^^^^^^^^^^^^^

Once you're logged into the compute node, you can now load the modules and run your graphical program. In this example we run MATLAB:

.. code-block:: console

    $ module load MATLAB/2023b
    $ matlab

After a few moments, the window for MATLAB should appear in your virtual desktop yet it's running on the compute node.


Tidy up
^^^^^^^

After you're done close everything down and remember to :ref:`kill the virtual desktop <kill_sessions>` just like we showed before. Doing this will also ensure that the resources allocated from the ``salloc`` command will be relinquished.

Alternatively, you can manually relinquish the resources by pressing ``Ctrl + d`` twice from the terminal which you ``ssh`` connected to the compute node earlier. Once to exit the ``ssh`` session, and the second time to relinquish the job allocation from the ``salloc`` command, and you should see confirmation of this. From here you could then type a new ``salloc`` command and continue from that step if you wish, this could be useful for requesting different resources.

If for any reason you need to manually kill a job type ``squeue -u $USER`` to show all the jobs you have on Viking and then type ``scancel JOBID`` where ``JOBID`` is found from the previous command of the job you wish to cancel.


