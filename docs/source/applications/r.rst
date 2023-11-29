R
=

To see which ``R`` versions are available, use the following command. Notice that we're using the ``-r`` option to allow us to use a ``Regular Expression`` (or ``RegEx``) in the search. This helps cut down on the returned results. Try ``module spider R/`` and see the difference.

.. code-block:: console

    $ module -r spider '^R/'


One of these versions can then be loaded as following. Here we use ``{MOD_R}`` as an example

.. code-block:: console

    $ module load {MOD_R}

Submitting R jobs
-----------------

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
---------------------------

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
----------

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
-----------------------------------------

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
