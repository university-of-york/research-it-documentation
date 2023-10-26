.. include:: /global.rst

Jobscripts - program specific
=============================

This section of documentation goes over various programs installed on Viking which are more complicated than average to use.

All of the example files shown on these pages can be downloaded or can be found on Viking at

.. code-block:: console

    /mnt/lustre/groups/viking-examples/program_job_scripts

.. note::

    These scripts are generic and as such you will need to insert your specific details for them to function correctly.

.. tip::

    In each section there may be an example ``module load`` command. Newer versions may be available so please try the command ``module spider NAME`` where 'NAME' is the software to search for, and you will be presented with the currently available list.

AlphaFold
----------

`AlphaFold <https://deepmind.com/blog/article/putting-the-power-of-alphafold-into-the-worlds-hands>`_ is an AI system developed by `DeepMind <https://deepmind.com/>`_ that predicts a protein's 3D structure from its amino acid sequence. The source code for the inference pipeline can be found on the `AlphaFold GitHub <https://github.com/deepmind/alphafold>`_ page.


.. attention::

    Since a few tweaks have been made to the installation, it is important to read through the following documentation before running any jobs with ``AlphaFold``.

The CPU-only version of ``AlphaFold`` can be loaded using the following:

.. code-block:: console

    $ module load {MOD_ALPHAFOLD_CPU}

And the GPU version of ``AlphaFold`` can be loaded using the following command:

.. code-block:: console

    $ module load {MOD_ALPHAFOLD_GPU}


Example job scripts
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash
    :caption: using 16 CPUs, 80 GBs of memory and for up to 24 hours

    {SHEBANG}
    #SBATCH --job-name=AlphaFold_cpu_example        # Job name
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=16
    #SBATCH --mem=80G
    #SBATCH --time=24:00:00
    #SBATCH --output=%x-%j.log
    #SBATCH --mail-type=BEGIN,END,FAIL              # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk           # Where to send mail
    #SBATCH --account=dept-proj-year                # Project account to use

    # Abort if any command fails
    set -e

    module purge                                    # purge any loaded modules
    # Load AlphaFold module
    module load {MOD_ALPHAFOLD_CPU}

    # Path to genetic databases
    export ALPHAFOLD_DATA_DIR={ALPHAFOLD_DB_PATH}{APLHPFOLD_DB_DATE}

    # Optional: uncomment to change number of CPU cores to use for hhblits/jackhmmer
    # export ALPHAFOLD_HHBLITS_N_CPU=8
    # export ALPHAFOLD_JACKHMMER_N_CPU=8

    # Run AlphaFold
    alphafold --fasta_paths=T1050.fasta --max_template_date=2020-05-14 --preset=full_dbs --output_dir=$PWD --model_names=model_1,model_2,model_3,model_4,model_5

.. code-block:: bash
    :caption: using a GPU in addition to 10 CPUs for up to 4 hours

    {SHEBANG}
    #SBATCH --job-name=AlphaFold_GPU_example    # Job name
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=10
    #SBATCH --gres=gpu:1
    #SBATCH --partition=gpu
    #SBATCH --time=4:00:00
    #SBATCH --output=%x-%j.log
    #SBATCH --mail-type=BEGIN,END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk       # Where to send mail
    #SBATCH --account=dept-proj-year            # Project account to use

    # Abort if any command fails
    set -e

    module purge                                # purge any loaded modules
    # Load AlphaFold module
    module load {MOD_ALPHAFOLD_GPU}

    # Path to genetic databases
    export ALPHAFOLD_DATA_DIR={ALPHAFOLD_DB_PATH}{APLHPFOLD_DB_DATE}

    # Optional: uncomment to change number of CPU cores to use for hhblits/jackhmmer
    # export ALPHAFOLD_HHBLITS_N_CPU=8
    # export ALPHAFOLD_JACKHMMER_N_CPU=8

    # Run AlphaFold
    alphafold --fasta_paths=T1050.fasta --max_template_date=2020-05-14 --preset=full_dbs --output_dir=$PWD --model_names=model_1,model_2,model_3,model_4,model_5


