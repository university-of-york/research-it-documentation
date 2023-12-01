Relion
======

``RELION`` can be loaded using the following command:

.. code-block:: console

    $ module load {MOD_RELION}

An example script to run ``RELION`` can be seen here using

.. code-block:: bash

    {SHEBANG}
    #SBATCH --job-name=RELION_CPU_example          # Job name
    #SBATCH --mail-type=BEGIN,END,FAIL             # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk          # Where to send mail
    #SBATCH --account=dept-proj-year               # Project account to use
    #SBATCH --ntasks=1                             # Number of tasks to run
    #SBATCH --mem=4gb                              # Memory requested
    #SBATCH --time=00:30:00                        # Time requested

    # Abort if any command fails
    set -e

    module purge                    # Purges all loaded modules

    module load {MOD_RELION}

    echo
    echo Job started at `date`
    echo Job ID $SLURM_JOB_ID

    mpiexec -n XXXmpinodesXXX XXXcommandXXX

    echo
    echo Job completed at `date`
    echo Job ID $SLURM_JOB_ID

.. note::
    ``RELION`` can use GPUs, and is available on Viking's virtual desktop


Many thanks to Huw Jenkins who has suggested the following:

For RELION jobs submitted via GUI I would have at least:

.. code-block:: bash

    #SBATCH --ntasks=XXXmpinodesXXX
    #SBATCH --cpus-per-task=XXXthreadsXXX
    #SBATCH --open-mode=append
    #SBATCH --output=XXXoutfileXXX # Standard output log
    #SBATCH --error=XXXerrfileXXX # Standard error log

In the script to ensure:

1) the user can set the number of MPI tasks and threads for each MPI rank from the GUI
2) stdout/stderr go into the appropriate folders
3) 'continuing' a job doesn't wipe the logfile

I personally can't live without these extra ones that require modifying ``.bashrc``:

.. code-block:: bash

    #SBATCH --mem-per-cpu=XXXextra2XXX # Memory per thread
    #SBATCH --time=XXXextra1XXX # Time limit hrs:min:sec

with:

.. code-block:: bash

    export RELION_QSUB_EXTRA_COUNT=2
    export RELION_QSUB_EXTRA1="Total run time"
    export RELION_QSUB_EXTRA1_DEFAULT="01:00:00"
    export RELION_QSUB_EXTRA1_HELP="--time in qsub script"
    export RELION_QSUB_EXTRA2="Memory per thread (MB!)"
    export RELION_QSUB_EXTRA2_DEFAULT="4g"
    export RELION_QSUB_EXTRA2_HELP="--mem-per-cpu in qsub script"

in my ``.bashrc``.
