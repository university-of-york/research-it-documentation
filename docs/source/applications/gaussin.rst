Gaussian
========

``Gaussian`` can be loaded using the following:

.. code-block:: console

    $ module load {MOD_GAUSSIAN}

This job script can be used to submit a ``Gaussian`` workflow to the cluster, using 16GB of memory, 16 cores and 48 hours. This assumes you have a Gaussian file called ``g16.gjf`` . Remember to update the account code and email address provided to ``slurm`` to your own details.

.. code-block:: bash
    :linenos:

    {SHEBANG}
    #SBATCH --job-name=Gaussian_CPU_example    # Job Name
    #SBATCH --account=dept-proj-year           # Project account to use
    #SBATCH --mail-type= BEGIN, END, FAIL      # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk      # Where to send mail
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=16
    #SBATCH --mem=16gb
    #SBATCH --time=48:00:00
    #SBATCH --output=output.log
    #SBATCH --partition=nodes

    # Abort if any command fails
    set -e

    module purge                               # purge any loaded modules
    module load {MOD_GAUSSIAN}
    g16 g16.gjf

.. note::

    Gaussian can be run both with and without a GPU

As ``Gaussian`` is licensed software, you will need to be added to the Gaussian group on Viking in order to use it. If you find that you can't use ``Gaussian`` on Viking due to permission errors, please get in touch with Viking support via an email to itsupport@york.ac.uk.

