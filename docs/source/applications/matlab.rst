MATLAB
======

MATLAB can be used with Viking in several different ways. These include:

* Interactively without a GUI (MATLAB command line)
* Interactively with a GUI (full MATLAB GUI)
* Batch mode - submit jobs from your local MATLAB GUI
* Batch mode - submit jobs from the Viking terminal

The instructions for each of these methods are provided below.

Running interactively without a GUI
-----------------------------------

Once you have :doc:`connected to one of the login nodes via SSH <../getting_started/connecting_to_viking>`, the first step is to create an interactive session on the compute nodes. Please ensure that you don't run MATLAB on :doc:`Viking's login nodes <../getting_started/code_of_conduct>`.

To create an interactive session on a compute node for 30 minutes, with 4 cores and 8 GB of memory enter the following command in the terminal:

.. code-block:: console

    $ srun --ntasks=1 --cpus-per-task=4 --mem=8GB --time=00:30:00 --pty bash

Once the resources have been assinged, you need to load the MATLAB module, then start MATLAB without a GUI.

.. code-block:: console

    $ module load {MOD_MATLAB}
    $ matlab -nojvm -nodisplay -nosplash

MATLAB will show you the following information and you will be at the MATLAB command prompt. You can now use the MATLAB command line as normal.

.. code-block:: console

                            < M A T L A B (R) >
                  Copyright 1984-2023 The MathWorks, Inc.
                   R2023b (23.2.0.2391609) 64-bit (glnxa64)
                            September 22, 2023

    For online documentation, see http://www.mathworks.com/support
    For product information, visit www.mathworks.com.

    >>

To close MATLAB just type ``exit`` at the MATLAB prompt. To end the interactive session and release your resources to other users type ``exit`` again or ``Ctrl+D`` and you will be returned to a login node. Please note that once your requested time has expired the interactive session and MATLAB will end and any unsaved data will be lost.

Different resources can be assigned to the interactive session by changing the srun command options. This includes the :doc:`partition <../using_viking/resource_partitions>`. For example, to request a GPU compute node with one GPU use:

.. code-block:: console

    $ srun --partition=gpu --gres=gpu:1 --ntasks=1 --cpus-per-task=4 --mem=8GB --time=00:30:00 --pty bash

Running interactively with a GUI
--------------------------------

The :doc:`Virtual desktops <../using_viking/virtual_desktops>` page and specifically the section on :ref:`Compute nodes <virtual_session_compute_node>` explain how to run MATLAB in a virtual desktop on Viking. This gives you access to the normal MATLAB GUI and all of its graphical functionality.

Batch mode - submit jobs from your local MATLAB GUI
---------------------------------------------------

There are some prerequisites before you can use this method of interacting with Viking:

* An account on Viking - see XXX for information on how to get an account
* You must either be on campus or connected via the VPN for this method to work
* A version of MATLAB on your local computer which matches a version on Viking - currently ``2023a`` and ``2023b``
* MATLAB Parallel Computing Toolbox installed on your local MATLAB instance. This should be present by default on managed devices

.. Note::
    These instructions will be completed soon!


Batch mode - submit jobs from the Viking terminal
-------------------------------------------------

``MATLAB`` (2019a and newer) can also be run in batch mode, i.e non-interactively. This model of execution fits nicely with HPC systems like Viking, where work can be submitted to the scheduler to be executed.

The following job script could be used to submit a ``MATLAB`` script to the cluster, using 1 core and 4.8GB of memory for 2 hours. The following assumes that you have a ``MATLAB`` script ``matlab_batch_example.m`` either in the job's working directory, or in the ``MATLAB`` search path:

.. code-block:: bash
    :caption: example MATLAB batch mode script
    :linenos:

    {SHEBANG}
    #SBATCH --job-name=matlab_batch_example        # Job name
    #SBATCH --account=dept-proj-year               # Project account to use
    #SBATCH --partition=nodes                      # Partition for the job
    #SBATCH --ntasks=1                             # Run a single task
    #SBATCH --cpus-per-task=1                      # Number of cores per task
    #SBATCH --mem=4800MB                           # Job memory request
    #SBATCH --time=02:00:00                        # Time limit hrs:min:sec
    #SBATCH --output=%x.log                        # Standard output and error log
    #SBATCH --mail-type=ALL                        # Events to receive emails about
    #SBATCH --mail-user=a.user@york.ac.uk          # Where to send mail

    # Abort if any command fails
    set -e

    module purge
    module load {MOD_MATLAB}
    matlab -batch matlab_batch_example

.. note::
    **Do not** include the ``.m`` extension, which is part of the ``matlab_batch_example.m`` filename, in the job script when calling ``matlab -batch`` command, as shown.


Standalone MATLAB programs
--------------------------

It is possible to create standalone ``MATLAB`` programs from your ``MATLAB`` projects, and these can be run on Viking. An advantage of doing this is that when running a standalone program, ``MATLAB`` does not check out a licence from the licence server, which means somebody else who has to run ``MATLAB`` interactively will be able to do so even if your ``MATLAB`` program is running!

You can find documentation about how to create standalone ``MATLAB`` programs in the `MathWorks help pages <https://uk.mathworks.com/help/compiler/standalone-applications.html>`_, and we recommend using mcc, the ``MATLAB`` compiler, as a straightforward way to create standalone programs.

