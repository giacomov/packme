*************************
This is a document title
*************************

Here is a quick and dirty cheat sheet for some common stuff you want
to do in sphinx and ReST.

You use inline markup to make text *italics*, **bold**,
or ``monotype``.

New lines in the rst code do not matter unless they are double
(in which case a new paragraph is opened).

You can represent code blocks fairly easily::

.. code-block:: python

   import numpy as np
   x = np.random.rand(12)

This is how you create the document structure:

This is a section title
============================================

This is a subsection title
---------------------------

This is how you reference other sections in the same
document:

.. _my-label:

Section to refer to
====================

I am referencing :ref:`my-label`.

Referring to other methods/functions
=====================================

To refer to a method of the same class::

    :py:meth:`.[method-name]`

Of another class::

    :py:meth:`[ClassName].[method_name]`


To refer to methods::

    :py:attr:`[attr_name]`
    :py:attr:`[ClassName].[attr_name]`

To refer to another module::

    :py:mod:`[module name]`

To refer to a function:

    :py:func:`[function name]`

.. _making-a-list:

Making a list
=============

It is easy to make lists in rest

Bullet points
-------------

This is a subsection making bullet points

* point A

* point B

* point C


Enumerated points
------------------

This is a subsection making numbered points

#. point A

#. point B

#. point C


Making a table
==============

This shows you how to make a table -- if you only want to make a list see :ref:`making-a-list`.

==================   ============
Name                 Age
==================   ============
John D Hunter        40
Cast of Thousands    41
And Still More       42
==================   ============


Making links
============

It is easy to make a link to `yahoo <http://yahoo.com>`_ or another
document.
