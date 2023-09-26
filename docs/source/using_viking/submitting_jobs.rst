Submitting Jobs
===============

Selecting configuration options for jobs in ``Slurm`` can be quite complex and not easy to predict. There is an `in depth guide <https://slurm.schedmd.com/cpu_management.html>`_ about CPU management in the ``Slurm`` docs which is well worth the read.

.. epigraph::

    The interactions between different CPU management options are complex and often difficult to predict. Some experimentation may be required to discover the exact combination of options needed to produce a desired outcome.

    -- Slurm documentation


.. hint::

    For the vast majority of jobs the configuration for requesting multiple CPU cores is:

    .. code-block:: bash

        #SBATCH --nodes=1
        #SBATCH --ntasks=1
        #SBATCH --cpus-per-task=N

    This configuration describes 1 task on 1 node and ``N`` CPU cores, where you substitute ``N`` for how many cores you need e.g ``16``

For more examples of how to use ``--nodes``, ``--ntasks``, ``--ntasks-per-node`` and ``--cpus-per-task`` `CECI has a good answer <https://support.ceci-hpc.be/doc/_contents/SubmittingJobs/SlurmFAQ.html#q05-how-do-i-create-a-parallel-environment>`_ on their site which explains various ways to request 16 cores and the results.


.. attention::

    In summary, usually where ``N > 1``, ``--ntasks=N`` is for mpi and ``--cpus-per-task=N`` is for multithreading applications


Best Practice
-------------

Resource Requests
^^^^^^^^^^^^^^^^^

Whilst you should avoid allocating fewer resources than required for your job to complete, please try to avoid significantly over-allocating resources. In addition to allowing more efficient utilisation of the cluster if job requests are reasonable, smaller jobs are likely to be scheduled quicker, thus improving your personal queue time. The same is true for wall-time; the scheduler assumes that the full duration will be used by the job, and so cannot backfill effectively if jobs are requesting significantly longer wall-times than they actually use.


Job Arrays
^^^^^^^^^^

When submitting large volumes of jobs with identical resource requests, job arrays offer an efficient mechanism to manage these. However, if the individual jobs are very short duration (e.g. 5 minutes or less), it may be preferable to instead use a simple for-loop within a single batch job script, to reduce the overhead associated with each job.


Bash Shebang and 'set -e'
^^^^^^^^^^^^^^^^^^^^^^^^^

Consider using ``set -e`` after the ``#SBATCH`` section. This has the effect of aborting the job if **any** command within the batch script fails, instead of potentially continuing with an environment that is different to what is expected, or with erroneous data. Furthermore, it ensures that the job displays as ``FAILED`` when querying the status of jobs with ``sacct``. In future versions of Viking this can be done in one line with ``#!/usr/bin/env -S bash -e``.


Batch Jobs
----------

Viking can run lots of different jobs in many different ways, but for the most part you'll probably want to submit the job via a jobscript. A jobscript is just a text file with various options in it and then a list of commands to run, which makes up the job. This is then submitted to the job scheduler called `Slurm <https://slurm.schedmd.com/quickstart.html>`_ which manages all the jobs on Viking and does it's best to ensure they all run as fairly and efficiently as possible. This means you set up the jobscript, send it to ``Slurm`` with the ``sbatch`` command and you can leave Viking to work on the job when ``Slurm`` decides it's time. This is great because you don't have to sit and wait for your job to start!

Below is an example jobscript, let's save it as ``jobscript.job`` for this example:

.. code-block:: bash
    :caption: jobscript.job

    {SHEBANG}

    #SBATCH --job-name=my_job               # Job name
    #SBATCH --ntasks=10                     # Number of MPI tasks to request
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

    # Purge any previously loaded modules #
    module purge

    # Load modules #
    module load lang/Python/3.10.8-GCCcore-12.2.0

    # Commands to run #
    echo My working directory is: `pwd`
    echo Running job on host:
    echo -e '\t'`hostname` at `date`'\n'

    python -c 'print ("Hello, world!")'

    echo '\n'Job completed at `date`


It uses ``bash`` syntax and importantly has a set of ``sbatch`` specific options **before** the commands which need to be run. There are many options that can be added into a jobscript, far more than we can go into here and the `slurm documentation for sbatch <https://slurm.schedmd.com/sbatch.html>`_ is a great place to see them all. For more advanced and specialised jobscript examples please see the :doc:`jobscript for specific applications section </using_viking/jobscripts_program_specific>`.

Send this to the job scheduler ``Slurm`` with the ``sbatch`` command:

.. code-block:: console

    $ sbatch jobscript.job

It's as simple as that!


Interactive Jobs
----------------

Interactive jobs are typically used when testing code, or when running applications interactively (such as MATLAB, Python or other GUI applications). In general, it is advisable to use ``sbatch`` jobscripts unless interactive input is **required**, since these do no require any further user interaction beyond the initial submission to the scheduler. Requesting an interactive session is very similar to logging into a new shell as ourlined below:

    1. Request an allocation of resources (CPU cores, memory, time, etc.)
    2. This request is added to the queue for scheduling
    3. Once resources become available, you will be logged into the allocated compute node
    4. You can now run commands interactively
    5. On exit, the allocated resources are automatically released


.. note::

    There is a dedicated ``interactive`` :doc:`partition </using_viking/resource_partitions>` but it won't be used by default. The default partition is the ``nodes`` partition, therefore unless you need more resources, please explicitly request the ``interactive`` partition.


srun Command
^^^^^^^^^^^^

.. code-block:: console
    :caption: describes a job to run on: the interactive partition for 8 hours, and the program to run is ``/bin/bash``

    $ srun --time=08:00:00 --partition=interactive --pty /bin/bash

The same options available to ``sbatch`` are available to ``srun`` so please see the `slurm documentation <https://slurm.schedmd.com/sbatch.html>`_ for more options and in depth descriptions.

If you do need more processing power than the interactive partition offers, perhaps you're running ``MATLAB`` interactively, then you can request other partitions and resources, for example:


.. code-block:: console
    :caption: describes a job to run on: 1 node with 20 CPU cores on the ``nodes`` partition for 1 hour and the command to run is ``/bin/bash``

    $ srun --nodes=1 --cpus-per-task=20 --partition=nodes --time=0-01:00:00 --pty /bin/bash


After submitting the job, it will be added to the queue, and you should receive the following message:

.. code-block:: console

    $ srun: job 1234567 queued and waiting for resources

Once the resources have been allocated, you will then be placed onto the computational node allocated:

.. code-block:: console

    $ srun: job 1234567 has been allocated resources


You can now run programs interactively with the allocated resources. The job will end either when the time limit has been exceeded, or when the interactive bash shell has been closed (e.g. using ``exit``, or by disconnecting from Viking).

If you find that you have been disconnected from Viking whilst you have an interactive job running, you should be able to get back to it using the ``sattach`` command as follows:

.. code-block:: console

    $ sattach JOBID.0

where ``JOBID`` is the ID of your running interactive job, if you need to find this, try listing all your jobs with:

.. code-block:: console

    $ squeue -u $USER
