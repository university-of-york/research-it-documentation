Virtual environments
====================

venv (Python)
-------------

For simple virtual environments, where you just need to install packages through ``pip``, ``venv`` can be a good choice. Here is a `really good article <https://www.bitecode.dev/p/relieving-your-python-packaging-pain>`_ about using ``venv`` in Python which is well worth the read. More info can be found in the `documentation <https://docs.python.org/3/library/venv.html>`_. Below we'll keep a quickstart guide of the list of commands to get a ``venv`` virtual environment up and running.

.. admonition:: Did you know?

   ``venv`` has been part of the standard library since Python 3.3

Quickstart
^^^^^^^^^^
.. code-block:: console

    $ mkdir new_project
    $ cd new_project
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ python3 -m pip install package1 package2 package3


First we create a new directory with ``mkdir new_project`` to house our project and run ``cd new_project`` to change into that directory. Next we create the ``venv`` virtual environment and tell it to store the files in a folder called ``.venv`` with the ``python3 -m venv .venv`` command. The directory called ``.venv`` can be name anything you like, it doesn't have to be ``.venv``.

.. admonition:: Info

    The full stop ``.`` at the beginning of the directory name makes it ``hidden``. This isn't necessary but can be handy to keep things organised. You can read more about `hidden files and directories here <https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory>`_.


Next we run ``source .venv/bin/activate`` which reads and executes the commands from the file name ``.venv/bin/activate`` - this then activates our environment and you'll see ``(.venv)`` pop up at the beginning of your command prompt like this:

.. code-block:: console

    (.venv) [abc123@login1 [viking] new_project]$

Now we're *inside* our virtual environment, we use Python to install the packages we need and we can start developing. We use ``python3 -m pip install`` command to install the packages, because the ``-m`` option means that particular ``python3`` is going to use *only its own* ``pip`` to install the packages. This is important because on Viking there are multiple different versions of ``Python`` and ``pip`` installed (and you can even install versions yourself in your home directory) - so this ensures that you use the *correct* ``pip`` associated with the ``python3`` that you are using.

Once all the required packages are installed you can start developing.

.. tip::

    To ``deactivate`` a ``venv`` environment, you simply type ``deactivate`` on the command line.


If you need a more complex virtual environment with complex dependencies then ``conda`` is probably more suited to your needs but remember that the best tool is the one that suits *your* needs best and makes the development process smoother for you.


Conda (multi-language)
----------------------

``Conda`` provides similar functionality to ``venv`` but with some additional useful features:

    - it is language-agnostic rather than being restricted to Python
    - it makes it easy to install different versions of Python (and other languages)
    - it hosts its own repository of pre-built packages

Viking provides the ``conda`` utility program, as part of the ``Miniconda`` module, to allow you to create and manage virtual environments. This page describes the basics of using ``conda``, as well as some Viking-specific configuration that you are likely to find useful. The full documentation of ``conda`` can be found in the `conda online documentation <https://docs.conda.io/projects/conda/en/latest/index.html>`_.

.. _conda_setup:

Initial setup
^^^^^^^^^^^^^

Before you get started using ``conda`` on Viking, there is a small amount of configuration that you can set up to make working with multiple environments much more straightforward. By default, ``conda`` will create environments and install packages into subdirectories of your ``HOME`` directory, namely:

.. code-block:: console

    /users/USERNAME/.conda/envs
    /users/USERNAME/.conda/pkgs

These directories inevitably end up containing many files, and Viking sets a quota on the number of files a user can have in their home directory of 100,000 files (this is to mitigate potential filesystem performance issues). In order for you to avoid hitting this 100,000 files limit, you can tell ``conda`` to create environments and install packages into a subdirectory of your ``scratch`` space instead of your ``HOME`` directory. To do this, you need to complete a few simple tasks:

1. Create directories in your scratch space to contain your Conda environments and packages. An example of this is: ``/users/USERNAME/scratch/conda_environments/envs`` and ``/users/USERNAME/scratch/conda_environments/pkgs``

.. code-block:: console

    $ cd ~
    $ mkdir -p scratch/conda_environments/envs
    $ mkdir -p scratch/conda_environments/pkgs


