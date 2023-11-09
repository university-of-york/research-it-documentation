.. include:: /global.rst

.. include the global.rst which includes the substitution of `|br|` to html `</br>`

Template Heading
================

Intro...

.. this is comment

Sub heading
-------------

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

.. admonition:: Custom notice box

   ``term`` this is a technical word

.. _anchor:

Sub sub heading
^^^^^^^^^^^^^^^

Lorem Ipsum has been the industry's standard ``dummy`` text ever since the ``1500s``, when an unknown printer took a galley of type and scrambled it to make a type specimen book.

.. code-block:: console
    :caption: this is a caption
    :emphasize-lines: 2,3
    :linenos:

    $ mkdir new_project
    $ cd new_project
    $ python3 -m venv .venv


It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

.. Warning::

    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.


Sub sub sub heading
"""""""""""""""""""

- `Link to outside page <http://www.google.com>`_
- :doc:`Internal page link </getting_started/backing_up>`
- :ref:`link to anchor <anchor>`


.. tip::

    This page then just needs to be referenced in the `index.rst` and |br| saved in the appropriate folder.

.. add a |br| to force a line break

