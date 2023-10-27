.. include:: /global.rst

Frequently asked questions
==========================

Here is a list of frequently asked questions about Viking, if you have any suggestions to add to this list please email itsupport@york.ac.uk


When I try to connect to Viking I get a warning that the ``fingerprint`` has changed, should I accept this?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you connected to the old Viking then your computer may have stored the old ``ssh fingerprint`` of the login nodes. As the new Viking has new login nodes it has new ssh fingerprints. Please check the fingerprints below and ensure they match what is being displayed in the terminal login screen:

.. code-block:: console

   SHA256:e6QUl1pE1RK55unuALoNDXaEvJLcam4LJo6P07nbGcs (RSA)
   SHA256:jn1KdPw+M9iws+uEwsnuqC5NVph4eNT095m22RFz4Mw (ECDSA)
   SHA256:TztJ/bGgPiK6bIGfQqRQnxfg/nVhw978T6kyy9HhJTQ (ED25519)


I cannot connect when using the eduroam WiFi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently this is being worked on and we hope to have a solution soon. In the meantime please use a wired connection on campus or use the :doc:`University VPN </getting_started/connecting_off_campus>`.


GitHub wont let me clone a repo using ssh
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default the ``IdentityFile`` used for all hosts is set to ``~/.ssh/id_alcescluster`` on Viking. This setting is found in your ``~/.ssh/config`` file which by default should looks like this:

.. code-block::

   Host *
     IdentityFile /users/nd996/.ssh/id_alcescluster
     StrictHostKeyChecking  no

You can generate a new ssh key with the following command:

.. code-block:: console
   :caption: inset your own email address in place of "your_email@example.com"

   $ ssh-keygen -t ed25519 -C "your_email@example.com"

And then add the following to your ``~/.ssh/config`` file:

.. code-block:: console

   Host github.com
     User git
     IdentityFile ~/.ssh/id_ed25519

You'll need to add this ssh key to your GitHub account by going to GitHub > Settings > SSH anf GPG Keys > Add SSH Key

Alternatively you can follow the guide on GitHub and run an `ssh-agent <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_
