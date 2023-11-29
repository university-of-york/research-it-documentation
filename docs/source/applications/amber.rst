Amber
=====

There are two installations of ``Amber``, one which only supports running on CPUs, and one which supports running on GPUs (using CUDA). Use the module command to load the required version (note that you can not use both at the same time):

.. code-block:: console
    :caption: load the desired Amber module

    $ module load {MOD_AMBER_CPU}
    $ module load {MOD_AMBER_GPU}

The following job script could be used to submit an ``Amber`` workflow to the cluster, using 1 core and 4.8GB of memory for 2 hours. The following assumes that you have defined in the script ``amber_cpu_example.sh`` an ``Amber`` workflow, e.g. `minimisation and molecular dynamics <https://ambermd.org/tutorials/basic/tutorial1/section4.php>`_:

.. code-block:: bash
    :linenos:
    :caption: Example **CPU** Amber Script

    {SHEBANG}
    #SBATCH --job-name=amber_cpu_example           # Job name
    #SBATCH --account=dept-proj-year               # Project account to use
    #SBATCH --partition=nodes                      # Partition for the job
    #SBATCH --ntasks=1                             # Run a single task
    #SBATCH --cpus-per-task=1                      # Number of cores per task
    #SBATCH --mem=4800MB                           # Job memory request
    #SBATCH --time=00:02:00                        # Time limit hrs:min:sec
    #SBATCH --output=%x.log                        # Standard output and error log
    #SBATCH --mail-type=ALL                        # Events to receive emails about
    #SBATCH --mail-user=a.user@york.ac.uk          # Where to send mail

    # Abort if any command fails
    set -e

    module purge
    module load {MOD_AMBER_CPU}
    ./amber_cpu_example.sh

The following job script could be used to submit an ``Amber`` workflow to the GPU partition in the cluster, using 1 core, 4.8GB of memory, and 1 GPU for 2 hours. The following assumes that you have defined in the script ``amber_gpu_example.sh`` an ``Amber`` workflow which makes use of GPUs:

.. code-block:: bash
    :linenos:
    :caption: Example **GPU** Amber Script

    {SHEBANG}
    #SBATCH --job-name=amber_gpu_example           # Job name
    #SBATCH --account=dept-proj-year               # Project account to use
    #SBATCH --partition=gpu                        # Partition for the job ('gpu' for the GPU partition)
    #SBATCH --ntasks=1                             # Run a single task
    #SBATCH --cpus-per-task=1                      # Number of cores per task
    #SBATCH --mem=4800MB                           # Job memory request
    #SBATCH --gres=gpu:1                           # Select 1 GPU
    #SBATCH --time=02:00:00                        # Time limit hrs:min:sec
    #SBATCH --output=%x.log                        # Standard output and error log
    #SBATCH --mail-type=END,FAIL                   # Events to receive emails about
    #SBATCH --mail-user=a.user@york.ac.uk          # Where to send mail

    # Abort if any command fails
    set -e

    module purge
    module load {MOD_AMBER_GPU}
    ./amber_gpu_example.sh


.. FIXME: Add in benchmarks like old docs
