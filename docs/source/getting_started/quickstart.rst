Quickstart
==========

.. attention::
    Please ensure you are on the campus network or :ref:`connected to the University VPN <connecting-off-campus>`. If you haven't already please :ref:`create an account <creating-an-account>`.

    For the time being if you are using the ``eduroam`` WiFi you need to connect to Viking as if you are off campus and use the University VPN.

.. attention::

    The ``ssh fingerprints`` for the two login nodes are listed below. If you connected to the old Viking previously then you will probably see a warning that the fingerprint has changed. The correct fingerprints for the two login nodes are:

    .. code-block:: console

        SHA256:e6QUl1pE1RK55unuALoNDXaEvJLcam4LJo6P07nbGcs (RSA)
        SHA256:jn1KdPw+M9iws+uEwsnuqC5NVph4eNT095m22RFz4Mw (ECDSA)
        SHA256:TztJ/bGgPiK6bIGfQqRQnxfg/nVhw978T6kyy9HhJTQ (ED25519)



Log in to viking
----------------

.. code-block:: console
    :caption: from a Linux / MacOS terminal

    $ ssh viking.york.ac.uk

.. admonition:: Windows Users

    It's a little bit more involved than the one line above but we have :ref:`nice breakdown here <connecting-via-windows>`.


Find the software you need
--------------------------

.. code-block:: console

    $ module spider Python


.. FIXME: add example output


Load a module
--------------

.. code-block:: console

    $ module load {MOD_PYTHON}


.. FIXME: check this is correct

.. hint::

    The module name scheme on Viking is as follows: ``program_name`` / ``version`` or sometimes - ``program_name`` / ``version`` / ``toolchain`` - ``toolchain_version``.

    To read more about the EasyBuild concept of *common toolchains*, please see the `EasyBuild docs <https://docs.easybuild.io/common-toolchains/>`_. In it's simplest sense, think of it as the compiler version the software was build with.


Develop and test
----------------

Develop and test the the job you plan to create. Remember not to leave a proper job running on the login node as this can affect other users. If you are testing something and need to kill the command whilst it's running, press ``Ctrl + c``.


Create job script
-----------------

In your favorite text editor, create a jobscript for your job. Save it as something like ``myjobscript.job``.

.. tip::

    Please change the email address **abc123@york.ac.uk** below to your own email address and see the emails it generates!


.. code-block:: bash
    :caption: this is just a basic template
    :linenos:

    {SHEBANG}
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --nodes=1                       # Number of nodes to run on
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=16G                       # Total memory to request
    #SBATCH --time=0-00:15:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --mail-type=END,FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk   # Where to send mail
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --error=%x-%j.err               # Standard error log
    #SBATCH --partition=test

    # Abort if any command fails
    set -e

    # Purge any previously loaded modules #
    module purge

    # Load modules #
    module load {MOD_PYTHON}

    # Commands to run #
    echo My working directory is: `pwd`
    echo Running job on host:
    echo -e '\t'`hostname` at `date`'\n'

    python -c 'print ("Hello, world!")'

    echo '\n'Job completed at `date`


Send the jobscript to the job scheduler
---------------------------------------

.. code-block:: console

    $ sbatch myjobscript.job


Check results
--------------

Depending on what you set for ``#SBATCH --mail-type=`` you should receive some emails as the job progresses. When the job is completed you should have a log file in the directory where you ran the ``sbatch`` command originally. This is a great opportunity to see how efficient your job was.


Adjust the jobscript
--------------------

If your ``CPU`` or ``memory`` utilisation is very low, it means your settings in the jobscript need adjusting if you are to run the job again. Now is a good time to adjust these down, you should aim to get the actual utilisation close to the requested values, this will mean that Viking can start more jobs quicker and everyone can get their results faster. That's teamwork! ❤️

.. note::

    In this example jobscript we specified the jobs to run on the ``test`` ``partition`` as we are just testing. For full jobs generally most users will be want to use the default ``nodes`` partition, you can see more about this on the :doc:`resource partitions </using_viking/resource_partitions>` page.
