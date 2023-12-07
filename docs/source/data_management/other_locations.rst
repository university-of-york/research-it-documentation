Other locations
===============


Transferring data to Viking from another computer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are many other ways you can copy data to and from Viking and so we will only go over some general examples here using popular programs as a basic guide. For quick reference here are the important details::

    Hostname:   viking.york.ac.uk
    Port:       22
    Protocol:   SFTP


.. caution::
    If you are not connected to the campus network, please remember you must be connected to the `University VPN <https://www.york.ac.uk/it-services/services/vpn/>`_ first.


Windows
"""""""

If you are copying data from a Windows device it is recommended that you use `WinSCP <https://winscp.net/>`_ and their website has some good `tutorials for uploading and downloading files <https://winscp.net/eng/docs/task_index>`_ and other uses. Using the your ``username`` and the ``hostname``, ``port`` and ``protocol`` shown above, you should be able to connect to Viking and start moving files!


.. _transfer_files_linux:

Linux
"""""

You can copy your data from any Linux device to Viking using the following commands:

- ``scp``
- ``rsync``

For example, you can run the following commands from a terminal running on your device to move files to Viking.


scp
"""

This is recommended for transferring a small number of files. This example will copy data from your device to your ``scratch`` directory on Viking

.. hint::

    The 'tilde' symbol ``~`` is shorthand for your home directory, e.g ``/users/abc123``


.. code-block:: console
    :caption: for an individual file

    $ scp filename viking.york.ac.uk:~/scratch/


.. code-block:: console
    :caption: for a folder with lots of files

    $ scp -r dirname viking.york.ac.uk:~/scratch/

There are many options you can use with ``scp``.  To view these options run the following command to view the ``scp`` manual

.. code-block:: console

    $ man scp


rsync
"""""

This is recommended for a large number of files. Rsync can check what is already in place, therefore if the network is interrupted you can run the command again and it will pick up from where it was stopped. It will only transfer files that do not exist on the other server or files that have been changed.

.. code-block:: console
    :caption: this will copy your data from your device to your scratch area on Viking

    $ rsync -av dirname viking.york.ac.uk:~/scratch

.. code-block:: console
    :caption: this can be useful for copying a very large file from your device to your scratch area on Viking as it will allow you continue the transfer if the connection breaks for some reason

    $ rsync -P --append filename viking.york.ac.uk:~/scratch

There are many more options you can use with ``rsync``.  To view these options run the following command to view the ``rsync`` manual

.. code-block:: console

    $ man rsync


FileZilla
"""""""""

Filezilla is a fantastic graphical program for transferring files and can be used on both Windows, Linux, or MacOS. You can download it from `their website <https://filezilla-project.org/>`_.

To connect to Viking, enter your details in the boxes towards the top of the screen::

    Host:   viking.york.ac.uk
    Port:   22

For the username and password, enter your IT Services credentials.

After entering these details and connecting to Viking, your Viking area will appear on the right. You will now be able to click and drag files similar to the file manager. More information can be found in the `FileZilla documentation <https://wiki.filezilla-project.org/Using>`_.


