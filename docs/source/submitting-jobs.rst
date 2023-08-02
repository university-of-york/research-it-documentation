Submitting Jobs
===============

Batch Jobs
----------

Viking can run lots of different jobs in many different ways, but for the most part you'll probably want to submit the job via a jobscript. A jobscript is just a text file with various options in it and then a list of commands to run, which makes up the job. This is then submitted to the job scheduler called `Slurm <https://slurm.schedmd.com/quickstart.html>`_ which manages all the jobs on Viking and does it's best to ensure they all run as fairly and efficiently as possible. This means you set up the jobscript, send it to ``Slurm`` with the ``sbatch`` command and you can leave Viking to work on the job when ``Slurm`` decides it's time. This is great because you don't have to sit and wait for your job to start!

Below is an example jobscript, let's save it as ``jobscript.job`` for this example:

.. code-block:: bash
    :caption: jobscript.job

    #!/usr/bin/env bash
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


It uses ``bash`` syntax and importantly has a set of ``sbatch`` specific options before the commands to be run. There are many options that can be added into a jobscript, far more than we can go into here but the `slurm documentation for sbatch <https://slurm.schedmd.com/sbatch.html>`_ is a great place to see them all. For more advanced and specialised jobscript examples please see the `advanced jobscript section <FIXME: Link>`_.


Interactive Jobs
----------------

Interactive jobs are typically used when testing code, or when running applications interactively (such as MATLAB, Python or other GUI applications). In general, it is advisable to use ``sbatch`` jobscripts unless interactive input is **required**, since these do no require any further user interaction beyond the initial submission to the scheduler. Requesting an interactive session is very similar to logging into a new shell as ourlined below:

    1. Request an allocation of resources (CPU cores, memory, time, etc.)
    2. This request is added to the queue for scheduling
    3. Once resources become available, you will be logged into the allocated compute node
    4. You can now run commands interactively
    5. On exit, the allocated resources are automatically released


srun Command
^^^^^^^^^^^^

.. code-block:: console
    :caption: describes a job to run on: 1 node, with up to 10 tasks, for 15 mins and the program to run is `/bin/bash`

    $ srun --nodes 1 --ntasks 10 --time 00-00:15:00 --pty /bin/bash

The same options available to ``sbatch`` are available to ``srun`` so please see the `slurm documentation <https://slurm.schedmd.com/sbatch.html>`_ for more options and in depth descriptions.

After submitting the job, it will be added to the queue, and you should receive the following message:

.. code-block:: console

    srun: job 1234567 queued and waiting for resources

Once the resources have been allocated, you will then be placed onto the computational node allocated:

.. code-block:: console

    srun: job 1234567 has been allocated resources
    $

You can now run programs interactively with the allocated resources. The job will end either when the time limit has been exceeded, or when the interactive bash shell has been closed (e.g. using `exit`, or by disconnecting from Viking).

If you find that you have been disconnected from Viking whilst you have an interactive job running, you should be able to get back to it using the ``sattach`` command as follows:

.. code-block:: console

    $ sattach JOBID.0

where ``JOBID`` is the ID of your running interactive job, if you need to find this, try listing all your jobs with:

.. code-block:: console

    $ squeue -u $USER
