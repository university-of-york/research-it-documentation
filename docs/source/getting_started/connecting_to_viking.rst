Connecting to Viking
====================

.. attention::
    Before you can connect to Viking you'll need a :ref:`project code and a user account<creating-an-account>`.

To access Viking you'll need to be on the campus network or using the VPN :doc:`which you can read about here. </getting_started/connecting_off_campus>`


Terminal access
---------------

Linux, MacOS and Windows PowerShell
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    The latest builds of Windows 10 and Windows 11 include a built-in ``ssh`` client, so you can run ``ssh`` commands directly from a ``CMD`` or ``PowerShell`` window. To run either of these search for ``CMD`` or ``PowerShell`` from the Windows search box and then type in the below command. If you're using a personal device and need to install the ``ssh`` client please follow the `Microsoft website <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui#install-openssh-for-windows>`_. Alternatively you can install ``PuTTY`` and use it as :ref:`described below <connecting-via-windows>`.

To log in from a terminal emulator, use the following command:

.. code-block:: console
    :caption: remember to substitute 'abc123' for your own username

    $ ssh abc123@viking.york.ac.uk

You will be prompted for your IT Services password.

.. note::

    If you previously connected to the old Viking then you may see a warning that the fingerprint has changed. Please see the :doc:`FAQ </faq/faq>` for how to overcome this.

.. _connecting-via-windows:

Windows
^^^^^^^

Alternatively, for terminal access to Viking from a Windows desktop, you can install `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`_ (or comparable software).


Configuring PuTTY to connect to Viking
"""""""""""""""""""""""""""""""""""""""

Open PuTTY and configure it to connect to Viking:

1. Add the name 'viking.york.ac.uk' to the 'Host Name' field
2. Check the 'Connection Type' to SSH
3. Type the name 'Viking' in 'Saved Sessions'
4. Click 'Save'

.. image:: ../assets/img/putty1.png

Connecting to Viking
"""""""""""""""""""""

1. Start PuTTY
2. Select 'Viking' from the 'Saved Sessions'
3. Click 'Open'

.. image:: ../assets/img/putty2.png

A terminal window should appear. Log in with your University username and password.

.. image:: ../assets/img/putty3.png

If you are successful this is what you will see:

.. image:: ../assets/img/putty4.png