Certain ``MATLAB`` features are not available in standalone programs, so it is worth being aware of what these are to avoid trouble when running your program. You can find a list of `ineligible features <https://uk.mathworks.com/support/requirements/product-requirements-platform-availability-list.html>`_, and comprehensive documentation of `supported features <https://uk.mathworks.com/products/compiler/compiler_support.html?s_tid=srchtitle>`_.

.. code-block:: console
    :caption: start an interactive session and load the MATLAB module

    $ srun --ntasks=1 --time=00:30:00 --pty /bin/bash
    $ module load {MOD_MATLAB}

Your ``MATLAB`` code will need to be in the form of a function. The following example calculates an nxn magic square, where the user gives the input ``n``.

.. code-block:: matlab
    :caption: magicsquare.m

    function m = magicsquare(n)

    if ischar(n)
        n=str2double(n);
    end

    m = magic(n);
    disp(m)

To compile magicsquare.m the mcc command can be run in ``MATLAB`` itself or from the command line:

.. code-block:: matlabsession
    :caption: in MATLAB

    >> mcc -m magicsquare.m

.. code-block:: console
    :caption: on the command line

    $ mcc -m magicsquare.m

If you encounter the following error it is because the compiler has detected that you have a ``startup.m`` file in your ``MATLAB`` path and this may cause issues if you distribute your standalone program. This `MATLAB Answers post <https://uk.mathworks.com/matlabcentral/answers/362818-why-does-creating-a-standalone-application-generate-a-warning-regarding-startup-m-adding-paths>`_ provides more details.

.. error::

    Warning: Your deployed application may fail because file or folder paths
    not present in the deployed environment may be included in your MATLAB startup
    file. Use the MATLAB function "isdeployed" in your MATLAB startup file to
    determine the appropriate execution environment when including file and folder
    paths, and recompile your application.


Running standalone programs
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Standalone ``MATLAB`` programs require the ``MATLAB`` Compiler Runtime ``MCR`` to run. This requires the ``MATLAB`` module to be loaded either in your interactive session or in your job script. Make sure that the version you load is the same version that was used when you compiled the program.

.. code-block:: console

    $ module load {MOD_MATLAB}

When you run your standalone program, either in an interactive session or in a job script, you should use the bash script created during compilation to execute the program. The script has ``run_`` before the name of your source ``.m`` file. You must also use the environment variable ``$EBROOTMATLAB`` after the bash script name to specify where the MCR is and then give any arguments that are required (in this example the number 5 is passed to the program to generate a 5x5 magic square).

.. code-block:: console
    :caption: run a standalone program

    $ ./run_magicsquare.sh $EBROOTMATLAB 5

