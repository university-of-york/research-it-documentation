Apptainer (Singularity)
=======================

Apptainer (formally Singularity), is available on Viking.  Due to security issues it is not possible to build containers on Viking.  We have detailed below some alternative options. Please see `apptainer.org <https://apptainer.org/docs/user/latest/>`_ for the complete documentation.

To load ``{NAME_APPTAINER}`` on Viking run

.. code-block:: console

    module load {MOD_APPTAINER}


Using the remote Builder (recommended)
--------------------------------------

You will need to `create an account <https://cloud.sylabs.io/builder>`_ and then create a ``access token`` for use on Viking. Once you're account is set up and you have logged in, click your username in the top right and select ``access tokens``. Give it a name and click ``Create Access Token``. Copy the token and then, on Viking run the following command and then paste the token:

.. code-block:: console

    singularity remote login

.. attention::

    If you don't complete the above step you will receive the following error:

    FATAL:   Unable to submit build job: no authentication token, log in with 'singularity remote login'

There are two ways to remote build.  You can upload or write the recipes on the main page.  Or you can build remotely using the following commands on Viking. Below we can use an example to test the remote builder.

.. code-block:: console

    {NAME_APPTAINER} build --remote hello-world.simg shub://vsoch/hello-world


.. note::

    Be aware that you only have an **11GB** quota on Sylabs Cloud.


Installing Singularity on Your Local System
--------------------------------------------

If you are running Linux and would like to install ``Singularity`` locally on your system, ``Singularity`` provide the free, open source `Singularity Community Edition <https://github.com/sylabs/singularity>`_. You will need to install various dependencies on your system and then build ``Singularity`` from source code.

If you have Linux systems knowledge and would like to attempt a local install of ``Singularity``, you can find details in the `INSTALL.md <https://github.com/sylabs/singularity/blob/master/INSTALL.md>`_ file within the ``Singularity`` repository that explains how to install the prerequisites and build and install the software. ``Singularity`` is written in the `Go <https://golang.org/>`_ programming language and ``Go`` is the main dependency that you'll need to install on your system. The process of installing ``Go`` and any other requirements is detailed in the `INSTALL.md <https://github.com/sylabs/singularity/blob/master/INSTALL.md>`_ file.

If you do not have access to a Linux system where you can build and install ``Singularity`` but you have administrative privileges on another system, you could look at installing a virtualisation tool such as `VirtualBox <https://www.virtualbox.org/>`_ on which you could run a Linux Virtual Machine (VM) image. Within the Linux VM image, you will be able to install ``Singularity``.

If you have a Mac system, you can also try the beta release of `Singularity Desktop <https://docs.sylabs.io/guides/3.2/user-guide/installation.html#mac>`_ for MacOS.
