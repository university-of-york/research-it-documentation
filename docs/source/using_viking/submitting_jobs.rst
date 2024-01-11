Submitting jobs
===============

Batch jobs
----------

Viking can run lots of different jobs in many different ways, but for the most part you'll probably want to submit the job via a **jobscript**.
A jobscript is just a text file with various options in it and then a list of the commands to run your desired program.
This is then submitted to the job scheduler called `Slurm <https://slurm.schedmd.com/quickstart.html>`_ which manages all the jobs on Viking and does its best to ensure they all run as fairly and efficiently as possible.

A typical workflow involves preparing the jobscript for your needs and submitting the job to ``Slurm`` when ready via the ``sbatch`` command.
However, this doesn't mean your program will start executing straight away!
Instead, ``Slurm`` will add it to a queue containing all jobs submitted by all users, and will start running it when there is availability based on the resources you requested.
This is great because you don't have to sit and wait for your job to start!

Below is an example jobscript to run a Python script, let's save it as ``jobscript.job``.

.. code-block:: bash
    :caption: jobscript.job

    {SHEBANG}
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --partition=nodes               # What partition the job should run on
    #SBATCH --time=0-00:15:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=2G                        # Total memory to request
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --mail-type=END,FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk   # Where to send mail
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --error=%x-%j.err               # Standard error log

    # Abort if any command fails
    set -e

    # Purge any previously loaded modules
    module purge

    # Load modules
    module load {MOD_PYTHON}

    # Commands to run
    python my_script.py


.. attention::

    Please ensure your project account code is specified through the ``--account`` option so that we can associate your work with your project. Your job won't run without it.

It uses ``bash`` syntax and importantly has a set of ``SBATCH`` specific options **before** the commands which need to be run.
Here is a quick summary of the most important ``SBATCH`` options as these determine the computational resources you are requesting, which will impact both on your queueing time (if you request more resources you will experience longer waits), but also on your job performance, however, there are far more possible options than we can go into here.
The `Slurm documentation <https://slurm.schedmd.com/sbatch.html>`_ is a great place to see them all, and please refer to the :doc:`Specific application guides </applications/index>` section for some specialised jobscript examples.

    - ``--partition``: The compute nodes on Viking are grouped into different *partitions* based on different use cases. For most general computing the ``nodes`` partition will be sufficient. See the :doc:`Resource Partition page </using_viking/resource_partitions>` for more details
    - ``--time``: How long your job will take to run; if your job exceeds this time it will be killed. It can be omitted in which case the default time is 8 hours. Specifying a shorter and more accurate time will allow your job to start execution sooner. In the format ``DD-HH:MM:SS``
    - ``--mem``: How much memory your job requires in the format ``<amount><unit>``, e.g. ``--mem=16GB``. As with time you want to request sufficient memory for your job to run successfully, but not too much that your job spends a long waiting in the queue for this amount of memory to become available. If you are using multi-core jobs (see :ref:`Job Script Examples <jobscript_parallelisation>`) you might want to specify memory per core instead, with ``--mem-per-cpu``
    - ``--ntasks``: The number of MPI tasks. If you don't know what MPI is then you likely want to keep this at 1.
    - ``--cpus-per-task``: Number of CPU cores to request. Increase this if you are using multi-core parallelisation (see :ref:`Job Script Examples <jobscript_parallelisation>`)

Send this to the job scheduler with the ``sbatch`` command, it's as simple as that!
If you filled out the ``--mail-user`` option you will get an email when the job either completes or fails.

.. code-block:: console

    $ sbatch jobscript.job

.. hint::

    This command must be run from the same folder that the Python file ``my_script.py`` is located in, or more generally filepaths should be relative to the directory where ``sbatch`` is run from.


Tips and best practices
-----------------------

Resource requests
^^^^^^^^^^^^^^^^^

Whilst you must avoid allocating fewer resources than required for your job to complete, please try to avoid significantly over-allocating resources. In addition to allowing more efficient utilisation of the cluster if job requests are reasonable, smaller jobs are likely to be scheduled quicker, thus improving your personal queue time. The same is true for wall-time; the scheduler assumes that the full duration will be used by the job, and so cannot backfill effectively if jobs are requesting significantly longer wall-times than they actually use.


Job arrays
^^^^^^^^^^

