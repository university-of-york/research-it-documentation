Software On Viking
==================

.. note::
    All users have the ability to download, build (if necessary) and run software as long as it's compatible with Viking. We do our best to fulfill all software install requests but this can take time so sometimes, especially if it's a small or simple program, it can be quicker for a user to install and run the program themselves.


Modules And The User Environment
--------------------------------

Most software installed on Viking are made available through the module system ``Lmod``. This allows multiple versions of the same software to be installed, without conflicting or interfering with each other. By loading modules, the user environment is automatically modified to set the appropriate variables (```$PATH``` etc.) to make the corresponding software visible.

For a quick overview of the available module sub-commands and options, try typing ``module help`` on Viking:

.. code-block:: console

    [abc123@login1(viking) ~]$ module help


Searching For Modules
---------------------

.. code-block:: console

    [abc123@login1(viking) ~]$ module spider Python


Loading
--------

.. code-block:: console

    [abc123@login1(viking) ~]$ module load lang/Python/3.10.8-GCCcore-12.2.0


Listing Modules In Use
----------------------

.. code-block:: console

    [abc123@login1(viking) ~]$ module list


Unloading
---------

.. code-block:: console

    [abc123@login1(viking) ~]$ module unload lang/Python/3.10.8-GCCcore-12.2.0
