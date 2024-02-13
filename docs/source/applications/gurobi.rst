Gurobi
======

The `Gurobi Optimizer <https://www.gurobi.com/>`_  is a state-of-the-art solver for mathematical programming. The solvers in the Gurobi Optimizer were designed from the ground up to exploit modern architectures and multi-core processors, using the most advanced implementations of the latest algorithms.

Gurobi is licenced software with some restrictions on it's use. It is available on Viking however you must agree to the terms by completing the `Gurobi Licence form <https://forms.gle/yegV2kE3tp9gac9TA>`_ either during your initial Viking new user sign up process or any time after. Once the form has been completed you should automatically join the ``viking-gurobi`` group on Viking later that day (it may take up to 24 hours to complete).

.. tip::

    You can check what groups you are a member of with the ``id`` command.

To load the module Gurobi module on Viking:

.. code-block:: console

    $ module load {MOD_GUROBI}

If you receive the following error, then you are not a member of the ``viking-gurobi`` Viking group and will need to complete the form and wait to be added to the group:

.. error::

    Lmod has detected the following error:  You are not part of 'viking-gurobi' group of users that have access

If all is well and you successfully load the module then you'll be given two suggestions for using Gurobi:

.. code-block:: console

    Gurobi shell based on Python 3.10.8 can be launched with command `gurobi.sh`
    Gurobi Python Interface can be loaded in Python 3.10.8 with 'import gurobipy'

