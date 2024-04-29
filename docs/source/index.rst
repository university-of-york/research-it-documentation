.. include:: /global.rst

Welcome to the Viking Documentation!
======================================

.. list of all the pages which are hidden on this page but used to build the navbar

.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :hidden:

   getting_started/quickstart
   getting_started/code_of_conduct
   getting_started/acknowledgements
   getting_started/creating_accounts
   getting_started/connecting_to_viking
   getting_started/connecting_off_campus
   getting_started/storage_quota
   getting_started/storage_on_viking
   getting_started/backing_up

.. toctree::
   :maxdepth: 1
   :caption: Using Viking
   :hidden:

   using_viking/software_on_viking
   using_viking/submitting_jobs
   using_viking/jobscript_examples
   using_viking/resource_partitions
   using_viking/terminal_multiplexing
   using_viking/virtual_desktops
   using_viking/virtual_environments
   using_viking/x11_forwarding
   using_viking/project_folders

.. toctree::
   :maxdepth: 1
   :caption: Data management
   :hidden:

   data_management/filestore
   data_management/vault
   data_management/google_drive
   data_management/drop_off
   data_management/other_locations


.. toctree::
   :maxdepth: 1
   :caption: Application Guides
   :hidden:

   Specific application guides <applications/index>

.. toctree::
   :titlesonly:
   :caption: Frequently asked questions
   :hidden:

   faq/faq

.. toctree::
   :maxdepth: 1
   :caption: Beginners Guides
   :hidden:

   beginners_guide/linux_shell


**Viking** is a large, Linux compute cluster with many nodes, CPUs, GPUs, lots of storage and boat loads of memory. Viking is housed in Sweden (of course!) in the forward thinking `EcoDataCentre <https://ecodatacenter.tech/>`_, which is one of the most sustainable data centres in the whole world. 🌍🥰

Cluster Configuration
---------------------

.. csv-table:: Viking breakdown
    :file: /assets/data/viking_stats.csv
    :align: center



Check out the :doc:`getting_started/quickstart` section for a speedy guide to getting started or for a more in depth guide, start with the :doc:`getting_started/creating_accounts` page.

If you are brand new to using the Linux commands line then how about a quick tutorial from Ubuntu called `The Linux command line for beginners <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>`_ or have a read of our own :doc:`beginners guide to the Linux shell </beginners_guide/linux_shell>`.


.. hint::

   In the examples of the Viking command line which we show here they will all begin with the dollar symbol ``$``, you don't need to copy this it's just there to help show you that it's a command prompt we are describing. For example you'll see things like this:

.. code-block:: console

   $ module spider Python
