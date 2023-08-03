Code of Conduct
===============

.. caution::
    WIP: Needs suggestions

We hope everyone enjoys using Viking and all it's powerful resources. As all of Viking's resources are shared amongst the users, it's up to all of us to do our best to ensure we are using them wisely and not negatively impacting other users. We understand that for some people this may be the first time they have access to a HPC like Viking, or even the first time using a Linux machine, so we have created this page to help explain some of the concepts on how to use Viking so we don't impact other users. As always, if you need help with any explanation please get in touch with the team by emailing ITSupport@york.ac.uk.


Running Tasks on the Login Nodes
--------------------------------

When you first log in to Viking you, and every other user, will be logged into one of the ``login nodes``. These act as gateways to the ``compute nodes``, which is where all the hard work should be done. The login nodes are meant for transferring files, writing code, viewing results and other similar **light work**. If you have a task which crunches through a massisve data set, spinning off multiple instances and taking up as many CPUs as it can to get the job done, then running this task on a login node will impact other people.

Please run all tasks through the ``slurm`` job scheduler, this way they are run on the compute nodes, not the login nodes and you can control their resources. You can read about ``Slurm`` and how to send jobs to it on the `scheduling jobs page <FIXME: Link to page>`_.


Closing Virtual Desktop Sessions
--------------------------------

Frees up resources


Deleting Unneeded Files
-----------------------

Speeds up the filesystem





