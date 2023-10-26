Apptainer (Singularity)
=======================

Apptainer (formally Singularity) allows for running containers on Viking and other HPC. It can run containers built from Docker images, although a conversion is required first. However, due to security issues it is not possible to build containers on Viking itself.  We have detailed below some alternative options. Please see `apptainer.org <https://apptainer.org/docs/user/latest/>`_ for the complete documentation.

To load ``{NAME_APPTAINER}`` on Viking run

.. code-block:: console

    module load {MOD_APPTAINER}


Using the remote builder (recommended)
--------------------------------------

You will need to `create an account <https://cloud.sylabs.io/builder>`_ and then create a ``access token`` for use on Viking. Once your account is set up and you have logged in, click your username in the top right and select ``access tokens``. Give it a name and click ``Create Access Token``. Copy the token and then, on Viking run the following command and then paste the token:

.. code-block:: console

    singularity remote login

.. attention::

    If you don't complete the above step you will receive the following error:

    FATAL:   Unable to submit build job: no authentication token, log in with 'singularity remote login'

..  FIXME: Is it worth including this first option? We seem to recommend remote building later on

There are two ways to remote build.

    1. You can upload or write the recipes on the main page in the web UI
    2. Build remotely on Viking using the ``{NAME_APPTAINER} build`` command

An example of the second approach is shown below, this creates a Hello World image to test your setup is configured correctly.

.. code-block:: console

    {NAME_APPTAINER} build --remote hello-world.simg shub://vsoch/hello-world


.. note::

    Be aware that you only have an **11GB** quota on Sylabs Cloud.


.. attention::

    {NAME_APPTAINER} images are run as **read only**. While this is great for reproducible results, it means that only files outside the image can be edited or created. Be aware that not all software suits this set up.



Example use step by step
------------------------

Here is an example use of building and running a program through ``{NAME_APPTAINER}`` step-by-step. This example is to allow us to use the `DIA-NN <https://github.com/vdemichev/DiaNN>`_ program. I searched `hub.docker.com <https://hub.docker.com/r/proteomicsunitcrg/dia-nn>`_ and found an image with ``dia-nn`` included, this is what we'll use.


.. admonition:: If you haven't already...

    - Create an account on `https://cloud.sylabs.io/builder <https://cloud.sylabs.io/builder>`_, this will allow you to build a container off Viking
    - Create an access token on that site: ``User account > Access Token > Generate`` you can name this anything but ``Viking`` will do


    On Viking, from the command line:

    .. code-block:: console

        $ module load {MOD_APPTAINER}
        $ {NAME_APPTAINER} remote login


    Then paste in the ``access token`` you created earlier. This will allow us to build the image from the Viking command line.


On the Viking command line we build the image. The ``docker://proteomicsunitcrg/dia-nn:latest`` was made by putting ``docker://`` in front of the container ``repository`` and ``tag`` as explained in the `documentation <https://apptainer.org/docs/user/main/docker_and_oci.html#public-containers>`_.

.. code-block:: console

    $ {NAME_APPTAINER} build --remote dia-nn.simg docker://proteomicsunitcrg/dia-nn:latest


This should build the image for you and save it as ``dia-nn.simg`` in your current folder. If all goes well you can run it with the following:

.. code-block:: console
    :caption: for this container we need to use the ``--cleanenv`` option

    $ {NAME_APPTAINER} shell --cleanenv dia-nn.simg


This should get you a ``shell`` session within the container, the program ``diann`` is located in the following directory, here I have it list its version:

.. code-block:: console

    $ /usr/diann/1.8/diann-1.8 --version


It's important to use the ``--cleanenv`` option when running this container to stop it passing the current environment variables to the container.


Installing singularity on your local system
--------------------------------------------

If you are running Linux and would like to install ``Singularity`` locally on your system, ``Singularity`` provide the free, open source `Singularity Community Edition <https://github.com/sylabs/singularity>`_.
If you would like to attempt a local install of ``Singularity``, you can find details in the `INSTALL.md <https://github.com/sylabs/singularity/blob/master/INSTALL.md>`_ file within the ``Singularity`` repository that explains how to install the prerequisites (most notably ``Go``), build, and install the software.

If you do not have access to a Linux system where you can build and install ``Singularity`` but you have administrative privileges on another system, you could look at installing a virtualisation tool such as `VirtualBox <https://www.virtualbox.org/>`_ on which you could run a Linux Virtual Machine (VM) image to install ``Singularity``.

If you have a Mac system, you can also try the beta release of `Singularity Desktop <https://docs.sylabs.io/guides/3.2/user-guide/installation.html#mac>`_ for MacOS.

