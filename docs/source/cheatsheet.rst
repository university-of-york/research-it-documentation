.. include:: global.rst

.. include the global.rst which includes the substitution of `|br|` to html `</br>`

Main heading
============

Use a clear line under each heading at least the length of the text

Subheading
----------

Subsubheading
^^^^^^^^^^^^^

Paragraphs
""""""""""

By using different heading `levels` the TOC will produce nested entries, cutting down the default TOC size


Styles
------

*Italic text*
**Bold text**
``Inline literal/code``
:sup:`super`\ Script
:sub:`sub`\ Script


Bullet Lists
------------

* Unordered item
* Unordered item

    1. Nested Ordered item
    2. Nested Ordered item

        a. Nested ordered item

* Unordered item


Preserve line breaks
--------------------

| These lines are
| broken exactly like in
| the source file.


Targets & Links
---------------

External Links
^^^^^^^^^^^^^^

`This is a link, ensure the is a SPACE <https://www.york.ac.uk/>`_


Internal Links
^^^^^^^^^^^^^^

.. _link-target:

:ref:`link text <link-target>`

Link to an internal page with the page filename minus the ``.rst``

:doc:`link text <getting_started/quickstart>`


Code-blocks
-----------

.. code-block:: console
    :caption: optional caption appears above the code-block. If there is no caption, there **must** be a clear line before the code.
    :emphasize-lines: 3,5
    :linenos:
    :lineno-start: 10
    :name: a label for hyperlink

    The following options are available:
    - Enter the name of the machine you wish to ssh to.
    - Enter 'username@machine' to use a different username.

    Enter York host or service name: viking


.. code-block:: bash

    echo "Hello World"

Quotes
------

.. epigraph::

    User this as a quote from someone.

    -- Joan Doe


Admonitions
-----------

.. Attention:: Directives at large.

.. Caution:: Don't take any wooden nickels.

.. DANGER:: Mad scientist at work!

.. Error:: Does not compute.

.. Hint:: It's bigger than a bread box.

.. Important::
   - Wash behind your ears.
   - Clean up your room.

     - Including the closet.
     - The bathroom too.

       - Take the trash out of the bathroom.
       - Clean the sink.
   - Call your mother.
   - Back up your data.

.. Note:: This is a note.
   Equations within a note:
   :math:`G_{\mu\nu} = 8 \pi G (T_{\mu\nu}  + \rho_\Lambda g_{\mu\nu})`.

.. Tip:: 15% if the service is good.

    +---------+
    | Example |
    +=========+
    | Thing1  |
    +---------+
    | Thing2  |
    +---------+
    | Thing3  |
    +---------+

.. WARNING:: Strong prose may provoke extreme mental exertion.
   Reader discretion is strongly advised.

.. admonition:: And, by the way...

   You can make up your own admonition too. Note the clear line above this one.

Tables
-------

For a basic table you can draw it out in ascii, it's pretty limited though:

.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====


Using a ``.csv`` file makes things a lot easier:

.. csv-table:: Viking breakdown
    :file: assets/data/viking_stats.csv
    :align: center


Simple abbreviations
--------------------

These use the ``title`` html attribute for mouse hover

:abbr:`LIFO (last-in, first-out)`
