Storage quota
=============

.. attention::

    Viking is a self-contained machine, therefore you will notice your normal UoY home directories are not available. This is intentional for the following reasons:
    - If the dedicated network link between campus and Viking goes down, it may cause slowness or jobs to fail. Instead, jobs should continue to run until the link is re-established
    - If a user tries to read/write from the University filestores using Viking, it is possible that they could bring the entire storage system down for the University
    - UoY home directories are not designed for high-performance computing. Instead Viking has its own filesystem designed for high-performance


Your area on Viking explained
-----------------------------

When you log in to Viking, you will land in your home directory, specifically:

.. code-block:: console

    /users/abc123

Where ``abc123`` will be replaced by your username. This ``home`` directory has a size of **100GB** and a file limit of **400,000**. From within the ``home`` directory, you can access your ``scratch`` directory, which is a special high-performance filestore with a default size of **2TB** and **no limit** on the number of files.

.. code-block:: console

    /mnt/scratch/users/abc123/


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
    uid 12345 is using default block quota setting
    uid 12345 is using default file quota setting

    Home quota:
    Disk quotas for user abc123 (uid 12345):
         Filesystem   space   quota   limit   grace   files   quota   limit   grace
    10.10.0.15:/export/users
                       232K    100G    110G              57    400k    500k


What happens if you exceed your quota
-------------------------------------

When you login to Viking you will be told if you are over quota. If this is in users area with the **100GB** or **400,000** files limit you will need to delete or move your files to your ``scratch`` area.  **There is a grace period of 7 days after which you will lose access to Viking.**

If you are over quota in the ``scratch`` area and need more space please email itsupport@york.ac.uk where we can increase your quota. **There is a grace period of 7 days after which you will lose access to Viking.**


Transferring file to and from Viking or backing up
--------------------------------------------------

Please see the **DATA MANAGEMENT** section with links to various locations and methods to transfer data to a from Viking for more information.