Notes for using AlphaFold on viking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``AlphaFold`` currently requires access to various genetic databases such as ``UniRef90``, ``MGnify``, ``BFD``, ``Uniclust30``, ``PDB70`` and ``PDB``.

To avoid needless duplication of large databases across the cluster, these have been made available in a central directory:

.. code-block:: console

    {ALPHAFOLD_DB_PATH}{APLHPFOLD_DB_DATE}

The name of the subdirectory ``{APLHPFOLD_DB_DATE}`` indicates the date that the databases were downloaded. The files are hosted on the burst buffer (``/mnt/bb``) - a shared filesystem powered by fast SSDs - which is recommended for ``AlphaFold`` due to the random I/O access patterns. As seen below this can cause jobs to run up to **2x faster** than if the databases were stored on the disk-based lustre filesystem.

It is important to note that we have made a few enhancements to the installation to facilitate easier usage:

- The location to the AlphaFold data can be specified via the ``$ALPHAFOLD_DATA_DIR``  environment variable, so you should define this variable in your AlphaFold job script: ``export ALPHAFOLD_DATA_DIR=/mnt/bb/striped/alphafold-db/20210908``
- A symbolic link named ``alphafold`` , which points to the ``run_alphafold.py script`` , is included. This means you can just use ``alphafold``  instead of ``run_alphafold.py`` or ``python run_alphafold.py``.
- The ``run_alphafold.py``  script has been slightly modified such that defining ``$ALPHAFOLD_DATA_DIR``  is sufficient to pick up all the data provided in that location, meaning that you don't need to use options like ``--data_dir``  to specify the location of the data.
- Similarly, the ``run_alphafold.py``  script was tweaked such that the location to commands like ``hhblits``, ``hhsearch``, ``jackhmmer`` or ``kalign`` are already correctly set, and thus options like ``--hhblits_binary_path``  are not required.
- The Python script that are used to run ``hhblits``  and ``jackhmmer``  have been tweaked so you can control how many cores are used for these tools (rather than hard-coding this to 4 and 8 cores respectively).

  - If set, the ``$ALPHAFOLD_HHBLITS_N_CPU``  environment variable can be used to specify how many cores should be used for running ``hhblits``. The default of 4 cores will be used if ``$ALPHAFOLD_HHBLITS_N_CPU`` is not defined. The same applies for ``jackhmmer`` and ``$ALPHAFOLD_JACKHMMER_N_CPU`` .
  - Tweaking either of these may not be worth it however, since test jobs indicated that using more than 4/8 cores actually resulted in worse performance (although this may be workload dependent)


CPU vs GPU performance
^^^^^^^^^^^^^^^^^^^^^^

Shown below are the results of using the ``T1050.fasta`` example mentioned in the ``AlphaFold`` README with different resource allocations.

.. csv-table:: AlphaFold performance
    :file: /assets/data/alphafold_performance.csv
    :align: center
    :header-rows: 1

This highlights the importance of requesting resources when using ``AlphaFold``. These results suggest:

  - It is faster for almost all jobs to use the ``AlphaFold`` with the database stored on the burst buffer, ``/mnt/bb``
  - Using a GPU can considerably increase the speed at which a job completes (up to 6x)
  - Using a second GPU does not significantly reduce the runtime for a job
  - Counter intuitively, using more cores can lower performance



Amber
-----

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

AtChem 2
---------

``AtChem2`` is a modelling tool for atmospheric chemistry. It is primarily designed to use the `Master Chemical Mechanism (MCM) <https://mcm.york.ac.uk>`_, but it can be used with any general set of chemical reactions. The MCM is a near-explicit chemical mechanism which describes the gas-phase oxidation of volatile organic compounds (VOC) in the lower atmosphere. The latest stable version of AtChem2 can be downloaded from the `AtChem2 GitHub <https://github.com/AtChem/AtChem2/releases>`_.

