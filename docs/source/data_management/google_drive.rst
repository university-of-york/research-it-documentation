Google drive
------------

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
