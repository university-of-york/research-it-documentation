.. include:: /global.rst

.. custom CSS to help the table render nicer
.. raw:: html

   <style>
    /* widen the page slightly to help the table render */
    .wy-nav-content { max-width: 900px !important; }

    /* lock the first column so scrolling makes it easier to compare */
    #storage-on-viking > div > table > tbody > tr > th,
    #storage-on-viking > div > table > thead > tr > th.head.stub {
        background-color: #fcfcfc;
        position: sticky;
        z-index: 2;
        left: 0;
        width: 2em;
    }

    #storage-on-viking > div > table > tbody > tr > td {
        position: relative;
        z-index: 1;
    }
   </style>

Storage on Viking
=================


It is vital that users continue to manage their data on the Viking cluster. There are currently 6 areas where data can be stored. Below details the areas, the type of data you should store there and what is/isn't backed up.

.. csv-table::
    :file: /assets/data/viking_storage.csv
    :header-rows: 1
    :stub-columns: 1


*\* (can be increased on request)*


Scratch
--------

Scratch is a high performance file system that runs Lustre. The `Lustre <https://www.lustre.org/>`_ file system is an open-source, parallel file system that supports High Performance Computing (HPC) environments. Scratch works best when the filesystem is not at capacity. To ensure it remains efficient we will be implementing a policy where data will be deleted automatically if it has **not been touched in 90 days**. If you wish to keep your data please ensure it is backed up on the University filestore ``storage.york.ac.uk`` or in the cloud or move to Longship (see below).


We will be making exceptions to this rule for certain project directories where groups share data between teams. This is to encourage users to not download the same datasets multiple times.


Scratch (Flash)
---------------

For data IO intensive workflows you may find better performance using our high performance flash storage. This filesystem also runs lustre. The overall capacity is smaller therefore we ask users to clean up and delete data after use. To use flash scratch perform the following steps:

.. code-block:: console

    $ mkdir test-dir
    $ lfs setstripe --pool flash test-dir


Then write to the directory that has the flash pool set. By default that just stripes over one `Object Storage Targets (OST) <https://wiki.lustre.org/Lustre_Object_Storage_Service_(OSS)>`_, to stripe across e.g. 10:

.. code-block:: console

    $ lfs setstripe --pool flash -c 10 test-dir


.. note::

    It's easiest to create a new dir with the striping set, then ``cp`` the files there (**don't use** ``mv`` as this only updates the metadata, the underlying objects remain the same). For better lustre performance it may be worth explicitly striping across multiple OSTs there as well. Striping in Lustre should only be used for large files, using it for small files can actually degrade performance. Further guidance on using lustre to achieve maximum performance can be found `here <https://oit.utk.edu/hpsc/lustre-striping-guide/>`_.

.. attention::

    Please remember to delete your data after you've finished using the flash storage.


Longship
--------

If you have data which needs to be kept on scratch but might not be used in the next 90 days you can copy it to *Longship*. This is not a high-performance filestore but can be used to save data so users do not have to copy datasets back and forth to Viking from campus. Longship is mounted read/write on the Viking login nodes and read only on the compute nodes. If you only have a small number of files to read for your job you might be able to do this direct from Longship. You can also access Longship on campus. The hope is to simplify the data journey for users, whilst also taking a lead on curating your data.

Location
^^^^^^^^

Below are the paths for accessing Longship from various locations.

Viking
""""""

.. code-block:: console

    /mnt/longship/users

    /mnt/longship/projects


Campus (SFTP/Linux)
""""""""""""""""""""
.. code-block:: console

    /shared/longship/users

    /shared/longship/projects


Campus (Windows)
""""""""""""""""

.. code-block:: console

    \\longship.york.ac.uk\users

    \\longship.york.ac.uk\projects




