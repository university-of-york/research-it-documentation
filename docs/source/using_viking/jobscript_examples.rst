Jobscript Examples
==================


In this section we'll try to give some general purpose examples of different jobscripts. Viking can run a vast array of programs to achieve results in many ways and so this page is really just the foundation to what is possible. Below we'll try and give some nice simple examples for some of the main types of job script which you can use and build upon yourself.


.. admonition:: We need your help!

    If you have a splendid jobscript, maybe it's super efficient, has a neat trick or maybe it does something not shown here. If that's the case then please send it to us so we can add it to this site and share it with everyone else. You never know, you may just make someone's day!


.. hint::

    The `Slurm Documentation site <https://slurm.schedmd.com/sbatch.html>`_ has the complete list of options you can use in an jobscript for ``sbatch``, it's quite a lot so please refer there for more information or type ``man sbatch`` on Viking for the manual.

Jobscript Layout
----------------

Jobscripts for ``sbatch`` must begin with the `shebang <https://en.wikipedia.org/wiki/Shebang_(Unix)>`_ and the path to the ``bash`` interpreter (we then use \'`set -e <https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html>`_\' to stop processing on the first error). Next are the ``sbatch directives``, which must be all together, before any other commands. Finally you have the commands you wish to run, which should include which modules you wish to load.


Managing Time
^^^^^^^^^^^^^

The time directive is the time that the job take to run. It can be omitted in which case the default time is 8 hours. The job will be killed if it exceeds this time. Specifying a shorter and more accurate time will allow your job to start execution sooner. The time can be specified in two ways in the format ``DD-HH:MM:SS``:

    1. In the job script using the ``#SBATCH --time=00-02:00:00`` directive **RECOMMENDED**
    2. On the command line using the ``--time=00-02:00:00`` option


Controlling Memory Usage
^^^^^^^^^^^^^^^^^^^^^^^^

You need to understand the memory requirements of your program. A job has a default memory allocation and sometimes you will need to request a little more memory so your program can run. Specify the real memory required per node, default units are megabytes ``--mem=<size[units]>`` for example: ``#SBATCH --mem=1G``

Redirecting Output
^^^^^^^^^^^^^^^^^^

The %j in the ``#SBATCH --output`` line tells ``Slurm`` to substitute the ``job ID`` in the name of the output file. You can also add a ``#SBATCH --error`` with an error file name to separate output and error logs.


Filename Patterns
^^^^^^^^^^^^^^^^^

There are several useful placeholders that can be used in filenames which will be automatically filled in by ``Slurm``. The full list of these can be found in the ``sbatch`` man page, under the ``filename pattern`` heading or in the `online documentation <https://slurm.schedmd.com/sbatch.html#lbAH>`_.


.. attention::

    Specifying a project account code is mandatory, please use the following line in your batch scripts so that we can associate your work with your project:

    ``#SBATCH --account=YOUR-PROJECT-CODE``


Single Process Jobs
-------------------

For software that does not support any parallelisation, or where single threaded operation is desired, the following example job script can serve as a template.

.. code-block:: bash
    :linenos:

    {SHEBANG}
    #----------------------------- Slurm directives ------------------------------#
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=1G                        # Total memory to request
    #SBATCH --time=0-00:05:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --output=%x-%j.log              # Standard output log

    # purge any existing modules
    module purge

    #--------------------------- Load software modules ---------------------------#
    module load {MOD_COMPILER}

    #------------------------- Directory/file management -------------------------#
    # copy example source code if it doesn't exist
    if [[ ! -f serial_example.cpp ]] && [[ ! -f serial_example ]]; then
        cp /mnt/lustre/groups/viking-examples/serial_job/serial_example.cpp .
    fi

    #------------------------------ Commands to run ------------------------------#
    echo My working directory is: `pwd`
    echo Running job on host:
    echo -e '\t'`hostname` at `date`'\n'

    # compile example, if executable doesn't already exist
    if [[ ! -f serial_example ]]; then
        g++ -o serial_example serial_example.cpp
    fi

    # run example
    ./serial_example 5

    echo '\n'Job completed at `date`


Threaded / Multi-Process Jobs
-----------------------------

.. caution::
    FIXME: needs explanation

.. code-block:: bash
    :linenos:

    {SHEBANG}
    #----------------------------- Slurm directives ------------------------------#
    #SBATCH --job-name=threaded_example     # Job name
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=8               # Number of CPU cores per MPI task
    #SBATCH --mem=1G                        # Total memory to request
    #SBATCH --time=0-00:05:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --output=%x-%j.log              # Standard output log

    # purge any existing modules
    module purge

    #--------------------------- Load software modules ---------------------------#
    module load {MOD_COMPILER}

    #------------------------- Directory/file management -------------------------#
    # copy example source code if it doesn't exist
    if [[ ! -f threaded_example.cpp ]] && [[ ! -f threaded_example ]]; then
        cp /mnt/lustre/groups/viking-examples/threaded_job/threaded_example.cpp .
    fi

    #------------------------------ Commands to run ------------------------------#
    echo My working directory is: `pwd`
    echo Running job on host:
    echo -e '\t'`hostname` at `date`'\n'

    # compile example, if executable doesn't already exist
    if [[ ! -f threaded_example ]]; then
        g++ -fopenmp -o threaded_example threaded_example.cpp -lpthread
    fi

    # run example
    ./threaded_example

    echo '\n'Job completed at `date`


Multi-processor Jobs
--------------------

.. caution::
    FIXME: needs explanation

.. code-block:: bash
    :linenos:

    {SHEBANG}
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --ntasks=40                     # Number of MPI tasks to request
    #SBATCH --cpus-per-task=1               # Number of CPU cores per MPI task
    #SBATCH --mem=16G                       # Total memory to request
    #SBATCH --time=0-00:15:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --mail-type=END,FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk   # Where to send mail
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --error=%x-%j.err               # Standard error log

    # purge any existing modules
    module purge

    # Load modules #
    module load {MOD_PYTHON}

    # Commands to run #
    echo My working directory is: `pwd`
    echo Running job on host:
    echo -e '\t'`hostname` at `date`'\n'

    python -c 'print ("Hello, world!")'

    echo '\n'Job completed at `date`


Array Jobs
----------

.. caution::
    FIXME: needs explanation

.. code-block:: bash
    :linenos:

    {SHEBANG}
    #SBATCH --job-name=my_job               # Job name
    #SBATCH --ntasks=1                      # Number of MPI tasks to request
    #SBATCH --cpus-per-task=2               # Number of CPU cores per MPI task
    #SBATCH --mem=8G                        # Total memory to request
    #SBATCH --time=0-00:15:00               # Time limit (DD-HH:MM:SS)
    #SBATCH --account=dept-proj-year        # Project account to use
    #SBATCH --mail-type=END,FAIL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk   # Where to send mail
    #SBATCH --output=%x-%j.log              # Standard output log
    #SBATCH --error=%x-%j.err               # Standard error log
    #SBATCH --array=1-100                   # Array range

    # purge any existing modules
    module purge

    module load lang/R/4.1.2-foss-2021b

    echo "Job started on $(hostname) at $(date)"
    Rscript --vanilla code/simulation_array.R $SLURM_ARRAY_TASK_ID
    echo "Job finished at $(date)"
