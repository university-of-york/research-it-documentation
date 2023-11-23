VSCode
======

``VSCode`` is a modern text editor from Microsoft. It's possible to use many extensions with it to extend its capabilities but here we'll explain how to use it to connect to Viking over ``ssh`` and allow you to remotely edit text files, which can be very handy.


    1. Install `VSCode <https://code.visualstudio.com/>`_ for your operating system
    2. Follow the instructions to install the `Remote - SSH <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh>`_ extension in VSCode
    3. Follow the instructions to `getting started <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh#getting-started>`_ to connect to viking, the address is ``viking.york.ac.uk``
    4. Enter your password when prompted and you should soon be connected and be able to edit and save files through VSCode.

.. tip::

    ``Ctrl + ``` (backtick) Opens a terminal in ``VSCode``


.. tip::

    If at some point VSCode refuses to connect and it's not obvious why, sometimes the files it installs on Viking have become corrupted. You can log into Viking in your usual way without VSCode, and delete the following directory ``~/.vscode-server``. The next time VSCode connects to Viking it will reinstall the files and hopefully will fix the problem.
