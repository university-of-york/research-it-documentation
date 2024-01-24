Software on Viking
==================

.. admonition:: Did you know...

    We provide a central library of software installed for all users to benefit from, although everyone has the ability to download, build, and run software as long as it's compatible with Viking.
    We do our best to fulfill all software install requests quickly, however, if it's a small or simple program, it can sometimes be beneficial for a user to download and build the software themselves. 🏗️👷🦺


Modules and the user environment
--------------------------------

Most software installed on Viking are made available through the module system ``lmod``. This allows multiple versions of the same software to be installed without conflicting or interfering with each other. By loading modules, the user environment is automatically modified to set the appropriate variables (``$PATH`` etc.) to make the corresponding software visible.

For a quick overview of the available ``module`` sub-commands and options, try typing ``module help`` on Viking:

.. code-block:: console

    $ module help


.. tip::

    The command ``ml`` is a handy front end for the ``module`` command. On Viking, try typing ``ml --help`` to see how you can use it as shorthand for ``module load`` and other commands. We'll continue to use explicit commands like ``module load`` in this guide but know you can use ``ml`` a lot of the time instead. Try it out! 😎


Using the module command
------------------------

Try out the commands below and see their output. Very quickly you will be able to find modules of familiar software, load and unload them.

Searching for modules
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
    :caption: note the trailing slash '/' this helps reduce the output

    $ module spider Python/


For even more control over the search you can use regular expressions, for example:

.. code-block:: console

    $ module -r spider '^Python'


.. hint::

    Try running the command ``module overview`` to give you a nicely categorised view of all names and number versions of each module on Viking.


Loading a module
^^^^^^^^^^^^^^^^

.. code-block:: console

    $ module load {MOD_PYTHON}


.. attention::

    Always use the **full module name**, including version and toolchain. Being specific means that as new modules are added your work remains the same and reproducible.


Listing modules in use
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ module list


Unloading a module
^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ module unload {MOD_PYTHON}


Purge all modules
^^^^^^^^^^^^^^^^^^

.. code-block:: console
    :caption: this is handy to put in your jobscript before you load the necessary modules, which can ensure reproducible results

    $ module purge
