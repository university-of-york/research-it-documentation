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

If you're using Linux or MacOS to connect to Viking then running ``ssh-keygen -R viking.york.ac.uk`` will remove the old ``ssh fingerprint`` stored in your ``~/.ssh/known_hosts`` file. Connecting again with ``ssh abc123@viking.york.ac.uk`` (with your username in place of ``abc123``) should give you the option to check the new ``ssh fingerprint``, confirm it matches one of the above, and if so, accept the new ``ssh fingerprint``. You should then be connected and no longer receive the warnings about the ``ssh fingerprint``.


I cannot connect when using the eduroam WiFi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently this is being worked on and we hope to have a solution soon. In the meantime please use a wired connection on campus or first connect to the `University VPN <https://www.york.ac.uk/it-services/services/vpn/>`_.

