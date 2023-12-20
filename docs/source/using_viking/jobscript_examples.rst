Jobscript examples
==================


In this section we'll try to give some general purpose examples of different jobscripts. Viking can run a vast array of programs to achieve results in many ways and so this page is really just the foundation to what is possible. Below we'll try and give some nice simple examples for some of the main types of job script which you can use and build upon yourself.


.. admonition:: We need your help!

    If you have a splendid jobscript, maybe it's super efficient, has a neat trick or maybe it does something not shown here. If that's the case then please send it to us so we can add it to this site and share it with everyone else. You never know, you may just make someone's day!


.. _jobscript_parallelisation:

Different types of parallelisation
----------------------------------

.. epigraph::

    The interactions between different CPU management options are complex and often difficult to predict. Some experimentation may be required to discover the exact combination of options needed to produce a desired outcome.

    -- Slurm documentation

There are several ``SBATCH`` options related to executing your program using a parallel execution model that all have similar sounding names, e.g.: ``--nodes``, ``--ntasks``, ``--cpus-per-task``, and ``--ntasks-per-node``.
Selecting configuration options for jobs in ``Slurm`` can be quite complex and not easy to predict. There is an `in depth guide <https://slurm.schedmd.com/cpu_management.html>`_ about CPU management in the ``Slurm`` docs which is well worth the read, and CECI has a `very informative FAQ <https://support.ceci-hpc.be/doc/_contents/SubmittingJobs/SlurmFAQ.html#q05-how-do-i-create-a-parallel-environment>`_ explaining the various ways to request 16 cores and the results.

For the purposes of simplicity, we'll group the types of parallel execution into 3:

  - Multi-threaded
  - Multi-processor (MPI)
  - Job arrays


Single process jobs
-------------------

For software that does not support any parallelisation, or where single threaded operation is desired, the following example job script can serve as a template.

.. code-block:: bash
    :linenos:

    {SHEBANG}
    #----------------------------- Slurm directives ------------------------------#
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=1G                        # Total memory to request
    #SBATCH --time=0-00:05:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --output=%x-%j.log              # Standard output log

    # Abort if any command fails
    set -e

    # purge any existing modules
    module purge

    # Load modules
    module load {MOD_PYTHON}

    # Commands to run
    python some_serial_script.py


.. _threaded-multi-process-jobs:

Multi-threaded
--------------

The following job script requests 8 cores on the same node, which could be used in a multi-threaded application.

.. code-block:: bash
    :linenos:

    {SHEBANG}
    #----------------------------- Slurm directives ------------------------------#
    #SBATCH --job-name=threaded_example     # Job name
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --nodes=1                       # Run on the same node
    #SBATCH --cpus-per-task=8               # Number of CPU cores per MPI task
    #SBATCH --mem=1G                        # Total memory to request
    #SBATCH --time=0-00:05:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --output=%x-%j.log              # Standard output log

    # Abort if any command fails
    set -e

    # purge any existing modules
    module purge

    # Load modules
    module load {MOD_R}

    # Commands to run
    Rscript --vanilla some_multithreaded_script.R


MPI
---

This job script requests 40 processes that could be split amongst different nodes, as might be desirable for an MPI application.

.. code-block:: bash
    :linenos:

    {SHEBANG}
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --ntasks=40                     # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=16G                       # Total memory to request
    #SBATCH --time=0-00:15:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --mail-type=END,FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk   # Where to send mail
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --error=%x-%j.err               # Standard error log

    # Abort if any command fails
    set -e

    # purge any existing modules
    module purge

    # Load modules
    module load {MOD_PYTHON}

    # Commands to run
    python some_mpi_script.py

.. _jobscript_job_arrays:

Job arrays
----------

Job arrays are efficient ways of running the same program multiple times.
They can be quicker to run than executing the program once and using MPI or multi-threaded for handling the multiple replicates.
This is because the job scheduler is much quicker at allocating resources to small jobs, even a large number of them, than one bigger job.

The example job script ``my_array.job`` below requests 100 jobs of the same R script, indicated by the ``--array`` option.
Submitting this file to Slurm has the same effect as running ``sbatch my_array.job`` 100 times if the ``--array`` option wasn't present.

