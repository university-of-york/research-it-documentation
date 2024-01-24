AtChem 2
========

``AtChem2`` is a modelling tool for atmospheric chemistry. It is primarily designed to use the `Master Chemical Mechanism (MCM) <https://mcm.york.ac.uk>`_, but it can be used with any general set of chemical reactions. The MCM is a near-explicit chemical mechanism which describes the gas-phase oxidation of volatile organic compounds (VOC) in the lower atmosphere. The latest stable version of AtChem2 can be downloaded from the `AtChem2 GitHub <https://github.com/AtChem/AtChem2/releases>`_.

This documentation will take you through getting a copy of the ``AtChem2`` source code, setting up the environment for ``AtChem2`` use, building a model, and submitting a model run to Viking's job scheduler, in batch mode.


Setting up the environment
--------------------------

To work with ``AtChem2`` you will need to load the following modules on Viking:

.. code-block:: console
    :caption: Modules needed for AtChem2

    $ module load GCC/11.2.0                   # Fortran compilter
    $ module load SUNDIALS/2.7.0-foss-2021b    # Solving suite
    $ module load OpenLibm/0.8.1-GCC-11.2.0    # Maths library
    $ module load Python/3.9.6-GCCcore-11.2.0  # A Python interpreter


Next, clone a copy of the ``AtChem2`` source code and move into the directory

.. code-block:: console
    :caption: Cloning AtChem2 source code

    $ git clone https://github.com/AtChem/AtChem2.git atchem2
    $ cd atchem2


Building a model
----------------

The 'Installation, Setup, and Execution' section of the `AtChem2 README <https://github.com/AtChem/AtChem2/blob/master/README.md>`_ describes the process of building a model, which will be paraphrased here.

Make a copy of the AtChem2 Makefile template - this will be used by the model build script to compile the model (if you're interested in learning more about what a Makefile is, have a look at the `GNU docs <https://www.gnu.org/software/make/>`_):

.. code-block:: console
    :caption: Making a copy of the template Makefile

    $ cp tools/install/Makefile.skel ./Makefile


Open the Makefile in a text editor (if you're not sure how to do this, see `this tutorial <https://swcarpentry.github.io/shell-novice/03-create/index.html#create-a-text-file>`_), and change the values of ``CVODELIBDIR`` and ``OPENLIBMDIR`` to correspond with the Viking module environment, i.e:

.. code-block:: bash
    :caption: Default Makefile parameters

    CVODELIBDIR     = cvode/lib
    OPENLIBMDIR     = openlibm-0.4.1

becomes:


.. code-block:: bash
    :caption: Makefile parameters after changing

    CVODELIBDIR     = /opt/apps/eb/software/SUNDIALS/2.7.0-foss-2021b/lib
    OPENLIBMDIR     = /opt/apps/eb/software/OpenLibm/0.8.1-GCC-11.2.0/lib


Run the AtChem2 build script, giving it the location of a `FACSIMILE format <https://www.mcpa-software.com/>`_ mechanism with which to build your model (for this example, we are using the test mechanism supplied with AtChem2):

.. code-block:: console
    :caption: Running the AtChem2 build script

    $ ./build/build_atchem2.sh model/mechanism.fac

You will see some text describing what this process is doing, as well as some compiler warnings - don't worry about these! If this process completes successfully, you should now have an AtChem2 executable file in the current directory.

Test that the mechanism test model built correctly by running it:

.. code-block:: console
    :caption: Testing the model

    $ ./atchem2

If the model runs successfully, you should see a 'final statistics' statement in the output that looks like the following:

.. code-block:: console
    :caption: Output for the test mechanism

    ------------------
     Final statistics
    ------------------
     No. steps = 603   No. f-s = 699   No. J-s = 1003   No. LU-s = 100
     No. nonlinear iterations = 696
     No. nonlinear convergence failures = 0
     No. error test failures = 28

     Runtime = 0
     Deallocating memory.

Model outputs are saved in the ``model/output`` directory:

.. code-block:: console
    :caption: Model output files

    $ ls model/output
    environmentVariables.output  finalModelState.output  lossRates.output             photolysisRates.output            productionRates.output  speciesConcentrations.output
    errors.output                jacobian.output         mainSolverParameters.output  photolysisRatesParameters.output  reactionRates


At this point, you can build and run AtChem2 models, and are ready to start using your own mechanisms and configuring the model parameters for your simulations. Please refer to the `AtChem2 wiki <https://github.com/AtChem/AtChem2/wiki/How-to-run-AtChem2>`_ or the `AtChem2 User Manual <https://raw.githubusercontent.com/AtChem/AtChem2/master/doc/AtChem2-Manual.pdf>`_ for comprehensive information about how to work with AtChem2.

Running models
--------------

An example Slurm batch script is shown below for the test mechanism used above.
This requests a single core and 100MB of RAM and will run for a maximum of 2 minutes.
If you are using the same mechanism file for multiple model runs you can build the model on the login node outside of the job rather than rebuilding it for each submission.

.. code-block:: bash
    :caption: Example AtChem2 job script

    #!/usr/bin/env bash

    #SBATCH --job-name=atchem2_mech_test
    #SBATCH --mail-user=USERNAME@york.ac.uk
    #SBATCH --mail-type=ALL
    #SBATCH --output=atchem2_mech_test.log
    #SBATCH --account=VIKING-PROJECT-ACCOUNT-CODE

    #SBATCH --partition=nodes
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=100MB
    #SBATCH --time=00:02:00

    cd ${SLURM_SUBMIT_DIR} || exit

    module load GCC/11.2.0
    module load SUNDIALS/2.7.0-foss-2021b
    module load OpenLibm/0.8.1-GCC-11.2.0
    module load Python/3.9.6-GCCcore-11.2.0

    ./build/build_atchem2.sh model/mechanism.fac
    ./atchem2
