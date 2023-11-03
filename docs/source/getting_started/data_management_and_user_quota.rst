Data management and user quota
==============================

.. FIXME: This uses OLD information

Viking is a self-contained machine, therefore you will notice your normal UoY home directories are not available. This is intentional for the following reasons:

- If the dedicated network link between campus and Viking goes down, it may cause slowness or jobs to fail. Instead, jobs should continue to run until the link is re-established
- If a user tries to read/write from the University filestores using Viking, it is possible that they could bring the entire storage system down for the University
- UoY home directories are not designed for high-performance computing. Instead Viking has its own filesystem designed for high-performance


Your area on viking explained
-----------------------------

When you log in to Viking, you will land in your home directory, specifically:

.. code-block:: console

    /users/abc123

Where ``abc123`` will be replaced by your username. This ``home`` directory has a size of **100GB** and a file limit of **200,000**. From within the ``home`` directory, you can access your ``scratch`` directory, which is a special high-performance filestore with a default size of **2TB** and **no limit** on the number of files.

.. code-block:: console

    /mnt/scratch/users/abc123/

.. FIXME: needs size


.. tip::
    If you need more ``scratch`` storage space, please email us at itsupport@york.ac.uk, we are more than happy to accommodate large projects.


.. FIXME: add size, and file duration

Additionally you also have access to a ``localtmp`` folder which points to storage space on the *current node* which you are logged into, on fast SSD drives. It's also an area which is **not backed up** so should only be used for processing data whilst it's in use, after which the data should be backed up or archived if needed. You can access this directory at:

.. code-block:: console

    /users/abc123/localtmp



Checking your quota
-------------------

To check how much space you have left, run the following command:

.. code-block:: console

    $ myquota

Which will produce something similar to the following result:

.. FIXME: update this

.. code-block:: console

    Scratch quota:
    Disk quotas for usr abc123 (uid 12345):
         Filesystem    used   quota   limit   grace   files   quota   limit   grace
       /mnt/scratch      4k      2T    2.1T       -       1       0       0       -
    uid 12860 is using default block quota setting
    uid 12860 is using default file quota setting

    Home quota:
    Disk quotas for user abc123 (uid 12345):
         Filesystem   space   quota   limit   grace   files   quota   limit   grace
    10.10.0.15:/export/users
                       232K    100G    110G              57    200k    250k


What happens if you exceed your quota
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you login to Viking you will be told if you are over quota. If this is in users area with the **100GB** or **200,000** files limit you will need to delete or move your files to your ``scratch`` area.  **There is a grace period of 7 days after which you will lose access to Viking.**

If you are over quota in the ``scratch`` area and need more space please email itsupport@york.ac.uk where we can increase your quota. **There is a grace period of 7 days after which you will lose access to Viking.**

.. tip::
    The most common reason for exceeding your quota in your home directory is by storing ``conda`` environments directly in your home directory. The solution for that is to :ref:`set up your Conda environment first <conda_setup>`.


Copying and moving your data to viking
--------------------------------------

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


Moving data to google drive directly from viking
------------------------------------------------

We know a number of Viking users like to store data on Google Drive.  It is possible to copy data directly from Viking to your Google Drive folder. Below we will provide instructions on how to set this up.

Setting up rclone on viking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to use ``rclone``, you will need a ``client-id``, the steps for which can be found on the `rclone website <https://rclone.org/drive/#making-your-own-client-id>`_.
You will also need to either have a local install of `rclone`, or to be doing the setup in a Virtual Desktop.

Login to Viking and navigate to an area on your scratch folder, then load the ``rclone`` module.

.. code-block:: console

    $ module load {MOD_RCLONE}

Next, for the first time using rclone, you will need to configure it using the following command

.. code-block:: console

    $ rclone config

``rclone`` will then ask you a number of questions, including asking for your ``client-id``. We recommend the following answers:

    1.  Action: ``n`` - new remote
    2.  Name: Choose something sensible without spaces (I used ``gdrive``)
    3.  Storage: ``Google Drive`` (NB: do not select "Google Cloud Storage")
    4.  Application Client Id: See step above to create an ID
    5.  Client Secret: See step above to create an ID
    6.  Scope: ``drive.file`` (or ``drive`` if you want to be able to download files from Google Drive onto Viking)
    7.  ``Enter`` - ID of the root folder
    8.  Service account credentials: ``Enter`` to leave empty
    9.  Edit advanced config: ``n``
    10. Web browser authenticate: ``n`` (or Yes if in a Virtual Desktop)
    11. Follow the steps to authenticate locally
    12. Configure this as a Shared Drive: ``n``
    13. ``y`` - This is okay
    14. ``q``

You are now ready to transfer files from Viking to your Google Drive.  This can be done with the following command

.. code-block:: console

    $ rclone copy directory_to_copy/ gdrive:viking-data

.. note::

    - ``directory_to_copy`` is the directory of files you wish to transfer
    - ``gdrive`` is the name you gave earlier when configuring rclone
    - ``viking-data`` is the name of the folder your files will be moved to inside your google drive

If you login into Google Drive you should see the files from ``directory_to_copy`` inside a folder named ``viking-data``

.. hint::
    If you see the following error message please check you are not trying to sync to a **Shared Drive** (previously known as Team Drives) instead. If you are trying to sync to a team drive you will need to amend question 12 to ``y``.

.. code-block:: console

    2021/08/16 11:33:23 Fatal error: listing Team Drives failed: googleapi: Error 403: Insufficient Permission: Request had insufficient authentication scopes., insufficientPermissions


Dropoff service
---------------

The York `DropOff Service <https://www.york.ac.uk/it-services/services/dropoff/>`_ is a web page that lets you easily and securely exchange files up to 128G with University staff and students or external people. Files are automatically deleted after 14 days and all files are transferred across the network `securely encrypted <https://dropoff.york.ac.uk/security>`_.
