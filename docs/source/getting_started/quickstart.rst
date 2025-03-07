Quickstart
==========

.. attention::
    Please ensure you are on the campus network or :ref:`connected to the University VPN <connecting-off-campus>`. If you haven't already please :ref:`create an account <creating-an-account>`.

Log in to Viking
----------------

.. code-block:: console
    :caption: from a Linux or MacOS terminal or Windows PowerShell with OpenSSH installed

    $ ssh abc123@viking.york.ac.uk

Remember to substitute ``abc123`` with your IT Services username.

.. hint::

    If you previously connected to the old Viking then you may see a warning that the fingerprint has changed. Please see the :doc:`FAQ </faq/faq>` for how to overcome this.


.. admonition:: Windows Users

    The latest builds of Windows 10 and Windows 11 include a built-in ``ssh`` client, so you can run ``ssh`` commands directly from a ``CMD`` or ``PowerShell`` window. To run either of these search for ``CMD`` or ``PowerShell`` from the Windows search box and then type in the above command. If you're on a personal device and need to install the ``ssh`` client please follow the `Microsoft website <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui#install-openssh-for-windows>`_. Alternatively you can install ``PuTTY`` which is only a little bit more involved than the one line above but we have :ref:`nice breakdown here <connecting-via-windows>` to help.


Find the software you need
--------------------------

.. code-block:: console

    $ module spider Python


.. FIXME: add example output

There is lots of output as Python is mentioned in lots of modules. For more control over the search you can use `regular expressions <https://datasciencedojo.com/blog/regular-expression-101/#>`_ with the ``-r`` option, for example:

.. code-block:: console

    $ module -r spider '^Python'


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
