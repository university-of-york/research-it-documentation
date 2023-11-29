MATLAB
======

``MATLAB`` can be loaded using the following command:

.. code-block:: console

    $ module load {MOD_MATLAB}


Running interactively
---------------------

``MATLAB`` can be run interactively both with and without a Graphical User Interface (GUI). When running ``MATLAB`` interactively, please ensure that you are doing so inside an :ref:`interactive cluster session <virtual_session_compute_node>`, rather than on :doc:`Viking's login nodes <../getting_started/code_of_conduct>`.

The following demonstrates how you could run ``MATLAB`` interactively without the GUI:

.. code-block:: console

    $ srun --ntasks=1 --mem-per-cpu=4800MB --time=00:30:00 --pty bash
    $ module load {MOD_MATLAB}
    $ matlab -nojvm -nodisplay -nosplash

                            < M A T L A B (R) >
                  Copyright 1984-2023 The MathWorks, Inc.
                   R2023b (23.2.0.2391609) 64-bit (glnxa64)
                            September 22, 2023

    For online documentation, see http://www.mathworks.com/support
    For product information, visit www.mathworks.com.

To run ``MATLAB`` interactively with the graphical user interface, you must first set up a :ref:`virtual desktop session on a compute mode <virtual_session_compute_node>`. Ensure that you use the command ``start-interactive-session.sh`` to set up your interactive job, rather than ``srun``. Note that these commands take the same parameters.

.. code-block:: console
    :caption: using ``start-interactive-session.sh`` as opposed to ``srun`` for the interactive session

    $ start-interactive-session.sh --ntasks=1 --mem-per-cpu=4800MB --time=00:30:00 --pty bash
    $ module load {MOD_MATLAB}
    $ matlab

In your virtual desktop session, you should now see the ``MATLAB`` graphical interface which is running on a compute node.


Running in batch mode
---------------------

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

