Connecting to viking
====================

.. hint::
    Before you can connect to Viking you'll need a :ref:`project code and a user account<creating-an-account>`.

To access Viking you'll need to be on the campus network or using the VPN :doc:`which you can read about here. </getting_started/connecting_off_campus>`


Terminal access
---------------

Linux and macOS
^^^^^^^^^^^^^^^

To log in from a terminal emulator, use the following command:

.. code-block:: console

    $ ssh viking.york.ac.uk

You will be prompted for your IT Services password. If you're using a personal device then you'll need to add your IT Services username for example:

.. code-block:: console

    $ ssh abc123@viking.york.ac.uk

.. hint::
    X11 forwarding will only work on the Viking login nodes, which means that you won't be able to run graphical applications e.g. MATLAB on the Viking compute nodes using X11 forwarding. Details about virtual desktop sessions on Viking :doc:`can be found here </using_viking/virtual_desktops>`.

.. _connecting-via-windows:

Windows
^^^^^^^

For terminal access to Viking from a Windows desktop, you will need to install `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`_ (or comparable software).


Configuring PuTTY to connect to viking
"""""""""""""""""""""""""""""""""""""""

Open PuTTY and configure it to connect to Viking:

1. Add the name 'viking.york.ac.uk' to the 'Host Name' field
2. Check the 'Connection Type' to SSH
3. Type the name 'Viking' in 'Saved Sessions'
4. Click 'Save'

.. image:: ../assets/img/putty1.png

Connecting to viking
"""""""""""""""""""""

1. Start PuTTY
2. Select 'Viking' from the 'Saved Sessions'
3. Click 'Open'

.. image:: ../assets/img/putty2.png

A terminal window should appear. Log in with your university username and password.

.. image:: ../assets/img/putty3.png

If you are successful this is what you will see:

.. image:: ../assets/img/putty4.png

