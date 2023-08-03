Main heading
============

Use a clear line under each heading or other markdown

Subheading
----------

Note: Heading structure is determined only by occurrence order.

Subsubheading
^^^^^^^^^^^^^

Paragraphs
""""""""""

By using different heading `levels` the TOC will produce nested entries, cutting down the default TOC size


Styles
======

**Bold text**
*Italic text*
``Inline literal/code``
:sup:`super`\ Script
:sub:`sub`\ Script

Bullet Lists
============

* Unordered item
* Unordered item

    1. Nested Ordered item
    2. Nested Ordered item

        a. Nested ordered item

* Unordered item

Targets & Links
===============

External Links
--------------

`This is a link, ensure the is a SPACE <https://www.york.ac.uk/etc>`_


Internal Links
--------------

.. _link-target:

:ref:`link text <link-target>`


Code-blocks
===========

.. code-block:: console
    :caption: optional caption appears above the code-block. If there is no caption, there **must** be a clear line before the code.

    The following options are available:
    - Enter the name of the machine you wish to ssh to.
    - Enter 'username@machine' to use a different username.

    Enter York host or service name: viking


Code-blocks will allow syntax highlighting
------------------------------------------

.. code-block:: bash

    echo "Hello World"


.. note::

    This is a note. Notice the clear line above this line.



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

   You can make up your own admonition too.
