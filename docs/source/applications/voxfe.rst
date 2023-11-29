VOX-FE
======

``VOX-FE`` can be loaded using the following command:

.. code-block:: console

    $ module load module load {MOD_VOXFE}


An example job script can be found here. This script takes 40 CPUs, 1 GB of memory and 2 hours. Remember to update the account code and email address provided to ``slurm`` to your own details.

.. code-block:: bash

    {SHEBANG}
    #SBATCH --job-name=VOX-FE_CPU_example       # Job name
    #SBATCH --mail-type=BEGIN,END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk       # Where to send mail to
    #SBATCH --ntasks=40
    #SBATCH --cpus-per-task=1
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=40
    #SBATCH --ntasks-per-socket=20
    #SBATCH --mem-per-cpu=1gb
    #SBATCH --time=02:00:00
    #SBATCH --output=logs/VOX-FE_CPU_example-node-%j.log
    #SBATCH --account=dept-proj-year            # Project account to use

    # Abort if any command fails
    set -e

    module purge                                # purge any loaded modules
    module load module load {MOD_VOXFE}

    echo "Running small-vox-fe on $SLURM_NTASKS CPU cores"
    echo "Nodes allocated to job: " $SLURM_JOB_NUM_NODES "(" $SLURM_JOB_NODELIST ")"
    echo

    date
    mpirun -np $SLURM_NTASKS PARA_BMU Script.txt
    date

.. note::

    ``VOX-FE`` can not take advantage of a GPU, and runs purely on a CPU
