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
