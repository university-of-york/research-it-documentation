Software on Viking
==================

.. admonition:: Did you know...

    All users have the ability to download, build and run software as long as it's compatible with Viking. We do our best to fulfill all software install requests quickly however, if it's a small or simple program, it can sometimes be beneficial for a user to download and build the software themselves. 🏗️👷🦺


Modules and the User Environment
--------------------------------

Most software installed on Viking are made available through the module system ``lmod``. This allows multiple versions of the same software to be installed, without conflicting or interfering with each other. By loading modules, the user environment is automatically modified to set the appropriate variables (``$PATH`` etc.) to make the corresponding software visible.

For a quick overview of the available ``module`` sub-commands and options, try typing ``module help`` on Viking:

.. code-block:: console

    $ module help


.. tip::

    The command ``ml`` is a handy front end for the ``module`` command. On Viking try typing ``ml --help`` to see how you can use it as shorthand for ``module load`` and other commands. We'll continue to use explicit commands like ``module load`` in this guide but know you can use ``ml`` a lot of the time instead. Try it out! 😎


Using the Module Command
------------------------

Try out the commands below and see their output. Very quickly you will be able to find modules of familiar software, load and unload them.

Searching for Modules
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ module spider Python


Loading a Module
^^^^^^^^^^^^^^^^

.. code-block:: console

    $ module load lang/Python/3.10.8-GCCcore-12.2.0


.. attention::

    Always use the **full module name**, including version and toolchain. Being specific means that as new modules are added your work remains the same.


Listing Modules in Use
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ module list


Unloading a Module
^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ module unload lang/Python/3.10.8-GCCcore-12.2.0


Purge All Modules
^^^^^^^^^^^^^^^^^^

.. code-block:: console
    :caption: this is handy to put in your jobscript before you load the necessary modules, which can ensure reproducible results

    $ module purge
