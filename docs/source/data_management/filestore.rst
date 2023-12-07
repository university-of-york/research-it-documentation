Storage
-------

If you need to transfer data to Viking from your department's shared storage space one of the fastest ways is doing this is by being logged into Viking and initiating the transfer there.

Transfer data from the shared storage directly to Viking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's possible to be logged into Viking and directly copy data across from your `shared filestore <https://www.york.ac.uk/it-services/filestore/rented/>`_ over `scp, sftp or rsync <https://www.york.ac.uk/it-services/services/file-transfer/>`_. You'll need to know the path to the folder but an example is shown below. Here we use ``scp`` to copy a folder to the current folder on Viking:

.. code-block:: console
    :caption: replace '<filestore>' with the path to your folder

    $ scp -r scp.york.ac.uk:/shared/storage/<filestore> .

The dot ``.`` at the end tells ``scp`` to copy the folder to the current directory, in this case it's ``<filestore>`` but you should change that to the correct folder path on the shared storage. You can change the ``.`` to any path you have access to (normally within your home folder).

Personal filestore
""""""""""""""""""

The following is the path for your `personal filestore <https://www.york.ac.uk/it-services/filestore/>`_:

.. code-block:: console

    $ scp -r scp.york.ac.uk:/home/userfs/a/abc123 .

Where ``a`` and ``abc123`` are the first letter of your username followed by your username. This is your `personal filestore <https://www.york.ac.uk/it-services/filestore/>`_.


Bioldata filestore
"""""""""""""""""""

For ``bioldata`` filestores the paths are either:

.. code-block:: console

    $ scp -r scp.york.ac.uk:/shared/biology/bioldata1/<filestore> .
    $ scp -r scp.york.ac.uk:/shared/biology/bioldata2/<filestore> .

Replace ``<filestore>`` is the rest of the path the your data. You can check this path by logging onto one or the `interactive research servers <https://wiki.york.ac.uk/display/RCS/Interactive+Research+Linux+Service>`_ and looking for the path in ``/shared/biology/bioldata1/`` and ``/shared/biology/bioldata1/``
