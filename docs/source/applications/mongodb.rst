MongoDB
=======

``MongoDB`` can be loaded using the following command:

.. code-block:: console

    $ module load {MOD_MONGODB}

When using ``MongoDB``, you have to explicitly state the location of the database or ``mongod`` will error out as shown in the first option for ``mongod`` below. If you are using a unix socket you should also specify it's location, shown in the second option for ``mongod`` below.

.. code-block:: console

    $ mongod --dbpath $HOME/scratch/mongod/db --unixSocketPrefix $HOME/scratch/mongod


