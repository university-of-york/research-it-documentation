X11 Forwarding
==============

X11 Forwarding is used to *forward* an *X11* type window from Viking, to your local computer. This is useful for running graphical programs, or GUIs, on Viking but having them display on your local machine. For most Linux distros this should work out of the box, for Mac OSX 10.8 and up, you'll need to install `XQuartz <https://www.xquartz.org/>`_.

.. For Windows `Xming <https://sourceforge.net/projects/xming/>`_ will need to be installed.

By default when you log into Viking you'll be logged into one of the two login nodes. As mentioned in the :doc:`/getting_started/code_of_conduct` page, we don't want to run big jobs on the login nodes as they are shared with other users whom it may affect.

Instead we'll access a compute node and then run the program on the compute node. This page will explain how we use X11 Forwarding to display the window on your local machine, whilst it's running on a compute node on Viking, behind the login node.

There are other ways to accomplish similar results so please treat this as a basic guide you can build upon.


Log into Viking
---------------

Use the ``-X`` option when we log into Viking over ``ssh``, this enables the ``X11 Forwarding`` from the login node to our local computer:

.. code-block:: console

    ssh -X viking.york.ac.uk


Request resources
-----------------

Once we're logged into Viking, we will request some resources on a compute node. Below we use the `salloc <https://slurm.schedmd.com/salloc.html>`_ command and use the same options as you would if you used the `srun <https://slurm.schedmd.com/srun.html>`_ command or the options from an jobscript when you use the `sbatch <https://slurm.schedmd.com/sbatch.html>`_ command. Once allocated we ``ssh`` into the node using the ``$SLURM_NODELIST`` environment variable which is set by ``Slurm`` to the node where our resources are allocated. Ensure you use the ``-X`` option again here, this will enable the ``X11 Forwarding`` from the compute node to the login node:

.. code-block:: console
    :caption: this describes one node, one task and eight CPU cores for two hours

    $ salloc --nodes=1 --ntasks=1 --cpus-per-task=8 --time=02:00:00
    $ ssh -X $SLURM_NODELIST

This means we now have ``X11 Forwarding`` from the compute node to the login node and also from the login node to our local computer.


Run your program
----------------

Once you're logged into the compute node, you can now load the modules and run your graphical program. In this example we run MATLAB:

.. code-block:: console

    $ module load MATLAB/2023b
    $ matlab

After a few moments, the window for MATLAB should appear on your local machine.


Tidy up
-------

Press ``Ctrl + d`` **twice** to exit the compute node. First to exit the ``ssh`` connection to the compute node and the second time to relinquish the resources from the ``salloc`` command earlier.
