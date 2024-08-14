.. include:: /global.rst

Slurm job scheduler
===================

.. Note::

    This page should be considered an introduction to the Slurm job scheduler as Slurm has capabilities *far beyond* what we describe on this page. We would encourage everyone to look through the `Slurm documentation <https://slurm.schedmd.com/>`_ for more in depth information. The `Slurm Manual <https://slurm.schedmd.com/man_index.html>`_ pages can be especially good for a quick reference.


What is Slurm?
--------------

Slurm is a job scheduling system for small and large clusters. As a cluster workload manager, Slurm has three key functions:

1. Lets a user request a resources on a compute node to run their workloads
2. Provides a framework (commands) to start, cancel, and monitor a job
3. Keeps track of all jobs to ensure everyone can efficiently use all computing resources without stepping on each others toes.

When a user submits a job Slurm will decide when to allow the job to run on a compute node. This is very important for shared machines such as the Viking cluster so that the resources are shared fairly between users so one person's jobs do not dominate.

.. tip::

    The Slurm documentation has an in depth `overview <https://slurm.schedmd.com/overview.html>`_ with a drawing to help picture Slurm.

Resource allocation
-------------------

In order to interact with Slurm, the user must first give some indication of the resources they require. At a minimum these include:

- How long does the job need to run for
- On how many processors to run the job

The default resource allocation for jobs can be found on the :doc:`resource partitions <resource_partitions>` page.

Armed with this information, the scheduler is able to dispatch the jobs at some point in the future when the resources become available. A fair-share policy is in operation to guide the scheduler towards allocating resources fairly between users.


Running some Slurm commands on Viking
-------------------------------------

To interact with Slurm there are a number of command you can use. This table summarises the most common commands that can be used on Viking:

===========     ================================================================================================
Command         Description
===========     ================================================================================================
**squeue**      Reports the state of jobs (with filtering, sorting, and formatting options). By default |br|
                it reports the running jobs in priority order followed by the pending jobs in priority order
**srun**	    Used to submit a job for execution in real time
**salloc**      Allocate resources for a job in real time (typically used to allocate resources and |br|
                spawn a shell, in which the **srun** command is used to launch parallel tasks)
**sbatch**      Submit a job script for later execution (the script typically contains one or more |br|
                **srun** commands to launch parallel tasks)
**sattach**	    Attach standard input, output, and error to a currently running job , or job step
**scancel**	    Cancel a pending or running job
**sinfo**       Reports the state of partitions and nodes managed by Slurm (it has a variety of filtering, |br|
                sorting, and formatting options)
**sacct**	    Report job accounting information about active or completed jobs
===========     ================================================================================================


squeue
""""""

The **squeue** command will be a command you use often. To run the command first login to Viking.

.. code-block:: console

    $ squeue

You should see a list of jobs. Each column describes the status of each job:

=======================  ==========================================================================
Column                   Description
=======================  ==========================================================================
**JOBID**                A number used to uniquely identify your job within **Slurm**
**PARTITION**            The partition the job has been submitted to
**NAME**                 The job's name
**USER**                 The username of the job's owner
**ST**                   Current job status: **R** (running), **PD** (pending - queued and waiting)
**TIME**                 The time the job has been running
**NODES**                The number of nodes used by the job
**NODELIST (REASON)**    The nodes used by the job or reason the job is not running
=======================  ==========================================================================

To see only your jobs in the queue, run the following command

.. code-block:: console
    :caption: alternatively, replace ``$USER`` with any username

    $ squeue -u $USER

To provide information on the job you have queued or are running:

.. code-block:: console
    :caption: replace JOBID with a value job ID

    $ squeue -j JOBID

Other useful options you can use with **squeue** are summarised here:

=========== ==================================================
-a          Display all jobs
-l          Display more information
-u          Only display users jobs
-p          Only display jobs in a particular partition
--usage     Print help
-v          Verbose listing
=========== ==================================================

For a comprehensive look at **squeue** refer to the `manual page <https://slurm.schedmd.com/squeue.html>`_ or run ``man squeue`` on Viking.


sinfo
"""""

The **sinfo** command displays node and partition (queue) information and state.

=====================   =================================================================================
Column                  Description
=====================   =================================================================================
**PARTITION**           Asterisk after a partition name indicates the default partition
**AVAIL**               Partition is able to accept jobs
**TIMELIMIT**           Maximum time a job can run for
**NODES**               Number of available nodes in the partition
**STATE**               **Down** - not available, **alloc** - jobs being run, **idle** - waiting for jobs
**NODELIST**            Nodes available in the partition
=====================   =================================================================================

For a comprehensive look at **sinfo** refer to the `manual page <https://slurm.schedmd.com/sinfo.html>`_ or run ``man sinfo`` on Viking.


sacct
"""""

To display a list of *recently completed* jobs use the **sacct** command.

.. code-block:: console
    :caption: in this case looking at job ID: 147874

    $ sacct -j 147874
    JobID        JobName    Partition  Account    AllocCPUS  State      ExitCode
    ------------ ---------- ---------- ---------- ---------- ---------- --------
    147874       simple.job nodes      dept-proj+ 1          COMPLETED  0:0
    147874.batch batch                 dept-proj+ 1          COMPLETED  0:0

Important switches to **sacct** are:

==========  ==================================
Option      Action
==========  ==================================
-a          Display all users jobs
-b          Display a brief listing
-E          Select the jobs end date/time
-h          Print help
-j          Display a specific job
-l          Display long format
--name      Display jobs with name
-S          Select the jobs start date/time
-u          Display only this user
-v          Verbose listing
==========  ==================================

For a comprehensive look at **sacct** refer to the `manual page <https://slurm.schedmd.com/sacct.html>`_ or run ``man sacct`` on Viking.

.. note::

    There are many more commands you can use to query **Slurm**.  Please see the `Slurm documentation <https://slurm.schedmd.com/documentation.html>`_ for further details.
