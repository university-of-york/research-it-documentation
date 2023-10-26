.. include:: /global.rst

.. raw:: html

   <style>
   .wy-nav-content { max-width: 900px !important; }
   </style>

.. attention::

    The resource partitions are currently being configured and not all limits are currently set. This will change over the coming days and this page will be updated accordingly.


Resource partitions
====================

Viking's resources are divided up into various partitions as layed out below, these may change over time as it becomes clear how best to share Viking's resources.

.. tip::

    To select a partition you use the ``--partition=`` option in the jobscript, for example ``--partition=test``. The ``nodes`` partition the default and will be used if no other partition is specified.


.. csv-table:: Viking partition table
    :file: /assets/data/partition_table.csv
    :header-rows: 1


Additional partition information
--------------------------------

nodes
    Maximum limit of 960 cores.

week
    Partition for jobs that need to run for longer than the 48h max time allowed by the nodes partition, but for less than a week. The max running cores and max running memory limits are practical limits, due to the resources available on the nodes.

month
    Partition for jobs that need to run for longer than the 7 day max time allowed by the week partition, but for less than 30 days. The max running cores and max running memory limits are practical limits, due to the resources available on the nodes.

test
    For testing small jobs

preempt
    **Warning:** Jobs submitted to this partition are subject to preemption. There is no guarantee when or if a job will run, or whether it will complete. This partition has no limits on the resources that can be requested, but a lower priority than the nodes partition. Jobs will run if there are free resources in the nodes partition, but will be cancelled if these resources are later required for another higher priority job.

gpu
    Partition for running jobs that require GPUs, see documentation for details about how to request GPUs.
    - Your job script must request at least one GPU
    - You can use **no more than six GPUs** at a time across all of your jobs running in the GPU partition

gpuplus
    Partition for running jobs that require GPUs, see documentation for details about how to request GPUs.
    - Your job script must request at least one GPU
    - You can use **no more than two GPUs** at a time across all of your jobs running in the GPU partition

himem
    For running jobs that require memory greater than that available in other partitions. Each of the two nodes (himem01 and himem02) have 96 cores. The max running cores and max running memory limits are practical limits, due to the resources available on the nodes.

himem_week
    Partition for running jobs that require memory greater than that available in other partitions. The max running cores and max running memory limits are practical limits, due to the resources available on the nodes.

interactive
    Partition for jobs that would like to use Viking interactively.  This could be used for graphical work with the **eight hour queue limit** set to mimic a working day. You can run interactive jobs in the ``nodes`` partition (or any other), but the queue time will be shorter in the ``interactive`` partition.