When submitting large volumes of jobs with identical resource requests, job arrays offer an efficient mechanism to manage these.
See the :ref:`Job Arrays section <jobscript_job_arrays>`  or the `official Slurm documentation <https://slurm.schedmd.com/job_array.html>`_ for further details.


Bash shebang and 'set -e'
^^^^^^^^^^^^^^^^^^^^^^^^^

Consider using ``set -e`` after the ``#SBATCH`` section. This has the effect of aborting the job if **any** command within the batch script fails, instead of potentially continuing with an environment that is different to what is expected, or with erroneous data. Furthermore, it ensures that the job displays as ``FAILED`` when querying the status of jobs with ``sacct``. In future versions of Viking this can be done in one line with ``#!/usr/bin/env -S bash -e``.  This is the `shebang <https://en.wikipedia.org/wiki/Shebang_(Unix)>`_ we were referencing in the title.

Redirecting output
^^^^^^^^^^^^^^^^^^

The %j in the ``#SBATCH --output`` line tells ``Slurm`` to substitute the ``job ID`` in the name of the output file. You can also add a ``#SBATCH --error`` with an error file name to separate output and error logs.

Filename patterns
^^^^^^^^^^^^^^^^^

There are several useful placeholders similar to ``%j`` that can be used in filenames which will be automatically filled in by ``Slurm``. The full list of these can be found in the ``sbatch`` man page, under the ``filename pattern`` heading or in the `online documentation <https://slurm.schedmd.com/sbatch.html#lbAH>`_.

.. _interactive-jobs:

Interactive jobs
----------------

If you would like to have a terminal session on a high powered compute node, for example to do interactive data analysis in programs like R, Python or MATLAB, or to run GUI applications, then you need an **interactive job**.
These are different to the batch jobs described above and are requested slightly differently, although as with batch jobs you still need to specify the resources you need and wait for these to become available.

The workflow is:

    1. Request an allocation of resources (CPU cores, memory, time, etc.) through the ``srun`` command
    2. This request is added to the queue for scheduling
    3. Once resources become available, you will be logged into the allocated compute node
    4. You can now run commands interactively
    5. On exit, the allocated resources are automatically released


Srun command
^^^^^^^^^^^^

Running the command below will request a Bash shell on a compute node in the interactive partition for 8 hours.
The same options available to ``sbatch`` are available to ``srun`` so please see the `Slurm documentation <https://slurm.schedmd.com/sbatch.html>`_ for more options and in depth descriptions.

.. code-block:: console
    :caption: describes a job to run on: the interactive partition for 8 hours, and the program to run is ``/bin/bash``

    $ srun --time=08:00:00 --partition=interactive --pty /bin/bash

After submitting the job, it will be added to the queue, and you should receive the following message:

.. code-block:: console

    $ srun: job 1234567 queued and waiting for resources

Once the resources have been allocated, you will then be placed onto the computational node allocated:

.. code-block:: console

    $ srun: job 1234567 has been allocated resources


You now have an interactive shell on a compute node and can run your programs as required (not forgetting to ``module load`` them first!).
The job will end either when the time limit has been exceeded, or when the interactive bash shell has been closed (e.g. using ``exit``, or by disconnecting from Viking).

If you find that you have been disconnected from Viking whilst you have an interactive job running, you should be able to get back to it using the ``sattach`` command as follows:

.. code-block:: console

    $ sattach JOBID.0

where ``JOBID`` is the ID of your running interactive job, if you need to find this, try listing all your jobs with:

.. code-block:: console

    $ squeue -u $USER

Interactive partition
^^^^^^^^^^^^^^^^^^^^^

Interactive jobs aren't restricted to running on the ``interactive`` :doc:`partition </using_viking/resource_partitions>`, and interactive jobs do not default to this partition.
However, for most use cases you will want to explicitly specify to use this partition through the ``--partition=interactive`` option to ``srun``, as this partition will have much shorter queueing times (in most cases near-instant) owing to its lower resources.

If you do need more processing power than the interactive partition offers, perhaps you're running a multi-core ``MATLAB`` program interactively, then you can request other partitions and resources, for example:

.. code-block:: console
    :caption: describes a job to run on: 1 node with 20 CPU cores on the ``nodes`` partition for 1 hour and the command to run is ``/bin/bash``

    $ srun --nodes=1 --cpus-per-task=20 --partition=nodes --time=0-01:00:00 --pty /bin/bash

