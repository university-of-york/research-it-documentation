.. include:: /global.rst

Frequently asked questions
==========================

Here is a list of frequently asked questions about Viking, if you have any suggestions to add to this list please email itsupport@york.ac.uk


When I try to connect to Viking I get a warning that the ``fingerprint`` has changed, should I accept this?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you connected to the old Viking then your computer may have stored the old ``ssh fingerprint`` of the login nodes. As the new Viking has new login nodes it has new ssh fingerprints. Please check the fingerprints below and ensure they match what is being displayed in the terminal login screen:

.. code-block:: console

   SHA256:e6QUl1pE1RK55unuALoNDXaEvJLcam4LJo6P07nbGcs (RSA)
   SHA256:jn1KdPw+M9iws+uEwsnuqC5NVph4eNT095m22RFz4Mw (ECDSA)
   SHA256:TztJ/bGgPiK6bIGfQqRQnxfg/nVhw978T6kyy9HhJTQ (ED25519)

In a Linux or MacOS terminal or in a PowerShell or Command Prompt on and up to date Windows 10 or 11 system you can run ``ssh-keygen -R viking.york.ac.uk`` which will remove the old stored ``ssh fingerprint``. Connecting again with ``ssh abc123@viking.york.ac.uk`` (with your username in place of ``abc123``) should give you the option to check the new ``ssh fingerprint``, confirm it matches one of the above, and if so, accept the new ``ssh fingerprint``. You should then be connected and no longer receive the warnings about the ``ssh fingerprint``.


I need a shared folder for our team to able to access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can create a folder within ``/mnt/scratch/projects`` with the same name as your project code. User access can be controlled by one or more people in your team acting as 'admins' to the shared folder. Please email us to request a shared folder: itsupport@york.ac.uk


Can you increase my quota on '/mnt/scratch/users/'?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Absolutely, please email itsupport@york.ac.uk to request we increase your quota. Please try to keep it to what you will use and if you no longer need it please let us know so we can adjust it back. Please remember to take time to arrange for :doc:`regular back ups </getting_started/backing_up>` of your data as nothing on the ``scratch`` file system is backed up automatically. If your data is no longer needed, please delete it to free up space on the file system.


WinSCP shows "Error Listing Directory /mnt/lustre/users/"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is due to WinSCP using the folder path from the old Viking when trying to connect to the new Viking, which it saved from a previous session. As the folder path has changed slightly on the new Viking, WinSCP exits with this, or a similar error. To fix this please change the path to ``/mnt/scratch/users/abc123`` where ``abc123`` is your username.


How to ensure a particular node isn't used for my job?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you come across an issue with a particular node, perhaps something on that node has crashed, and your job suddenly fails on one particular node - let us know through itsupport@york.ac.uk. You can still continue your work by using the `exclude <https://slurm.schedmd.com/sbatch.html#OPT_exclude>`_ option to exclude the troubled node form being allocated. This will allow you to continue your work whilst we fix the problem.

If you're using a jobscript then add the following line:

.. code-block:: shell
   :caption: replace 'node123' with the name of the node to be excluded

   #SBATCH --exclude=node123

Or if you're using the `srun <https://slurm.schedmd.com/srun.html>`_ or `salloc <https://slurm.schedmd.com/salloc.html>`_ commands, then adding either of the following options will do:

.. code-block:: shell
   :caption: replace 'node123' with the name of the node to be excluded

   --exclude=node123
   -x node123


Why hasn't my job started?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Jobs submitted to the Slurm job scheduler will sometimes take some time before they start running. This can be for a number of reasons for example how busy the particular partition is that the job was submitted to or how many resources the job is requesting. It's always a good idea to request only the :ref:`resources <job_resources>` your job requires. You can check the jobs you have in the queue with the following command:

.. code-block:: console

   $ squeue -u $USER

If you see the reason for a job being held as ``QOSGrpGRES`` then this means a resource has reached its limit for that partition. For example, on the ``gpu_week`` partition only a total of three GPUs are allowed to be used by all users at the same time (on that particular partition). When this limit is reached all new jobs to the queue will be held with that reason code.

For more information there is a full list of `reason codes <https://slurm.schedmd.com/resource_limits.html#reasons>`_.