2. Create a conda configuration file in your ``HOME`` directory, specifically: ``/users/USERNAME/.condarc``

3. Add content to the newly-created ``.condarc`` configuration file to tell ``conda`` where to create environments and install packages. Using the example directory names from step 1, this would look like:

.. code-block:: console

    envs_dirs:
    - /users/USERNAME/scratch/conda_environments/envs
    pkgs_dirs:
    - /users/USERNAME/scratch/conda_environments/pkgs

You will also need to load the Miniconda module, which will enable you to make use of the ``conda`` tools. You can do this by running:

.. code-block:: console

   $ module load {MOD_MINICONDA}


in a Viking shell. At this point, you are ready to use the ``conda`` utility with no risk of hitting the 100,000 files quota on your ``HOME`` directory.


Creating an environment
^^^^^^^^^^^^^^^^^^^^^^^

There are a few different ways in which environments can be created using the ``conda`` utility, but we are going to describe what is perhaps the most reliable and reproducible method - using an environment file. An environment file is a `YAML <https://yaml.org/>`_ file that describes the environment that you would like to create. This allows you to recreate the same environment in multiple places and easily pass on a specification to other users to reproduce your findings. A simple example environment file is shown below.

.. code-block:: console
    :caption: my_first_environment.yaml

    name: my_first_environment
    channels:
      - conda-forge
    dependencies:
      - python=3.7
      - numpy
      - ipython
      - pip:
        - mido

The above file, ``my_first_environment.yaml``, has the following attributes:

    - **name**: the name of the Conda environment.
    - **channels**: the `Anaconda <https://anaconda.cloud/>`_ Cloud channels that should be used to find packages for this environment. There are many channels available, but the two most common that you will see are ``defaults``, which contains stable packages curated by the Anaconda team, and `conda-forge <https://conda-forge.org/>`_, a community-led channel containing a wide range of high-quality packages that are often of a more recent version than those in ``defaults``
    - **dependencies**: the dependencies of the environment that you want to create. In the example above, we have specified a Python version that we want to use (3.7), some packages to be installed from the ``conda-forge`` channel that we named earlier in the environment file, and a package to be installed from `PyPI <https://pypi.org/>`_ through ``pip``, as the package is not available from ``conda-forge``

You can read more about environment files in the `conda user guide <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually>`_.

.. note::

    Create a ``yaml`` file somewhere on disk.  You can start with creating the above example ``my_first_environment.yaml`` as a test if you wish.

Now that you have an environment file somewhere on disk, you can recreate the environment that we have specified using conda:

.. code-block:: console

    $ conda env create -f my_first_environment.yaml

Here you are telling ``conda`` to create a new environment using the file (``-f``) ``my_first_environment.yaml`` as the specification. Once the environment has been installed, you should be able to confirm that the environment exists by using the ``info`` subcommand of the ``conda`` tool:

.. code-block:: console

    $ conda info --envs
    # conda environments:
    #
    base                  *  /opt/apps/easybuild/software/lang/Miniconda3/4.4.10
    my_first_environment     /users/klcm500/scratch/conda_environments/envs/my_first_environment


At this point, the environment ``my_first_environment`` has been created, and is ready to be used. Note: the asterisk in the output of ``conda info --envs`` indicates *which* conda environment is currently activated. As you haven't yet activated your new environment, the ``base`` environment (the default environment over which you have no control) is activated.


Using an environment
^^^^^^^^^^^^^^^^^^^^

Once an environment has been created, you can activate it using the ``source activate`` command. This can be seen clearly in the following example:

.. code-block:: console

    $ command -v python
    /opt/apps/easybuild/software/lang/Miniconda3/4.4.10/bin/python

    $ source activate my_first_environment

    (my_first_environment) $ command -v python
    /users/klcm500/scratch/Python/envs/my_first_environment/bin/python

The execution of ``command -v python`` is not necessary, it is just used to illustrate that the Python environment has changed from ``base`` to ``my_first_environment``.

