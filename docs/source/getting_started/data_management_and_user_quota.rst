Data Management and User Quota
==============================

.. attention::

    FIXME: This uses OLD information

Viking is a self-contained machine, therefore you will notice your normal UoY home directories are not available. This is intentional for the following reasons:

- If the dedicated network link between campus and Viking goes down, it may cause slowness or jobs to fail. Instead, jobs should continue to run until the link is re-established
- If a user tries to read/write from the university filestores using Viking, it is possible that they could bring the entire storage system down for the university
- UoY home directories are not designed for high-performance computing. Instead Viking has its own filesystem designed for high-performance


Your Area on Viking Explained
-----------------------------

When you log in to Viking, you will land in your home directory, specifically:

.. code-block:: console

    /users/abc123

Where ``abc123`` will be replaced by your username. This home directory has a size of **50GB** and a file limit of **100,000**. From within the home directory, you can access your ``scratch`` directory at

.. code-block:: console

    /users/abc123/scratch

This is a special high-performance filestore with a default size of **3TB** and **no limit** on the number of files. Because of this, you should run all your jobs on Viking from this directory rather than the home directory.

.. tip::
    If you need more ``scratch`` storage space, please email us at itsupport@york.ac.uk, we are more than happy to accommodate large projects.


Additionally, you also have access to the ``warm storage`` area, linked as ``FIXME: warm_storage`` which is **FIXME:??TB** and has no file limit. This is used for FIXME: What is it used for?

.. code-block:: console

    /users/abc123/FIXME: warm

Checking Your Quota
-------------------

To check how much space you have left, run the following command:

.. code-block:: console

    $ myquota

Which will produce the following result:

.. code-block:: console

    Scratch quota:
    Disk quotas for usr abc123 (uid 12345):
         Filesystem    used   quota   limit   grace   files   quota   limit   grace
        /mnt/lustre  254.5G      3T    3.1T       - 1465164       0       0       -

    Home quota:
    Disk quotas for user abc123 (uid 12345):
         Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
    storage:/export/users
                      31384  52428800 78643200             318  100000  150000


What Happens If You Exceed Quota
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you login to Viking you will be told if you are over quota. If this is in users area with the **50GB** or **100,000** files limit you will need to delete or move your files to your ``scratch`` area.  **There is a grace period of 7 days after which you will lose access to Viking.**

If you are over quota in the ``scratch`` area and need more space please email itsupport@york.ac.uk where we can increase your quota. **There is a grace period of 7 days after which you will lose access to Viking.**

.. tip::
    The most common reason for exceeding your quota in your home directory is by storing ``conda`` environments directly in your home directory. The solution for that is to :ref:`set up your Conda environment first <conda_setup>`.


Copying and Moving Your Data to Viking
--------------------------------------

There are many ways you can copy data to and from Viking and so we will only go over some general examples here using popular programs as a basic guide. For quick reference here are the important details::

    Hostname:   viking.york.ac.uk
    Port:       22
    Protocol:   SFTP


.. caution::
    If you are not connected to the campus network, please remember you must be connected to the `university VPN <https://www.york.ac.uk/it-services/services/vpn/>`_ first.


Windows
^^^^^^^

If you are copying data from a Windows device it is recommended that you use `WinSCP <https://winscp.net/>`_ and their website has some good `tutorials for uploading and downloading files <https://winscp.net/eng/docs/task_index>`_ and other uses. Using the your ``username`` and the ``hostname``, ``port`` and ``protocol`` shown above, you should be able to connect to Viking and start moving files!


.. _transfer_files_linux:

Linux
^^^^^

You can copy your data from any Linux device to Viking using the following commands:

- ``scp``
- ``rsync``

For example, you can run the following commands from a terminal running on your device to move files to Viking.


scp
^^^

This is recommended for transferring a small number of files. This example will copy data from your device to your ``scratch`` directory on Viking

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
^^^^^

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
^^^^^^^^^

Filezilla is a fantastic graphical program for transferring files and can be used on both Windows, Linux, or MacOS. You can download it from `their website <https://filezilla-project.org/>`_.

To connect to Viking, enter your details in the boxes towards the top of the screen::

    Host:   viking.york.ac.uk
    Port:   22

For the username and password, enter your IT Services credentials.

After entering these details and connecting to Viking, your Viking area will appear on the right. You will now be able to click and drag files similar to the file manager. More information can be found in the `FileZilla documentation <https://wiki.filezilla-project.org/Using>`_.


Moving Data to Google Drive Directly from Viking
------------------------------------------------

We know a number of Viking users like to store data on Google Drive.  It is possible to copy data directly from Viking to your Google Drive folder. Below we will provide instructions on how to set this up.

Setting up rclone on Viking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to use ``rclone``, you will need a ``client-id``, the steps for which can be found on the `rclone website <https://rclone.org/drive/#making-your-own-client-id>`_.

Login to Viking and navigate to an area on your scratch folder, then load the ``rclone`` module.

.. code-block:: console

    $ module load tools/rclone

Next, for the first time using rclone, you will need to configure it using the following command

.. code-block:: console

    $ rclone config

``rclone`` will then ask you a number of questions, including asking for your ``client-id``. We recommend the following answers:

    1.  ``n`` - new remote
    2.  Give it a name - don't use spaces, makes it awkward (I used ``gdrive``. Remember this as you will need it later)
    3.  ``16`` - Google Drive (NB: do not select "google cloud storage")
    4.  ``Enter`` - Application Client Id (see step above to create an ID)
    5.  ``Enter`` - Client Secret (see step above to create an ID)
    6.  ``3`` - Scope
    7.  ``Enter`` - ID of the root folder
    8.  ``Enter`` - Service account credentials
    9.  ``n`` - Edit advanced config
    10. ``n`` - Use auto config
    11. Copy and paste the URL provided into your browser
    12. Authorize app with click through
    13. Copy and paste code back into terminal
    14. ``n`` - Configure this as Team Drive
    15. ``y`` - This is okay
    16. ``q``

You are now ready to transfer files from Viking to your Google Drive.  This can be done with the following command

.. code-block:: console

    $ rclone copy directory_to_copy/ gdrive:viking-data

.. note::

    - ``directory_to_copy`` is the directory of files you wish to transfer
    - ``gdrive`` is the name you gave earlier when configuring rclone
    - ``viking-data`` is the name of the folder your files will be moved to inside your google drive

If you login into Google Drive you should see the files from ``directory_to_copy`` inside a folder named ``viking-data``

.. hint::
    If you see the following error message please check you are not trying to sync to a **team drive** instead. If you are trying to sync to a team drive you will need to amend question 14 to ``y``.

.. code-block:: console

    2021/08/16 11:33:23 Fatal error: listing Team Drives failed: googleapi: Error 403: Insufficient Permission: Request had insufficient authentication scopes., insufficientPermissions


DropOff Service
---------------

The York `DropOff Service <https://www.york.ac.uk/it-services/services/dropoff/>`_ is a web page that lets you easily and securely exchange files up to 128G with University staff and students or external people. Files are automatically deleted after 14 days and all files are transferred across the network `securely encrypted <https://dropoff.york.ac.uk/security>`_.
