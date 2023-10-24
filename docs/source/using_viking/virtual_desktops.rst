Virtual Desktops
================

You can create virtual desktop sessions to run graphical programs. There two main ways you can do this, on the login node and on a compute node.

.. attention::

    Remember, the login nodes are only for **light work** as mentioned in the :doc:`code of conduct <../getting_started/code_of_conduct>`, so if you need to use a GUI program for heavy work, then please ensure that is done on a compute node.


Login Node
----------

.. code-block:: console

Run the following line from within a login node

    $ alces session start gnome

And you will be presented with information similar to mine below:

.. code-block:: console
    :emphasize-lines: 4,5,7

    VNC server started:
        Identity: 743178ce-32d2-11ee-8df4-246e96c38380
            Type: gnome
            Host: 144.32.247.22
            Port: 5938
         Display: 38
        Password: 5jaHqekY
       Websocket: 41377

    Depending on your client, you can (insecurely by default) connect to the
    session using:

      vnc://nd996:5jaHqekY@144.32.247.22:5938
      144.32.247.22:5938
      144.32.247.22:38


    If prompted, you should supply the following password: 5jaHqekY


Connect to the Virtual Desktop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the appropriate application for your operating system (examples listed below), log into the virtual desktop. It will ask for a password (in my example this is ``5jaHqekY``), yours will be whatever was displayed in the previous step.

Windows
"""""""

On Windows you can connect using `TightVNC <https://www.tightvnc.com/download.php>`_. Using the above as an example (your details will be different), the ``Remote Host`` would be:

.. code-block:: console

    144.32.247.22:5938

Linux
""""""

`Remmina <https://remmina.org/how-to-install-remmina/>`_ is a good tool, run it and ensure you have ``VNC`` selected to the left of the address bar and use the same address:

.. code-block:: console

     144.32.247.22:5938


MacOS
""""""

 MacOS has built in support and you can use ``Finder`` for this, select ``Go`` and then ``Connect to server`` but the address is slightly different you must add ``vnc://`` to the beginning:

.. code-block:: console

    vnc://144.32.247.22:5938


.. _virtual_desktop:

Use the Virtual Desktop
^^^^^^^^^^^^^^^^^^^^^^^

You should soon be presented with a virtual desktop running on Viking. Click the ``Applications > System Tools > Terminal`` button to launch a terminal and you can load modules and programs as usual.

.. figure:: ../assets/img/virtual_desktop1.png
    :align: center
    :alt: a virtual desktop on Viking with the application menu open

    it's a virtual desktop, on a remote machine!


List Sessions
^^^^^^^^^^^^^

List all the current virtual desktops you have running with the following command:

.. code-block:: console

    $ alces session list

And you'll be presented with a list similar to mine below:

.. code-block:: console

    +----------+------------+--------------------+-----------------+---------+------+----------+
    | Identity | Type       | Host name          | Host address    | Display | Port | Password |
    +----------+------------+--------------------+-----------------+---------+------+----------+
    | 743178ce | gnome      | login2             | 144.32.247.22   |     :38 | 5938 | 5jaHqekY |
    +----------+------------+--------------------+-----------------+---------+------+----------+

.. _kill_sessions:

Kill Sessions
^^^^^^^^^^^^^

To kill a session you need to use the ``Identity`` code from the output above, use it with the following command:

.. code-block:: console

    $ alces session kill 743178ce

Your ``Identity`` code will be different to mine, this is just an example.


.. attention::

    It's important to ``kill`` any unused virtual desktops not just log out / close down the connection. They will still be running in the background using resources (remember the :doc:`code of conduct <../getting_started/code_of_conduct>`) so it's really important that you ``kill`` them after you are finished. If you leave too many running you will not be able to start a fresh one and will negatively impact other users.

.. _virtual_session_compute_node:

Compute Node
-------------

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
