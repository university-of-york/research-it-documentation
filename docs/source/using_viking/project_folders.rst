Project folders
===============

Shared project folders can be created for you on Viking which are a place for your team to easily share files.

You can admin who has ``read-only`` and ``read/write`` access to this folder and who else can also admin the group in the same way. To request a shared project folder please email itsupport@york.ac.uk and let us know the :doc:`project code </getting_started/creating_accounts>` you wish the folder to be associated with and who should be the admin(s).

The shared project folder will:

    - Be named after your project code
    - Be located in Viking's ``/mnt/scratch/projects/`` folder
    - Have no quota limit associated with the folder itself, the contents within count towards their respective owner's quota

As the folders themselves do not have quota limits, you will need to ensure you have enough personal quota space to take into account your files in your own ``scratch`` folder as well as any of your files in the ``shared project folder``. Transferring file ownership to other users will then count towards their quota once transferred.

.. tip::

    If you need your ``scratch`` quota increasing please email itsupport@york.ac.uk.


Manage user access
-------------------

If you are an admin of the shared project folder you can add or remove users to the ``Read-write access``, ``Read-only access`` and ``Administrator access`` groups through `permman.york.ac.uk <https://permman.york.ac.uk/>`_. The ``Administrator access`` group only allows access to this page on permman - not access to the folder on Viking.

To manage the groups, log into `permman.york.ac.uk <https://permman.york.ac.uk/>`_, select ``viking`` from the list and then click the ``Go`` button. You'll see a list of all the project folders you can manage. Select the desired folder from the list and click ``Edit access to folder``. You'll be presented with a screen similar to the one below and from here you can add and remove users from the three groups:

.. hint::

    Changes made on the ``permman`` page are reflected on Viking three times a day, so there will be some delay for changes made and may take up to 24hrs to take effect.

.. image:: /assets/img/permman.png

.. hint::

    You can only add valid Viking user accounts on this page. Groups also cannot be added, only user accounts. To check if someone has a Viking account use the ``id`` command on Viking for example ``id abc123``, where ``abc123`` is the username. To create an account on Viking please see :doc:`creating an account </getting_started/creating_accounts>`.


Sub folders
-----------

The above will only allow you to add or remove access to the main shared project folder. You can manually create subfolders with the ``mkdir`` command on Viking.

If you wish to create sub folders with restricted access you can use the `chmod <https://linuxhint.com/linux_chmod_command_tutorial_beginners/>`_ or `setfacl <https://www.geeksforgeeks.org/linux-setfacl-command-with-example/>`_ commands to set the permissions to those subfolders if you are familiar using those commands.
