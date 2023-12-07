Apptainer (Singularity)
=======================

Apptainer (formally Singularity) allows for running containers on Viking and other HPCs. It can run containers built from Docker images, although a conversion is required first and we can now build the converted images on Viking directly. Please see `apptainer.org <https://apptainer.org/docs/user/latest/>`_ for the complete documentation.

To load ``apptainer`` on Viking run

.. code-block:: console

    module load {MOD_APPTAINER}


Build a container
-----------------

It's possible to build the containers on Viking directly, here we will give a very simple example where we build and then run a container from Docker Hub, more information can be found in the `apptainer docs <https://apptainer.org/docs/user/main/docker_and_oci.html>`_.

.. code-block:: console

    $ module load {MOD_APPTAINER}
    $ apptainer build lolcow.sif docker://sylabsio/lolcow:latest
    $ apptainer run lolcow.sif
     _____________________________
    < Mon Dec 25 09:00:00 GMT 2023 >
     -----------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||


.. important::

    ``apptainer`` images are run as **read only**. While this is great for reproducible results, it means that only files outside the image can be edited or created. Be aware that not all software suits this set up.


Example use step by step
------------------------

Here is an example use of building and running a program through ``apptainer`` step-by-step. This example is to allow us to use the `DIA-NN <https://github.com/vdemichev/DiaNN>`_ program. I searched `hub.docker.com <https://hub.docker.com/r/proteomicsunitcrg/dia-nn>`_ and found an image with ``dia-nn`` included, this is what we'll use.

On Viking, from the command line:

    .. code-block:: console

        $ module load {MOD_APPTAINER}

On the Viking command line we build the image. The ``docker://proteomicsunitcrg/dia-nn:latest`` was made by putting ``docker://`` in front of the container ``repository`` and ``tag`` as explained in the `documentation <https://apptainer.org/docs/user/main/docker_and_oci.html#public-containers>`_.

.. code-block:: console

    $ apptainer build dia-nn.sif docker://proteomicsunitcrg/dia-nn:latest


This should build the image for you and save it as ``dia-nn.sif`` in your current folder. If all goes well you can run it with the following:

.. code-block:: console
    :caption: for this container we need to use the ``--cleanenv`` option

    $ apptainer shell --cleanenv dia-nn.sif


This should get you a ``shell`` session within the container, the program ``diann`` is located in the following directory, here I have it list its version:

.. code-block:: console

    $ /usr/diann/1.8/diann-1.8 --version


In this case I used the ``--cleanenv`` option when running this container to stop it passing the current environment variables to the container.


Installing singularity on your local system
--------------------------------------------

If you are running Linux and would like to install ``Singularity`` locally on your system, ``Singularity`` provide the free, open source `Singularity Community Edition <https://github.com/sylabs/singularity>`_.
If you would like to attempt a local install of ``Singularity``, you can find details in the `INSTALL.md <https://github.com/sylabs/singularity/blob/master/INSTALL.md>`_ file within the ``Singularity`` repository that explains how to install the prerequisites (most notably ``Go``), build, and install the software.

If you do not have access to a Linux system where you can build and install ``Singularity`` but you have administrative privileges on another system, you could look at installing a virtualisation tool such as `VirtualBox <https://www.virtualbox.org/>`_ on which you could run a Linux Virtual Machine (VM) image to install ``Singularity``.

If you have a Mac system, you can also try the beta release of `Singularity Desktop <https://docs.sylabs.io/guides/3.2/user-guide/installation.html#mac>`_ for MacOS.