You have now activated the ``my_first_environment`` environment, which changes the Python executable in the ``PATH`` from the default Miniconda Python to the Python from ``my_first_environment``. All of the necessary environment changes have been made such that you can use Python as normal, but with a guarantee of no conflict with other Python installations on the system. Your shell prompt will include the name of the current Conda environment in parentheses to remind you that you are in a specific environment.

If you wish to add more packages into ``my_first_environment``, you can use both conda or pip to install them. You must activate ``my_first_environment`` first, though! Taking ``pytest`` as an example, you first see that it is not available in your environment:

.. code-block:: console

   (my_first_environment) $ python

   Python 3.7.1 | packaged by conda-forge | (default, Mar 13 2019, 12:57:14)
   [GCC 7.3.0] :: Anaconda, Inc. on linux
   Type "help", "copyright", "credits" or "license" for more information.

    >>> import pytest
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'pytest'
    >>>

You can then install it using conda:

.. code-block:: console

    (my_first_environment) $ conda install pytest
    Solving environment: done

    ## Package Plan ##

    environment location: /users/klcm500/scratch/Python/envs/my_first_environment

      added / updated specs:
        - pytest


   The following packages will be downloaded:

        package                    |            build
        ---------------------------|-----------------
        certifi-2019.3.9           |           py37_0         155 KB
        pluggy-0.9.0               |           py37_0          30 KB
        attrs-19.1.0               |             py_0          35 KB
        more-itertools-6.0.0       |           py37_0          89 KB
        pytest-4.3.0               |           py37_0         349 KB
        py-1.8.0                   |           py37_0         140 KB
        atomicwrites-1.3.0         |             py_0           9 KB
        ------------------------------------------------------------
                                               Total:         808 KB

    The following NEW packages will be INSTALLED:

        atomicwrites:    1.3.0-py_0
        attrs:           19.1.0-py_0
        more-itertools:  6.0.0-py37_0
        pluggy:          0.9.0-py37_0
        py:              1.8.0-py37_0
        pytest:          4.3.0-py37_0

    The following packages will be UPDATED:

        certifi:         2019.3.9-py37_0     conda-forge --> 2019.3.9-py37_0
        openssl:         1.1.1b-h14c3975_1   conda-forge --> 1.1.1b-h7b6447c_1

    The following packages will be DOWNGRADED:

        ca-certificates: 2019.3.9-hecc5488_0 conda-forge --> 2019.1.23-0

    Proceed ([y]/n)? y

    Downloading and Extracting Packages
    certifi 2019.3.9: ################################################################## | 100%
    pluggy 0.9.0: ###################################################################### | 100%
    attrs 19.1.0: ###################################################################### | 100%
    more-itertools 6.0.0: ############################################################## | 100%
    pytest 4.3.0: ###################################################################### | 100%
    py 1.8.0: ########################################################################## | 100%
    atomicwrites 1.3.0: ################################################################ | 100%
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done

Here ``conda`` has to download and install some dependencies for the new package pytest, as well as solve some dependency issues that result in a couple of already installed packages needing to be downgraded. Once this process is complete, you can immediately use the new ``pytest`` package in your environment:


.. code-block:: console

    (my_first_environment) $ python

    Python 3.7.1 | packaged by conda-forge | (default, Mar 13 2019, 12:57:14)
    [GCC 7.3.0] :: Anaconda, Inc. on linux
    Type "help", "copyright", "credits" or "license" for more information.

    >>> import pytest
    >>>


If the package that you wanted to install was not available through ``conda install``, you could just have easily installed it using ``pip install`` instead.

Once you are finished using your environment, it can be easily exited using the source deactivate command:

.. code-block:: console

   (my_first_environment) $ source deactivate
   $


You will notice that the first section of the bash prompt - ``(my_first_environment)`` - disappears after the source deactivate command successfully runs. This lets you know that you have left ``my_first_environment``. Sure enough, the Python executable that is in the ``PATH`` is no longer the one from ``my_first_environment``:

.. code-block:: console

   $ command -v python
   /opt/apps/easybuild/software/lang/Miniconda3/4.4.10/bin/python


At this point, we can specify and create virtual environments with ``conda``, we can switch between them, use them, and update them with any necessary new packages.