This documentation will take you through getting a copy of the ``AtChem2`` source code, setting up the environment for ``AtChem2`` use, building a model, and submitting a model run to Viking's job scheduler, in batch mode.


Setting up the environment
^^^^^^^^^^^^^^^^^^^^^^^^^^

To work with ``AtChem2`` you will need to load the following modules on Viking:

.. code-block:: console
    :caption: a Fortran compiler

    $ module load {MOD_TOOLCHAIN_FOSS}


.. code-block:: console
    :caption: CMake, for building AtChem2 dependencies

    $ module load {MOD_CMAKE}


Next, clone a copy of the ``AtChem2`` source code:

.. code-block:: console

    $ git clone https://github.com/AtChem/AtChem2.git atchem2


Then create a directory to contain ``AtChem2``'s dependencies

.. code-block:: console

    $ mkdir atchem2_dependencies


Run the following files from the repository to install the dependencies for ``AtChem2``. These will automatically be installed into the directory you have made.

.. code-block:: console
    :caption: CVODE

    $ ./atchem2/tools/install/install_cvode.sh ./atchem2_dependencies $(command -v gfortran)


.. code-block:: console
    :caption: OpenLibm

    $ ./atchem2/tools/install/install_openlibm.sh ./atchem2_dependencies

Make a note of the full path to your ``AtChem2`` dependencies directory by copying the output of the following command, this will be used later to build a model.

.. code-block:: console

    $ realpath ./atchem2_dependencies

At this point, the environment is set up and you are ready to build an ``AtChem2`` model.


Gaussian
--------

``Gaussian`` can be loaded using the following:

.. code-block:: console

    $ module load {MOD_GAUSSIAN}

This job script can be used to submit a ``Gaussian`` workflow to the cluster, using 16GB of memory, 16 cores and 48 hours. This assumes you have a Gaussian file called ``g16.gjf`` . Remember to update the account code and email address provided to ``slurm`` to your own details.

.. code-block:: bash
    :linenos:

    {SHEBANG}
    #SBATCH --job-name=Gaussian_CPU_example    # Job Name
    #SBATCH --account=dept-proj-year           # Project account to use
    #SBATCH --mail-type= BEGIN, END, FAIL      # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk      # Where to send mail
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=16
    #SBATCH --mem=16gb
    #SBATCH --time=48:00:00
    #SBATCH --output=output.log
    #SBATCH --partition=nodes

    # Abort if any command fails
    set -e

    module purge                               # purge any loaded modules
    module load {MOD_GAUSSIAN}
    g16 g16.gjf

.. note::

    Gaussian can be run both with and without a GPU

As ``Gaussian`` is licensed software, you will need to be added to the Gaussian group on Viking in order to use it. If you find that you can't use ``Gaussian`` on Viking due to permission errors, please get in touch with Viking support via an email to itsupport@york.ac.uk.


MATLAB
------

``MATLAB`` can be loaded using the following command:

.. code-block:: console

    $ module load {MOD_MATLAB}


.. FIXME: New docs reference a jobscript emailed to Emma - can we get a copy?


Running interactively
^^^^^^^^^^^^^^^^^^^^^

``MATLAB`` can be run interactively both with and without a Graphical User Interface (GUI). When running ``MATLAB`` interactively, please ensure that you are doing so inside an :ref:`interactive cluster session <virtual_session_compute_node>`, rather than on :doc:`Viking's login nodes <../getting_started/code_of_conduct>`.

The following demonstrates how you could run ``MATLAB`` interactively without the GUI:

