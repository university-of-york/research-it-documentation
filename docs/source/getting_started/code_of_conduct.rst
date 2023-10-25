Code of Conduct
===============

.. FIXME: Needs suggestions

We hope everyone enjoys using Viking and all its powerful resources. As all of Viking's resources are shared amongst all users, it's up to all of us to do our best to ensure we are using them wisely and not negatively impacting other users. We understand that for some people this may be the first time they have access to a HPC like Viking, or even the first time using a Linux machine, so we have created this page to provide some guidelines for using Viking responsibly and considerately. As always, if you need help with any explanation please get in touch with the team by emailing itsupport@york.ac.uk.


Running Tasks on the Login Nodes
--------------------------------

When you first log in to Viking you, and every other user, will be logged into one of the ``login nodes``. These act as gateways to the ``compute nodes``, which is where all the hard work should be done. The login nodes are meant for transferring files, writing code, viewing results and other similar **light work**. If you have a task which crunches through a massive data set, spinning off multiple instances and taking up as many CPUs as it can to get the job done, then running this task on a login node will negatively impact upon other people's ability to do their work.

Please run all serious work through the ``slurm`` job scheduler, this way they are run on the compute nodes, not the login nodes and you can control their resources. You can read about ``Slurm`` and how to send jobs to it on the :doc:`scheduling jobs page </using_viking/submitting_jobs>`.


Closing Virtual Desktop Sessions
--------------------------------

`Virtual desktop sessions <using_viking/virtual_desktops.html>`_ don't close if you simply disconnect, this is to allow you to come back to them at a later time. If you do not ``kill`` the virtual desktop after you have finished and later create new ones, more and more virtual desktops will be running taking up resources. This is why it's required to simply :ref:`kill virtual desktops when finished with <kill_sessions>`.


Backing up data
----------------

The ``scratch`` folder, a large area in your home directory where you can store data, is **not backed up**. This is partly due to the sheer size of the filesystem and means that backing up data is each user's responsibility. In a worst case scenario all data could be lost, therefore you should regularly :doc:`back up your data </getting_started/backing_up>`. If you need any help with this, please get in touch with itsupport@york.ac.uk.


Deleting Unneeded Files
-----------------------

We strongly encourage all users to take time to periodically sort through their data on Viking, back up the data and when it's successfully backed up, delete it from Viking if it's no longer needed. This frees up space for other people's data on the filesystem and helps avoid us reaching storage limits.
