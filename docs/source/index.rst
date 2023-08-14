.. include:: global.rst

Welcome to the Viking Documentation!
======================================

.. caution::

   This project is under active development.

.. list of all the pages which are hidden on this page but used to build the navbar

.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :hidden:

   getting_started/quickstart
   getting_started/code-of-conduct
   getting_started/creating-accounts
   getting_started/connecting-to-viking
   getting_started/connecting-off-campus
   getting_started/data-management-and-user-quota

.. toctree::
   :maxdepth: 1
   :caption: Using Viking
   :hidden:

   using_viking/software-on-viking
   using_viking/submitting-jobs
   using_viking/resource-partitions
   using_viking/jobscript-examples
   using_viking/jobscripts-program-specific
   using_viking/terminal-multiplexing
   using_viking/virtual-desktops

.. toctree::
   :maxdepth: 1
   :caption: Beginners Guides
   :hidden:

   beginners_guide/linux-shell

.. toctree::
   :maxdepth: 1
   :caption: In Depth Guides
   :hidden:

   in_depth/program-specific-how-tos


**Viking** is a large, Linux compute cluster with many nodes, CPUs, GPUs, lots of storage and boat loads of memory. Viking is housed in Sweden (of course!) in the forward thinking `EcoDataCentre <https://ecodatacenter.tech/>`_, which is one of the most sustainable data centres in the whole world. 🌍🥰

Cluster Configuration
---------------------

.. csv-table:: Viking breakdown
    :file: assets/data/viking_stats.csv
    :align: center



Check out the :doc:`getting_started/quickstart` section for a speedy guide to getting started or for a more in depth guide, start with the :doc:`getting_started/creating-accounts` page.

If you are brand new to using the Linux commands line then how about a quick tutorial from Ubuntu called `The Linux command line for beginners <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>`_ or have a read of our own :doc:`beginners guide to the Linux shell </beginners_guide/linux-shell>`.


.. hint::

   In the examples of the Viking command line which we show here they will all begin with the dollar symbol ``$``, you don't need to copy this it's just there to help show you that it's a command prompt we are describing. For example you'll see things like this:

.. code-block:: console

   $ module spider Python
