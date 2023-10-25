Backing Up your Data
====================

There are two main options depending on how frequently you need to access the data, the University **Filestore** or the **Vault**.

The **Vault** provides unlimited cold storage and is appropriate for storing sensitive data but retrieving the data can take some time and may incur a charge

The **Filestore** is more readily accessible, if you need more space please contact itsupport@york.ac.uk. If you use the Filestore for backing up, usually the data will be transferred to the Vault for archiving later.


.. warning::

    Please ensure you **regularly** back up your data, if there is a catastrophic failure all data on Viking could be lost!


The Vault
----------

Vault is a file archiving service.  It can be used to store files that need to be kept, but are unlikely to be accessed again.  The main use is for storing research data which needs to be kept for contractual or other reasons, but is probably never going to be used or looked at again. Please see the `Vault User Guide <https://support.york.ac.uk/s/article/Vault-User-Guide>`_ for more details.


Filestore
---------

Please see the University's `Filestore guide <https://www.york.ac.uk/it-services/filestore/rented/>`_ for more information about accessing and using this service.
To move your data from Viking and to the Filestore ("Storage"), the address you need to use as an example is::

    sftp.york.ac.uk:/shared/storage/<filestore>


.. tip::

    Please speak to your department if you need access to your department's shared filestore.


You can use ``PuTTY`` on Windows and the command line on Linux and MacOS with commands such as ``rsync``  and ``scp`` much like the examples on the :ref:`Data Management page <transfer_files_linux>`, examples below.

.. code-block:: console
    :caption: copies a file 'filename' to your filestore

    $ scp filename sftp.york.ac.uk:/shared/storage/<filestore>

.. code-block:: console
    :caption: copies a directory 'dirname' to your filestore

    $ scp -r dirname sftp.york.ac.uk:/shared/storage/<filestore>

The ``-r`` option means it copies the directory recursively.

.. code-block:: console
    :caption: copies a directory 'dirname' to your filestore

    $ rsync -av dirname sftp.york.ac.uk:/shared/storage/<filestore>

Options ``a`` set up a number of options useful for *archiving*, ``v`` for *verbose* so you can monitor the process.

.. code-block:: console
    :caption: copies a file 'filename' to your filestore

    $ rsync -P --append filename sftp.york.ac.uk:/shared/storage/<filestore>

Option ``-P`` sets the ``--partial`` and ``--progress`` options, which will *keep partially transferred files* and shows *progress*. The ``--append`` option will *append data onto shorter files*. Together this is handy if a large file needs to be transferred but for some reason could get interrupted. Rerunning this command should pick up where it left off.


.. hint::

    If you use the above commands on Viking to transfer files why not look into using :doc:`tmux or screen </using_viking/terminal_multiplexing>`, and this will allow you to ``detach`` from the terminal where it will continue to run ready for your return later.
