.. include:: global.rst

.. raw:: html

   <style>
   .wy-nav-content { max-width: 900px !important; }
   </style>

.. attention::

    THIS IS THE OLD PARTITION TABLE


Available Partitions
====================

Viking's resources are divided up into various partitions as layed out below, these may change over time as it becomes clear how best to share Viking's resources.

.. tip::

    To select a partition you use the ``--partition=`` option in the jobscript, for example ``--partition=test``. The ``nodes`` partition the default and will be used if no other partition is specified.


.. csv-table:: Viking partition table
    :file: data/partition_table.csv
    :header-rows: 1


Additional Partition Information
--------------------------------

nodes
    Practical job limit of 500 running jobs, assuming 1 core per job. There is also a total limit of 2.4TB

test
    For testing small jobs

preempt
    **Warning:** Jobs submitted to this partition are subject to preemption. There is no guarantee when or if a job will run, or whether it will complete. This partition has no limits on the resources that can be requested, but a lower priority than the nodes partition. Jobs will run if there are free resources in the nodes partition, but will be cancelled if these resources are later required for another higher priority job.

himem
    For running jobs that require memory greater than that available in other partitions. Three nodes (himem02, himem04 and himem05) have 64 cores, one node (himem01) has 96 cores. The max running cores and max running memory limits are practical limits, due to the resources available on the nodes.

himem_week
    Partition for running jobs that require memory greater than that available in other partitions. The max running cores and max running memory limits are practical limits, due to the resources available on the nodes.

gpu
    Partition for running jobs that require GPUs, see documentation for details about how to request GPUs.
    There are 4 GPUs and 40 cores on each GPU node, subject to the following rules:

    - Your job script must request at least one GPU
    - You can request a maximum of 10 cores per GPU
    - You can use no more than 2 GPUs at a time across all of your jobs running in the GPU partition

week
    Partition for jobs that need to run for longer than the 48h max time allowed by the nodes partition, but for less than a week. The max running cores and max running memory limits are practical limits, due to the resources available on the nodes.

month
    Partition for jobs that need to run for longer than the 7 day max time allowed by the week partition, but for less than 30 days. The max running cores and max running memory limits are practical limits, due to the resources available on the nodes.

interactive
    Partition for jobs that would like to use Viking interactively.  This could be used for graphical work with the 8 hr queue limit set to mimic a working day.