.. code-block:: console

    $ srun --ntasks=1 --mem-per-cpu=4800MB --time=00:30:00 --pty bash
    $ module load {MOD_MATLAB}
    $ matlab -nojvm -nodisplay -nosplash

                            < M A T L A B (R) >
                  Copyright 1984-2018 The MathWorks, Inc.
                   R2018a (9.4.0.813654) 64-bit (glnxa64)
                             February 23, 2018

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
^^^^^^^^^^^^^^^^^^^^^

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
    #SBATCH --time=00:02:00                        # Time limit hrs:min:sec
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
^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Certain ``MATLAB`` features are not available in standalone programs, so it is worth being aware of what these are to avoid trouble when running your program. You can find a list of ineligible features here, and comprehensive documentation of supported features `here <https://uk.mathworks.com/products/compiler/compiler_support.html?s_tid=srchtitle>`_.


Running standalone programs
"""""""""""""""""""""""""""

Standalone ``MATLAB`` programs require the ``MATLAB`` Compiler Runtime ``MCR`` to run. This requires the ``MATLAB`` module to be loaded either in your interactive session or in your job script. Make sure that the version you load is the same version that was used when you compiled the program.

.. code-block:: console

    $ module load {MOD_MATLAB}

When you run your standalone program, either in an interactive session or in a job script, you should use the bash script created during compilation to execute the program. The script has ``run_`` before the name of your source ``.m`` file. You must also use the environment variable ``$EBROOTMATLAB`` after the bash script name to specify where the MCR is and then give any arguments that are required (in this example the number 5 is passed to the program to generate a 5x5 magic square).

.. code-block:: console
    :caption: run a standalone program

    $ ./run_magicsquare.sh $EBROOTMATLAB 5


MongoDB
-------

``MongoDB`` can be loaded using the following command:

.. code-block:: console

    $ module load {MOD_MONGODB}

When using ``MongoDB``, you have to explicitly state the location of the database or ``mongod`` will error out as shown in the first option for ``mongod`` below. If you are using a unix socket you should also specify it's location, shown in the second option for ``mongod`` below.

.. code-block:: console

    $ mongod --dbpath $HOME/scratch/mongod/db --unixSocketPrefix $HOME/scratch/mongod


R
-

To see which ``R`` versions are available, use the following command. Note the trailing slash in the command, without this ``Ruby`` modules will also be included in the results.

.. code-block:: console

    $ module spider R/

One of these versions can then be loaded as following. Here we use ``{MOD_R}`` as an example

.. code-block:: console

    $ module load {MOD_R}

Submitting R jobs
^^^^^^^^^^^^^^^^^

The following Job Script will run an ``R`` script with no parallelisation, just in a single process. This is useful when you have a script that takes a long time to run and you don't want to tie up your personal computer with it, but the code has no parallelisable functionality.

.. code-block:: r
    :caption: Example Simple R Script - simple.R

    # Load data
    df <- read.csv("/path/to/data.csv")

    # Run long running model
    fit_model <- function(data) {
      # Fit model
      ...
    }
    mod <- fit_model(df)

    # Save results
    saveRDS(mod, "model.rds")


.. code-block:: bash
    :caption: Job Script to run simple.R

    {SHEBANG}
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=1G                        # Total memory to request
    #SBATCH --time=0-00:05:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --mail-type=BEGIN,END,FAIL      # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=my.name@york.ac.uk  # Where to send mail

    # Abort if any command fails
    set -e

    module purge
    module load {MOD_R}
    Rscript --vanilla simple.R


Multi-threaded applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your code does have the ability to use multiple cores, then use the :ref:`example multi-threaded job script <threaded-multi-process-jobs>` to request the correct number of cores, otherwise the job will run mulithreaded on the same core and being inefficient. Some libraries can also offer MPI support but that is less common.

Examples of ``R`` packages that support multi-core parallelisation are the Bayesian probabilist programming languages `Stan <https://mc-stan.org/>`_ and `INLA <https://www.r-inla.org>`_, or the machine learning library `caret <https://cran.r-project.org/web/packages/caret/index.html>`_.
You can also write your own parallel code through functions such as ``parallel::mclapply`` (forked processes, recommended on Viking) or ``parallel::makeCluster`` (socket cluster, compatible with Windows but could be slower than forked processes on Viking).
See the relevant chapter in `R Programming for Data Science <https://bookdown.org/rdpeng/rprogdatascience/parallel-computation.html>`_ for further guidance.

The following example shows how to run ``cmdstanr`` using 4 cores, one for each chain.

.. code-block:: r
    :caption: Example multithreaded R Script - multithreaded.R

    # Load library
    library(cmdstanr)

    # Load data
    df <- read.csv("/path/to/data.csv")

    # Compile stan model
    mod <- cmdstan_model("my_model.stan")

    # Fit the model
    fit <- mod$sample(
      data = list(x=df$x, y=df$y),
      chains=4,
      parallel_chains=4
    )

    # Save results
    saveRDS(fit, "model.rds")

.. code-block:: bash
    :caption: Job Script to run multithreaded.R

    {SHEBANG}
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=4               # Number of CPU cores per MPI task
    #SBATCH --mem=1G                        # Total memory to request
    #SBATCH --time=0-00:05:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --mail-type=BEGIN,END,FAIL      # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=my.name@york.ac.uk  # Where to send mail

    # Abort if any command fails
    set -e

    module purge
    module load {MOD_R}
    Rscript --vanilla multithreaded.R


.. note::

    The crucial step in the above job script is setting ``--cpus-per-task=4``, to ensure that you request the same number of cores that you are using in your ``R`` script to parallelise over.

.. attention::

    Always explicitly specify the number of cores in your ``R`` code when possible. This is because some ``R`` packages use ``parallel::detect_cores()`` to identify the number of cores on the system to parallelise over. However, this doesn't work on Viking as it returns the number of cores in total on the node, **not** the number of cores you have requested and can result in unexpected behaviour.


Array jobs
^^^^^^^^^^

Array jobs are extremely useful for running a large number of related programs where you would typically use a for loop, such as fitting 1,000 copies of a model with different parameters, running a stochastic model a large number of times for a sensitivity analysis, or fitting a model for a number of different subgroups in your data.

The example below shows the case of fitting a model that takes a single parameter 1,000 times, where the parameter is drawn from a standard normal distribution.
The Slurm environment variable, ``$SLURM_ARRAY_TASK_ID`` corresponds to the array iteration number and gets passed into the ``R`` script.
NB: if your ``R`` script also makes use of multi-core parallelisation then you can set ``--cpus-per-task`` in the job-script, e.g. if you are running multiple copies of a Stan model that itself uses multi-threading.

.. code-block:: r
    :caption: Example array job R Script - arrayjob.R

    # Read array iteration number from script arguments
    args <- commandArays(trailingOnly=TRUE)
    job <- as.integer(args[1])

    # Load data
    df <- read.csv("/path/to/data.csv")

    # Load parameters
    params <- rnorm(1000)

    # Fit model using this iteration's parameters
    fit_model <- function(param, data) {
      # Fit model
      ...
    }
    job_param <- params[job]
    mod <- fit_model(job_param, df)

    # Save results
    filename <- sprintf("model_%d.rds", job)
    saveRDS(mod, filename)


.. code-block:: bash
    :caption: Job Script to run arrayjob.R

    {SHEBANG}
    #SBATCH --job-name=my_job                # Job name
    #SBATCH --ntasks=1                       # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1                # Number of CPU cores per MPI task
    #SBATCH --mem=1G                         # Total memory to request
    #SBATCH --time=0-00:15:00                # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year         # Project account to use
    #SBATCH --mail-type=END,FAIL             # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk    # Where to send mail
    #SBATCH --output=%x-%j.log               # Standard output log
    #SBATCH --error=%x-%j.err                # Standard error log
    #SBATCH --array=1-1000                   # Array range
    #SBATCH --mail-type=BEGIN,END,FAIL       # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=my.name@york.ac.uk   # Where to send mail

    # Abort if any command fails
    set -e

    module purge
    module load {MOD_R}
    Rscript --vanilla jobarray.R $SLURM_ARRAY_TASK_ID


Converting a serial for loop to array job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While array jobs are a very effective way of running trivially parallelisable code on Viking, they require a bit of modification to scripts that you have been running on your personal computer. Take the parameter sweep example from above, this might have started out life as a for loop when running on your computer, as in the example below. This would work well until it takes too long to run, either from increasing the number of iterations or from the model fitting taking longer, until you want to run it on Viking to free up your PC.

.. code-block:: r
    :caption: Example parameter sweep R Script

    # Read array iteration number from script arguments
    args <- commandArays(trailingOnly=TRUE)

    # Load data
    df <- read.csv("/path/to/data.csv")

    # Load parameters
    params <- rnorm(1000)
    results <- list()
    fit_model <- function(param, data) {
      # Fit model
      ...
    }

    for (job in 1:1000) {
        # Fit model using this iteration's parameters
        job_param <- params[job]
        mod <- fit_model(job_param, df)
        results[[job]] <- mod
    }

    # Save results
    saveRDS(results, "models.rds")


Porting this script to an array job to run on Viking requires several steps:

  1. Add an argument to the script
  2. Remove the for loop and replace with the iteration number being passed in
  3. Create a Slurm batch script
  4. Write a script to collate the results from each iteration

A neat solution to manually undertaking each of these steps is using the ``batchtools`` package (available on `CRAN <https://cran.r-project.org/web/packages/batchtools/index.html>`_) to automate it.
This package takes as input:

  - A function that will be run at each iteration
  - The values to iterate over
  - A location to save a *registry*
  - A Slurm batch job template file (one provided below)

The registry is just a structured directory where ``batchtools`` saves its environment, which includes items such as the completed Slurm job script, serialised versions of the ``R`` code to run, and outputs from each iteration of the array.

The ``R`` script below shows how to use ``batchtools`` to convert the for-loop parameter sweep into an array job that runs on Viking.
This script will need to be moved onto Viking and run - it can't automatically submit from your PC (yet... watch this space).
If the preparation doesn't take much time or memory then it can be run from a login node, otherwise it should be run from a compute node.

.. code-block:: r
    :caption: Example R script using batch tools

    # Prepare batchtools registry and Slurm config
    reg <- makeRegistry(
        file.dir = "registry",  # This is where data related to this job will be saved
        make.default = FALSE,
        source=c(),             # Replace with paths to any files that are Sourced and needed by fit_model()
        packages=c()            # Replace with any libraries used by fit_model()
    )
    reg$cluster.functions <- makeClusterFunctionsSlurm(
        template="slurm_template.tmpl",
        array.jobs=TRUE  # Allow batchtools to create array jobs
    )

    # Load data
    df <- read.csv("/path/to/data.csv")

    # Load parameters
    params <- rnorm(1000)
    fit_model <- function(param, data) {
      # Fit model
      ...
    }

    # Create Slurm jobs
    jobs <- batchMap(
        fit_model,         # Function to call at each iteration
        param=1:1000,      # Arguments to iterate over
        more.args = list(  # Arguments that don't change per array
          data = df
        ),
        reg = reg)         # Registry to save results and job information to

    # Submit jobs, specifying resources
    submitJobs(
        jobs,
        reg=reg,
        resources=list(
          walltime=as.integer(10 * 60),  # walltime should be in seconds, so this is 10 mins
          memory="1GB",
          ncpus="1",                     # Can increase if fit_model() uses multithreading
          modules="{MOD_R}",
          job.name="my_job",
          log.file="%x-%j.log",
          account="dept-proj-year",
          email_address="my.name@york.ac.uk"
        )
    )

The Slurm template that this references is shown below and should be general enough to be used in most situations, feel free to adapt it to meet your needs.

.. code-block:: bash
    :caption: Example batchtools template - slurm_template.tmpl

    #!/usr/bin/env bash

    ## Slurm template for using batchtools on Viking at the University of York
    ## Modified from https://github.com/mllg/batchtools/blob/master/inst/templates/slurm-lido3.tmpl
    ## Author: Stuart Lacy
    ## Date: 2023-07-13

    ## Job Resource Interface Definition
    ##
    ## ncpus [integer(1)]:        Number of required cpus per task,
    ##                            Set larger than 1 if you want to further parallelise
    ##                            with multicore/parallel within each task.
    ## walltime [integer(1)]:     Walltime for this job, in seconds.
    ##                            Must be at least 1 minute.
    ## memory   [integer(1)]:     Memory in megabytes for each cpu.
    ##                            Must be at least 100 (when I tried lower values my
    ##                            jobs did not start at all).
    ##
    ## Default resources can be set in your .batchtools.conf.R by defining the variable
    ## 'default.resources' as a named list.

    <%

    # resources
    walltime = asInt(resources$walltime, lower = 60L, upper = 31L * 24L * 60L * 60L)
    memory = asInt(resources$memory, lower = 100L, upper = 1024L * 1024L)
    ncpus = if (!is.null(resources$ncpus)) ncpus = assertInt(resources$ncpus, lower = 1L) else 1L

    # modules
    modules = paste(resources$modules, resources$R)

    # user
    account = resources$account
    email_address = resources$email_address

    # cli args
    cli.args = ""
    if (!is.null(resources$pp.size))
        cli.args = sprintf("--max-ppsize=%i", assertInt(pp.size, upper = 500000L))
    -%>

    #SBATCH --mail-type=BEGIN,END,FAIl
    #SBATCH --job-name=<%= job.name %>
    #SBATCH --output=<%= log.file %>
    #SBATCH --error=<%= log.file %>
    #SBATCH --time=<%= ceiling(walltime / 60L) %>
    #SBATCH --cpus-per-task=<%= ncpus %>
    #SBATCH --ntasks=1
    #SBATCH --mem-per-cpu=<%= memory %>
    #SBATCH --account=<%= account %>
    #SBATCH --mail-user=<%= email_address %>
    <%= if (array.jobs) sprintf("#SBATCH --array=1-%i", nrow(jobs)) else "" %>

    ## Initialise work environment like
    module add <%= modules %>

    ## Export value of DEBUGME environemnt var to slave
    export DEBUGME=<%= Sys.getenv("DEBUGME") %>

    ## Use scratch on the node, TMPDIR is mounted as tmpfs
    export TMPDIR=/mnt/lustre/users/${USER}/slurm/<%= job.name %>/${SLURM_JOBID}
    mkdir -p ${TMPDIR}

    ## Run R:
    ## we merge R output with stdout from SLURM, which gets then logged via --output option
    Rscript <%= cli.args -%> -e 'batchtools::doJobCollection("<%= uri %>")'

Another advantage of the registry that is that it makes it easy to monitor your jobs, for example checking how many are still running, how many errored, resubmitting those that errored and so on.
An additional benefit is that the output from each job is automatically saved to the registry (note that we didn't manually call ``saveRDS()`` unlike for the manual ``arrayjob.R`` version).
You can then easily load the results and collate them into a single data structure, as shown below.
Again, if you aren't doing anything complex during this phase you can run this from a login node.

.. code-block:: r
    :caption: Example R script to collate results from a registry

    library(batchtools)

    # Load registry
    reg <- loadRegistry(file.dir="registry")
    # Load the saved results within the registry
    results <- lapply(1:1000, loadResult, reg)


Relion
-------

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

VASP
----

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




VOX-FE
------

``VOX-FE`` can be loaded using the following command:

.. code-block:: console

    $ module load module load bio/VOX-FE/2.0.1-foss-2017b


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


