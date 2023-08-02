Quickstart
==========

.. note::
    Please ensure you are on the campus network or :ref:`connected to the university VPN <connecting-off-campus>`. If you haven't already please :ref:`create an account <creating-an-account>`.


Log in to Viking
----------------

.. code-block:: console
    :caption: from a linux terminal

    ssh viking.york.ac.uk


Find the Software You Need
--------------------------

.. code-block:: console

    module spider lang/Python


Load a Module
--------------

.. code-block:: console

    load module lang/Python/3.10.8-GCCcore-12.2.0


Develop and Test
----------------

Develop and test the the job you plan to create. Remember not to leave a proper job running on the login node as this can affect other users. If you are testing something and need to kill the command whilst it's running, press ``CTRL + C``.


Create Job Script
-----------------

In your favorite text editor, create a jobscript for your job. Save it as something like ``myjobscript.job``.

.. code-block:: bash
    :caption: this is just a basic template

    #!/usr/bin/env bash
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --ntasks=10                     # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=16G                       # Total memory to request
    #SBATCH --time=0-00:15:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --mail-type=END,FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk   # Where to send mail
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --error=%x-%j.err               # Standard error log

    # Purge any previously loaded modules #
    module purge

    # Load modules #
    module load lang/Python/3.10.8-GCCcore-12.2.0

    # Commands to run #
    echo My working directory is: `pwd`
    echo Running job on host:
    echo -e '\t'`hostname` at `date`'\n'

    python -c 'print ("Hello, world!")'

    echo '\n'Job completed at `date`


Send the Jobscript to the Job Scheduler
---------------------------------------

.. code-block:: console

    sbatch myjobscript.job


Check Results
--------------

Depending on what you set for ``#SBATCH --mail-type=`` you should receive some emails as the job progresses. When the job is completed you should have a log file in the directory where you ran the ``sbatch`` command originally. This is a great opportinuty to see how efficient your job was.


Adjust the Jobscript
--------------------

If your ``CPU`` or ``memory`` utilisation is very low, it means your settings in the jobscript need adjusting if you are to run the job again. Now is a good time to adjust these down, you should aim them pretty close to the end results, this will mean that Viking can start more jobs quicker and everyone can get their results faster. That's teamwork! ❤️
