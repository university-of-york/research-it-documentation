Filestore ("Storage")
=====================

Please see the University's `Filestore guide <https://www.york.ac.uk/it-services/filestore/rented/>`_ for more information about accessing and using this service.


Send data to the Filestore
--------------------------


To move your data from Viking and to the Filestore ("Storage"), the address you need to use as an example is::

    sftp.york.ac.uk:/shared/storage/<filestore>


.. tip::

    Please speak to your department if you need access to your department's shared filestore.


You can use ``PuTTY`` on Windows and the command line on Linux and MacOS with commands such as ``rsync``  and ``scp`` much like the examples on the :ref:`Data Management page <transfer_files_linux>`, examples below.

Using the ``scp`` command
^^^^^^^^^^^^^^^^^^^^^^^^^

To copy a file 'filename' to your filestore
"""""""""""""""""""""""""""""""""""""""""""
.. code-block:: console

    $ scp filename scp.york.ac.uk:/shared/storage/<filestore>

To copy a directory 'dirname' to your filestore
"""""""""""""""""""""""""""""""""""""""""""""""
.. code-block:: console

    $ scp -r dirname scp.york.ac.uk:/shared/storage/<filestore>

The ``-r`` option means it copies the directory recursively.

Using the ``rsync`` command
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To copy a file 'filename' to your filestore
""""""""""""""""""""""""""""""""""""""""""""
.. code-block:: console

    $ rsync -P --append filename sftp.york.ac.uk:/shared/storage/<filestore>

Option ``-P`` sets the ``--partial`` and ``--progress`` options, which will *keep partially transferred files* and shows *progress*. The ``--append`` option will *append data onto shorter files*. Together this is handy if a large file needs to be transferred but for some reason could get interrupted. Rerunning this command should pick up where it left off.

To copy a directory 'dirname' to your filestore
"""""""""""""""""""""""""""""""""""""""""""""""
.. code-block:: console

    $ rsync -av dirname sftp.york.ac.uk:/shared/storage/<filestore>

Options ``a`` set up a number of options useful for *archiving*, ``v`` for *verbose* so you can monitor the process.

.. hint::

    If you use the above commands on Viking to transfer files why not look into using :doc:`tmux or screen </using_viking/terminal_multiplexing>`, and this will allow you to ``detach`` from the terminal where it will continue to run ready for your return later.


Retrieve data from the Filestore
--------------------------------

If you need to transfer data to Viking from your department's shared storage space one of the fastest ways is doing this is by being logged into Viking and initiating the transfer there.

It's possible to be logged into Viking and directly copy data across from your `shared filestore <https://www.york.ac.uk/it-services/filestore/rented/>`_ over `scp, sftp or rsync <https://www.york.ac.uk/it-services/services/file-transfer/>`_. You'll need to know the path to the folder or file you wish to transfer to Viking. Here we use ``scp`` to copy a folder to the current folder on Viking:

Using the ``scp`` command
^^^^^^^^^^^^^^^^^^^^^^^^^

To copy a file 'filename' from your filestore
"""""""""""""""""""""""""""""""""""""""""""""

Replace ``<filestore>`` with the path to your filestore and ``<filename>`` with the name of your file:

.. code-block:: console

    $ scp scp.york.ac.uk:/shared/storage/<filestore>/<filename> .


To copy a directory 'dirname' from your filestore
"""""""""""""""""""""""""""""""""""""""""""""""""

Replace ``<filestore>`` with the path to your filestore and ``<dirname>`` with the name of the folder you with to copy to Viking:

.. code-block:: console

    $ scp -r scp.york.ac.uk:/shared/storage/<filestore>/<dirname> .

.. tip::

    The dot ``.`` at the end tells ``scp`` to copy the folder to the current directory. You can change the ``.`` to any path you have access to (normally within your home folder).


Using the ``rsync`` command
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To copy a file 'filename' from your filestore
"""""""""""""""""""""""""""""""""""""""""""""

Replace ``<filestore>`` with the path to your filestore and ``<filename>`` with the name of your file:

.. code-block:: console

    $ rsync -P --append sftp.york.ac.uk:/shared/storage/<filestore>/<filename> .


To copy a directory 'dirname' from your filestore
"""""""""""""""""""""""""""""""""""""""""""""""""

Replace ``<filestore>`` with the path to your filestore and ``<dirname>`` with the name of the folder you with to copy to Viking:

.. code-block:: console

    $ rsync -av sftp.york.ac.uk:/shared/storage/<filestore>/<dirname>



Personal filestore
^^^^^^^^^^^^^^^^^^

The following is the path for your `personal filestore <https://www.york.ac.uk/it-services/filestore/>`_:

.. code-block:: console

    scp.york.ac.uk:/home/userfs/a/abc123

Where ``a`` and ``abc123`` are the first letter of your username followed by your username. This is your `personal filestore <https://www.york.ac.uk/it-services/filestore/>`_. Use this with the examples above to send data to or retrieve data from your personal filestore.

