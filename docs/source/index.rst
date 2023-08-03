Welcome to the Viking Documentation!
======================================

.. caution::

   This project is under active development.

**Viking** is a large, Linux compute cluster with many nodes, CPUs, GPUs, lots of storage and boat loads of memory. Viking is housed in Sweden (of course!) in the forward thinking `EcoDataCentre <https://ecodatacenter.tech/>`_, which is one of the most sustainable data centres in the whole world.

Contents
--------

.. toctree::
   :maxdepth: 1

   quickstart
   code-of-conduct
   creating-accounts
   connecting-to-viking
   connecting-off-campus
   data-management-and-user-quota
   software-on-viking
   submitting-jobs
   available-partitions

Cluster Configuration
---------------------

+------------------------------+-----------+
| Compute node only CPU cores  | 12,864    |
+------------------------------+-----------+
| Total standard compute nodes | 134       |
+------------------------------+-----------+
| Compute node generation      | AMD EPYC3 |
+------------------------------+-----------+
| Cores per processor          | 48        |
+------------------------------+-----------+
| Number of processors per node| 2         |
+------------------------------+-----------+
| Memory per compute node      | 512 GB    |
+------------------------------+-----------+
| High memory node             | 2x 2TB    |
+------------------------------+-----------+
| High memory node             | 1x 4 TB   |
+------------------------------+-----------+
| GPUs                         | 48x A40   |
|                              | 12x H100  |
+------------------------------+-----------+
| Scratch (PB)                 | 1         |
+------------------------------+-----------+
| Usable NVME storage (TB)     | 215       |
+------------------------------+-----------+
| Interconnect type            | 100Gb OPA |
+------------------------------+-----------+


Check out the :doc:`quickstart` section a speedy guide to getting started or the more in depth guide starting with the :doc:`creating-accounts` page.

If you are new to using Linux then how about a quick :doc:`FIXME-LINUXBEGINNER` course?


