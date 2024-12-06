.. include:: /global.rst

.. raw:: html

   <style>
   .wy-nav-content { max-width: 900px !important; }
   </style>

.. attention::

    The resource partitions will likely change over time and this page will be updated accordingly.


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
    - Each node has 96 cores.
    - Maximum limit of 960 cores per user.

week
    Partition for jobs that need to run for longer than the 48h max time allowed by the nodes partition, but for less than a week. There are 12 nodes in this partition and each user is limited to using a maximum of six node's CPU and memory (576 cores and 3T of RAM).

month
    Partition for jobs that need to run for longer than the 7 day max time allowed by the week partition, but for less than 30 days. The max running cores and max running memory limits are practical limits, due to the resources available on the two nodes.

test
    For testing jobs to ensure they run as expected.

preempt
    **Warning:** Jobs submitted to this partition are subject to preemption. There is no guarantee when or if a job will run, or whether it will complete. This partition has no limits on the resources that can be requested, but a lower priority than the nodes partition. Jobs will run if there are free resources in the nodes partition, but will be cancelled if these resources are later required for another higher priority job.

gpu
    Partition for running jobs that require GPUs, see documentation for details about how to :ref:`request GPUs <gpu-jobs>`.

    - Each of the 16 nodes house three **nVidia A40 GPUs**
    - Your job script must request at least one GPU (eg ``#SBATCH --gres=gpu:1``)
    - You are limited to **no more than six GPUs** at a time across all of your jobs running in the ``gpu`` partition
    - Each GPU is limited to a maximum of 32 CPU cores and 167G of memory **per GPU** (1/3 of the the node's resources)

gpu_short
    Partition for running short jobs on a GPU

    - One dedicated node with three **nVidia A40 GPUs**
    - Your job script must request **only one** GPU (eg ``#SBATCH --gres=gpu:1``) per job
    - Practical limit of three jobs at any one time, as the dedicated node only has three GPUs
    - Maximum memory per job is 167G
    - Maximum cores per job is 32

gpu_week
    Partition for running GPU jobs on any of the **nVidia A40 nodes** for up to a week

    - Maximum time is seven days (eg ``#SBATCH --time=7-00:00:00``)
    - Your job script should request **only** one GPU (eg ``#SBATCH --gres=gpu:1``)
    - The ``gpu_week`` partition is limited to running **a maximum of three GPUs** at any time, across all users

gpu_interactive
    Partition for running interactive jobs with a GPU

    - One dedicated node with three **nVidia A40 GPUs**
    - Your job script must request **only one** GPU (eg ``#SBATCH --gres=gpu:1``)
    - Only **one job per user** on this partition
    - Maximum memory per job is 167G
    - Maximum cores per job is 32

gpuplus
    Partition for running jobs that require more GPU power, see documentation for details about how to request GPUs :ref:`request GPUs <gpu-jobs>`.

    - Each of the six nodes house two **nVidia H100 GPUs**
    - Your job script must request at least one GPU (eg ``#SBATCH --gres=gpu:1``)
    - You are limited to **no more than two GPUs** at a time across all of your jobs running in the ``gpuplus`` partition

himem
    For running jobs that require memory greater than that available in other partitions. Each of the two nodes (himem01 and himem02) have 96 cores. The max running cores and max running memory limits are practical limits, due to the resources available on the nodes.

himem_week
    Partition for running jobs that require memory greater than that available in other partitions. The max running cores and max running memory limits are practical limits, due to the resources available on the nodes.

interactive
    Partition for jobs that would like to use Viking interactively.  This could be used for graphical work with the **eight hour queue limit** set to mimic a working day. You can run interactive jobs in the ``nodes`` partition (or any other), but the queue time will be shorter in the ``interactive`` partition.
