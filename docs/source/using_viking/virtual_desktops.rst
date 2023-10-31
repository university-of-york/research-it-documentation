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
      Identity: ef742a0c-63e7-4b7e-8aef-fa1bcca92e3f
          Type: gnome
       Host IP: 10.0.13.22
      Hostname: login2
          Port: 5902
       Display: :2
      Password: Nicdaij9
      Geometry: 1024x768

    This desktop session is not directly accessible from outside of your
    cluster as it is running on a machine that only provides internal
    cluster access.  In order to access your desktop session you will need
    to perform port forwarding using 'ssh'.

    Refer to 'flight desktop show ef742a0c' for more details.

    If prompted, you should supply the following password: Nicdaij9


More details on the virtual desktop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need more info, from the output copy and run the command from the line highlighted above. In this example it's  ``flight desktop show ef742a0c`` but for you the ``ef742a0c`` part will be different, please ensure you copy from the output on your session. As as example the output will look similar to this:

.. code-block:: console
    :emphasize-lines: 9,17

    == Session details ==
          Name:
      Identity: ef742a0c-63e7-4b7e-8aef-fa1bcca92e3f
          Type: gnome
       Host IP: 10.0.13.22
      Hostname: login2
          Port: 5902
       Display: :2
      Password: Nicdaij9
      Geometry: 1024x768

    This desktop session is not directly accessible from outside of your
    cluster as it is running on a machine that only provides internal
    cluster access.  In order to access your desktop session you will need
    to perform port forwarding using 'ssh':

      ssh -L 5902:10.0.13.22:5902 abc123@

    Once the ssh connection has been established, depending on your
    client, you can connect to the session using one of:

      vnc://abc123:Nicdaij9@localhost:5902
      localhost:5902
      localhost:2

    If, when connecting, you receive a warning as follows, try again with
    a different port number, e.g. 5903, 5904 etc.:

      channel_setup_fwd_listener_tcpip: cannot listen to port: 5902

    If prompted, you should supply the following password: Nicdaij9


Create the ssh tunnel
^^^^^^^^^^^^^^^^^^^^^

The virtual desktop isn't running on the login node, so we need a way to *tunnel* a connection from your computer to the login node, the command highlighted in the output above is incomplete but on Linux and MacOS from a terminal or in a PowerShell on an up to date Windows 10 or 11 system you would need to run the following:

.. code-block:: console
    :caption: substitute ``abc123`` for your actual username

    ssh -L 5902:10.0.13.22:5902 abc123@viking.york.ac.uk

Notice we added the ``viking.york.ac.uk`` address after ``abc123@``, this is a temporary issue we will shortly correct. Please ensure you substitute in your own username in place of ``abc123``. **Leave this terminal open**, it will function as our ``ssh tunnel``.


Connect to the virtual desktop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the appropriate application for your operating system (examples listed below), log into the virtual desktop. It will ask for a password (in my example this is ``Nicdaij9``), yours will be whatever was displayed in the previous step.

Windows
"""""""

On Windows you can connect using `TightVNC <https://www.tightvnc.com/download.php>`_. Using the above as an example, the ``Remote Host`` would be:

.. code-block:: console

    localhost:5902

Linux
""""""

`Remmina <https://remmina.org/how-to-install-remmina/>`_ is a good tool, run it and ensure you have ``VNC`` selected to the left of the address bar and use the same address:

.. code-block:: console

     localhost:5902


MacOS
""""""

 MacOS has built in support and you can use ``Finder`` for this, select ``Go`` and then ``Connect to server`` but the address is slightly different you must add ``vnc://`` to the beginning:

.. code-block:: console

    vnc://localhost:5902


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
    │      │ ef742a0c │ gnome │ login2    │ 10.0.13.22 │ :2 (5902)      │ Nicdaij9 │ Active │
    └──────┴──────────┴───────┴───────────┴────────────┴────────────────┴──────────┴────────┘


.. _kill_sessions:

Kill sessions
^^^^^^^^^^^^^

To kill a session you need to use the ``Identity`` code from the output above, use it with the following command:

.. code-block:: console

    $ flight desktop kill ef742a0c

Your ``Identity`` code will be different to mine, this is just an example.


.. attention::

    It's important to ``kill`` any unused virtual desktops not just log out / close down the connection. They will still be running in the background using resources (remember the :doc:`code of conduct <../getting_started/code_of_conduct>`) so it's really important that you ``kill`` them after you are finished. If you leave too many running you will not be able to start a fresh one and will negatively impact other users.

.. _virtual_session_compute_node:

Compute node
-------------

.. attention::

    This does not currently work and it being worked on, please bear with us.

The above method is great for light work like checking results but what if you want to do the heavy work with a GUI application? It's easy, when you get the the virtual desktop :ref:`like above <virtual_desktop>`, then you ask for some resources on a compute node, this is exactly the same as using the ``srun`` command however we use a special wrapper called ``start-interactive-session.sh`` in the terminal in the virtual desktop, for example:

.. code-block:: console
    :caption: like ``srun``, this describes 1 node, 20 tasks, for 4 hours and runs a bash shell

    $ start-interactive-session.sh -N 1 -n 20 -t 4:0:0 --pty /bin/bash

You'll have to wait for the resources and you'll get output similar to that below:

.. code-block:: console

    srun: job 25363864 queued and waiting for resources
    srun: job 25363864 has been allocated resources
    Enabling login2 to accept our X-connection... node001 being added to access control list

After this you'll have a new session on one of the compute nodes. Stay in this terminal, load your modules and run your program and it will be running on the compute node. After you're done close everything down and remember to kill the virtual desktop just like we showed :ref:`before <kill_sessions>`.
