Google drive
============

We know a number of Viking users like to store data on Google Drive.  It is possible to copy data directly from Viking to your Google Drive folder. Below we will provide instructions on how to set this up.

Setting up rclone on viking
---------------------------

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

Send data to Google drive
^^^^^^^^^^^^^^^^^^^^^^^^^

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


Retrieve data from Google drive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have data you wish to retrieve from your Google drive then using the above example folder, on Viking first ensure the ``rclone`` module is loaded:

.. code-block:: console

    $ module load {MOD_RCLONE}

Then to copy the folder from your Google drive to Viking:

.. code-block:: console

    $ rclone copy gdrive:viking-data ./

Or copy a single file:

.. code-block:: console

    $ rclone copy gdrive:viking-data/filename.zip ./


.. tip::

    More options for the ``copy`` command can be found on the `rclone docs <https://rclone.org/commands/rclone_copy/>`_ for example ``--max-age 24h`` to only retrieve files newer than 24 hours.


Reconnect rclone to Google drive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If it's been a while since you last used ``rclone`` you'll need to reconnect it to your google drive, here is an example:

.. code-block:: console

    $ rclone config reconnect gdrive:

Then answer the following questions:

    1. Already have a token - refresh? ``y``
    2. Use web browser to automatically authenticate rclone with remote? ``n``

You should then see similar output asking you to copy and paste the following line to your local machine to allow you to authenticate with Google. Make sure you copy the output from your terminal (not from the example below):

.. code-block:: console
    :emphasize-lines: 7

    Option config_token.
    For this to work, you will need rclone available on a machine that has
    a web browser available.
    For more help and alternate methods see: https://rclone.org/remote_setup/
    Execute the following on the machine with the web browser (same rclone
    version recommended):
    	rclone authorize "drive" "eyJjbGllbnRfc2VjcmpBdmZqRnhNG1kZ2dyMXZrbGguYXBwOV0IjoiR09DU1BYLXFmRUpBDktbjAzNXaTY4VHZMaGNjb2MyQ3BwdWkzZ2cy5nbI1NzUyNTU229nbGV1c2VyY29udGVudC5jb20iLCJjbGlfaWQiOiOTAwp1MW9qbDl2ZWprdlbnR
    Enter a value.
    config_token>


Paste it to a **local terminal** and run it, you may need to just try ``rclone authorize "drive"`` if it fails the first time and you're running an older version of ``rclone`` on your local device. A browser window should pop up, authenticate with google and in the local terminal you will receive a token like this:

.. code-block:: console

    {"access_token":"ys29.a2AfB_byA7dScgqO-Mmb3inj_vA4ekXEZeArV4DaXJquZlaOffvJb-6KrWJXtqP0ldI74NFf7vWN5_W2-jBBx1sIe_cpJucmS4PhKb2XJgVg_9WoBLSxLW_ptYjyIoI-j9fTa3TtTUEWkm2lIXKutr0I_I6Uv5GQXJIQV9aCgYdAc0SARISFQHGX2Mi-mGIzGP0lg0171-WkSxrrcBuvj","token_type":"Bearer","refresh_token":"1//03mj2JasEkNTQsgYIARAAGAMSNwF-L9Irw3sdt-H2jRP6o6sJzXqiNHgUjDSIOXDsnMthsW5yBCrKi3IymwWr7uLZwy0mmmcqsGc","expiry":"2023-12-25T11:00:24.685141432Z"}


Copy and paste that in the **Viking terminal**, press ``Enter`` and complete the final question about a 'team drive' (enter ``n`` if unsure). You can then run ``rclone config show`` to should show your token, you can now use ``rclone`` again.