Job arrays aren't restricted to running identical copies of a program either.
The ``$SLURM_ARRAY_TASK_ID`` environmental variable represents the array index, which can be passed into your program as an argument to allow for iteration-specific behaviour, e.g. using 100 different parameter settings, or 100 different input data files.

.. attention::

    You can only request a maximum of 10,000 iterations in a single array job submission; if you want more you'll need to submit the job multiple times.
    You also can't have an index of more than 10,000, so ``--array 9999-10001`` would fail because the final index is > 10,001, even though only 3 iterations are requested.

.. code-block:: bash
    :caption: my_array.job
    :linenos:

    {SHEBANG}
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=8G                        # Total memory to request
    #SBATCH --time=0-00:15:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --mail-type=END,FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk   # Where to send mail
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --error=%x-%j.err               # Standard error log
    #SBATCH --array=1-100                   # Array range

    # Abort if any command fails
    set -e

    # purge any existing modules
    module purge

    # Load modules
    module load {MOD_R}

    # Commands to run
    Rscript --vanilla some_job_array_script.R $SLURM_ARRAY_TASK_ID



GPU jobs
--------

Viking has three GPU :doc:`partitions </using_viking/resource_partitions>`, two with access to 48 nVidia A40 GPUs for either up to three days or a week, and another with access to twelve nVidia H100 GPUs for up to three days. Requesting access to a GPU requires you to select the corresponding partition and also request the number of GPUs, for example those lines in a job script looks like:

.. code-block:: bash

    #SBATCH --partition=gpu
    #SBATCH --gres=gpu:1

In this example we select the ``gpu`` :doc:`partition </using_viking/resource_partitions>` and with ``gres=gpu:1`` we describe how many resources you require **per node** - so in this case it's one gpu from the ``gpu`` partition, which is one A40 GPU overall.

If you wanted one of the H100s then the lines would be:

.. code-block:: bash

    #SBATCH --partition=gpuplus
    #SBATCH --gres=gpu:1

Read through the GPU limits for each of the GPU :doc:`partitions </using_viking/resource_partitions>` and understand how many GPUs are on each node. For example, if you wanted six A40 GPUs then you could request it over two nodes:

.. code-block:: bash

    #SBATCH --nodes=2
    #SBATCH --partition=gpu
    #SBATCH --gres=gpu:3

This is because each node in the ``gpu`` partition has only three GPUs, so if you need six, you must specify using two nodes with ``nodes=2``. The ``gres=gpu:3`` specifies three GPUs **per node**, which in total here is six.

Example jobscripts
""""""""""""""""""

Here are two example job scripts for the ``gpu`` partition and the ``gpuplus`` partition to use as a starting point. Firstly for the ``gpu`` partition with the nVidia A40s:

.. code-block:: bash
    :caption: my_gpu.job
    :linenos:

    {SHEBANG}
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --nodes=1                       # Number of nodes
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=8G                        # Total memory to request
    #SBATCH --time=0-00:15:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --mail-type=END,FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk   # Where to send mail
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --error=%x-%j.err               # Standard error log
    #SBATCH --partition=gpu                 # Which partition to use
    #SBATCH --gres=gpu:1                    # Generic resources required per node

    # Abort if any command fails
    set -e

    # purge any existing modules
    module purge

    # Commands to run
    nvidia-smi


And alternatively, the ``gpuplus`` partition with the nVidia H100s:

.. code-block:: bash
    :caption: my_gpuplus.job
    :linenos:

    {SHEBANG}
    #SBATCH --job-name=my_gpuplus_job       # Job name
    #SBATCH --nodes=1                       # Number of nodes
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=8G                        # Total memory to request
    #SBATCH --time=0-00:15:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --mail-type=END,FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk   # Where to send mail
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --error=%x-%j.err               # Standard error log
    #SBATCH --partition=gpuplus             # Which partition to use
    #SBATCH --gres=gpu:1                    # Generic resources required per node

    # Abort if any command fails
    set -e

    # purge any existing modules
    module purge

    # Commands to run
    nvidia-smi
