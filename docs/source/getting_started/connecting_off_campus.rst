.. _connecting-off-campus:

Connecting to Viking off campus
===============================

Viking has been configured to only allow connections from the University network. Therefore, in order to access Viking off-campus, you must first connect to either the VPN service, or create an ``ssh`` tunnel. These re-route your traffic through the University network allowing you to connect to Viking as if you were on campus.

Using the VPN
-------------

Please see the main IT Services page on using the VPN found `here <https://www.york.ac.uk/it-services/services/vpn/>`_.


SSH gateway
-----------

The University also provides an `SSH gateway service <https://www.york.ac.uk/it-services/services/ssh/>`_ that can be used to allow off-campus access to Viking, as an alternative to the VPN. To use this method, ``ssh`` to ``ssh.york.ac.uk`` (substituting your username for ``abc123``):

.. code-block:: console

    $ ssh abc123@ssh.york.ac.uk

Once you have entered your password and gone through the 2FA (two-factor authentication), you should then see the following message asking which machine you wish to connect to. Simply enter ``viking`` and press ``Enter``.

.. code-block:: console

    The following options are available:
    - Enter the name of the machine you wish to ssh to.
    - Enter 'username@machine' to use a different username.

    Enter York host or service name: viking


Jump hosting via the SSH gateway
--------------------------------

To avoid manual entering the hostname when using the SSH gateway, it's also possible to directly connect to Viking by "jump hosting":

.. code-block:: console

    ssh -J abc123@ssh.york.ac.uk viking

.. hint::

    You will still need to enter your password, and then complete the 2FA

.. note::

    If you're using a personal device you should specify your IT Services username before the 'viking' address, for example:

    .. code-block:: console

        ssh -J abc123@ssh.york.ac.uk abc123@viking
