VASP
====

``VASP`` can be loaded using the following command:

.. code-block:: console

    $ module load {MOD_VASP}

.. code-block:: bash
    :caption: example of a batch script using ``VASP`` can be found here using 120 CPU cores, 4750mb of RAM and for one hour.

    {SHEBANG}
    #SBATCH --job-name=VASP_cpu_example     # Job name
    #SBATCH --mail-type=BEGIN,END,FAIL      # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk   # where to send mail
    #SBATCH --nodes=3-18                    # Node range
    #SBATCH --spread-job                    # Evenly distribute cores
    #SBATCH --ntasks=120                    # Num mpi tasks
    #SBATCH --cpus-per-task=1               # Number of CPU cores per task
    #SBATCH --mem-per-cpu=4750mb            # Memory per core
    #SBATCH --time=01:00:00                 # Time limit hrs:min:sec
    #SBATCH --output=%x.o%j                 # Archer style screen output
    #SBATCH --error=%x.e%j                  # Archer style error output
    #SBATCH --account=dept-proj-year        # Project account to use

    # Abort if any command fails
    set -e

    module purge
    module load {MOD_VASP}
    ulimit -s unlimited

    mpirun -np 120 vasp_std


.. note::

     ``VASP`` can take advantage of a GPU
