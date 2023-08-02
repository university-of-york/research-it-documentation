Software On Viking
==================

.. note::
    All users have the ability to download, build (if necessary) and run software as long as it's compatible with Viking. We do our best to fulfill all software install requests quickly however, if it's a small or simple program, it can sometimes be beneficial for a user to download and build the software themselves.


Modules And The User Environment
--------------------------------

Most software installed on Viking are made available through the module system ``Lmod``. This allows multiple versions of the same software to be installed, without conflicting or interfering with each other. By loading modules, the user environment is automatically modified to set the appropriate variables (``$PATH`` etc.) to make the corresponding software visible.

For a quick overview of the available ``module`` sub-commands and options, try typing ``module help`` on Viking:

.. code-block:: console

    $ module help


.. note::

    The command ``ml`` is a handy front end for the ``module`` command. On Viking try ``ml --help`` to see how you can use it as shorthand for ``module load`` and other commands. We'll continue to use explicit commands like ``module load`` in this guide but know you can use ``ml`` a lot of the time instead. Try it out! 😎


Searching For Modules
---------------------

.. code-block:: console

    $ module spider Python


Loading
--------

.. code-block:: console

    $ module load lang/Python/3.10.8-GCCcore-12.2.0


Listing Modules In Use
----------------------

.. code-block:: console

    $ module list


Unloading A Module
------------------

.. code-block:: console

    $ module unload lang/Python/3.10.8-GCCcore-12.2.0


Purge All Modules
------------------

.. code-block:: console
    :caption: this is handy to put in your jobscript before you load the necessary modules, which can ensure reproducable results

    $ module purge
