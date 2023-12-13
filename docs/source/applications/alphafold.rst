.. include:: /global.rst

AlphaFold
=========

`AlphaFold <https://deepmind.com/blog/article/putting-the-power-of-alphafold-into-the-worlds-hands>`_ is an AI system developed by `DeepMind <https://deepmind.com/>`_ that predicts a protein's 3D structure from its amino acid sequence. The source code for the inference pipeline can be found on the `AlphaFold GitHub <https://github.com/deepmind/alphafold>`_ page.


.. attention::

    Since a few tweaks have been made to the installation, it is important to read through the following documentation before running any jobs with ``AlphaFold``.

The CPU-only version of ``AlphaFold`` can be loaded using the following:

.. code-block:: console

    $ module load {MOD_ALPHAFOLD_CPU}

And the GPU version of ``AlphaFold`` can be loaded using the following command:

.. code-block:: console

    $ module load {MOD_ALPHAFOLD_GPU}


Example job scripts
-------------------

.. code-block:: bash
    :caption: using 16 CPUs, 80 GBs of memory and for up to 24 hours

    {SHEBANG}
    #SBATCH --job-name=AlphaFold_cpu_example        # Job name
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=16
    #SBATCH --mem=80G
    #SBATCH --time=24:00:00
    #SBATCH --output=%x-%j.log
    #SBATCH --mail-type=BEGIN,END,FAIL              # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk           # Where to send mail
    #SBATCH --account=dept-proj-year                # Project account to use

    # Abort if any command fails
    set -e

    module purge                                    # purge any loaded modules
    # Load AlphaFold module
    module load {MOD_ALPHAFOLD_CPU}

    # Path to genetic databases
    export ALPHAFOLD_DATA_DIR={ALPHAFOLD_DB_PATH}{APLHPFOLD_DB_DATE}

    # Optional: uncomment to change number of CPU cores to use for hhblits/jackhmmer
    # export ALPHAFOLD_HHBLITS_N_CPU=8
    # export ALPHAFOLD_JACKHMMER_N_CPU=8

    # Run AlphaFold
    alphafold --fasta_paths=T1050.fasta --max_template_date=2020-05-14 --preset=full_dbs --output_dir=$PWD --model_names=model_1,model_2,model_3,model_4,model_5

.. code-block:: bash
    :caption: using a GPU in addition to 10 CPUs for up to 4 hours

    {SHEBANG}
    #SBATCH --job-name=AlphaFold_GPU_example    # Job name
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=10
    #SBATCH --gres=gpu:1
    #SBATCH --partition=gpu
    #SBATCH --time=4:00:00
    #SBATCH --output=%x-%j.log
    #SBATCH --mail-type=BEGIN,END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
    #SBATCH --mail-user=abc123@york.ac.uk       # Where to send mail
    #SBATCH --account=dept-proj-year            # Project account to use

    # Abort if any command fails
    set -e

    module purge                                # purge any loaded modules
    # Load AlphaFold module
    module load {MOD_ALPHAFOLD_GPU}

    # Path to genetic databases
    export ALPHAFOLD_DATA_DIR={ALPHAFOLD_DB_PATH}{APLHPFOLD_DB_DATE}

    # Optional: uncomment to change number of CPU cores to use for hhblits/jackhmmer
    # export ALPHAFOLD_HHBLITS_N_CPU=8
    # export ALPHAFOLD_JACKHMMER_N_CPU=8

    # Run AlphaFold
    alphafold --fasta_paths=T1050.fasta --max_template_date=2020-05-14 --preset=full_dbs --output_dir=$PWD --model_names=model_1,model_2,model_3,model_4,model_5


Notes for using AlphaFold on viking
-----------------------------------

``AlphaFold`` currently requires access to various genetic databases such as ``UniRef90``, ``MGnify``, ``BFD``, ``Uniclust30``, ``PDB70`` and ``PDB``.

To avoid needless duplication of large databases across the cluster, these have been made available in a central directory:

.. code-block:: console

    {ALPHAFOLD_DB_PATH}{APLHPFOLD_DB_DATE}

The name of the subdirectory ``{APLHPFOLD_DB_DATE}`` is a symlink which points to the latest databases which have been downloaded. You can see all the sets within the ``{ALPHAFOLD_DB_PATH}`` directory. The files are hosted on the  fast SSDs - which is recommended for ``AlphaFold`` due to the random I/O access patterns. As seen below this can cause jobs to run up to **2x faster** than if the databases were stored on the disk-based lustre filesystem.

It is important to note that we have made a few enhancements to the installation to facilitate easier usage:

- The location to the AlphaFold data can be specified via the ``$ALPHAFOLD_DATA_DIR``  environment variable, so you should define this variable in your AlphaFold job script: ``export ALPHAFOLD_DATA_DIR={ALPHAFOLD_DB_PATH}{APLHPFOLD_DB_DATE}``
- A symbolic link named ``alphafold`` , which points to the ``run_alphafold.py script`` , is included. This means you can just use ``alphafold``  instead of ``run_alphafold.py`` or ``python run_alphafold.py``.
- The ``run_alphafold.py``  script has been slightly modified such that defining ``$ALPHAFOLD_DATA_DIR``  is sufficient to pick up all the data provided in that location, meaning that you don't need to use options like ``--data_dir``  to specify the location of the data.
- Similarly, the ``run_alphafold.py``  script was tweaked such that the location to commands like ``hhblits``, ``hhsearch``, ``jackhmmer`` or ``kalign`` are already correctly set, and thus options like ``--hhblits_binary_path``  are not required.
- The Python script that are used to run ``hhblits``  and ``jackhmmer``  have been tweaked so you can control how many cores are used for these tools (rather than hard-coding this to 4 and 8 cores respectively).

  - If set, the ``$ALPHAFOLD_HHBLITS_N_CPU``  environment variable can be used to specify how many cores should be used for running ``hhblits``. The default of 4 cores will be used if ``$ALPHAFOLD_HHBLITS_N_CPU`` is not defined. The same applies for ``jackhmmer`` and ``$ALPHAFOLD_JACKHMMER_N_CPU`` .
  - Tweaking either of these may not be worth it however, since test jobs indicated that using more than 4/8 cores actually resulted in worse performance (although this may be workload dependent)


CPU vs GPU performance
----------------------

Shown below are the results of using the ``T1050.fasta`` example mentioned in the ``AlphaFold`` README with different resource allocations.

.. csv-table:: AlphaFold performance
    :file: /assets/data/alphafold_performance.csv
    :align: center
    :header-rows: 1

This highlights the importance of requesting resources when using ``AlphaFold``. These results suggest:

  - It is faster for almost all jobs to use the ``AlphaFold`` with the database stored on the SSDs
  - Using a GPU can considerably increase the speed at which a job completes (up to 6x)
  - Using a second GPU does not significantly reduce the runtime for a job
  - Counter intuitively, using more cores can lower performance

