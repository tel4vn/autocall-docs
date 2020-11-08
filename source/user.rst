***********************
HEADER 1
***********************

Header 2
======================

Header 2.1
-----------------------

Header 2.1.1
+++++++++++++++++++++++

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

Header 2.1.2
+++++++++++++++++++++++

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

1. Item 1 initial text.

   a) Item 1a.
   b) Item 1b.

2. a) Item 2a.
   b) Item 2b.

Header 2.2
-----------------------

Header 2.2.1
+++++++++++++++++++++++

danh sach 1
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

danh sach 2
    Definition 2.

    Definition 2.

danh sach 3
	Definition 3.

danh sach 4
	Definition 4.

Header 2.2.2
+++++++++++++++++++++++

:Date: 2001-08-16
:Version: 1
:Authors: - Me
          - Myself
          - I
:Author: Me
:Indentation: Since the field marker may be quite long, the second
   and subsequent lines of the field body do not have to line up
   with the first line, but they must be indented relative to the
   field name marker, and they must line up with each other.
:Parameter: integer
:Copyright: This document has been placed in the public domain.
:Address: 123 Example Ave.
        Example, EX
:Hue: hue example

Header 3
======================

Header 3.1
-----------------------


Header 3.1.1
+++++++++++++++++++++++

.. topic:: Topic English 

   Body of topic.



Header 3.1.2
+++++++++++++++++++++++

Bibliographic fields recognized by the parser are normally checked for RCS [4] keywords and cleaned up [5]. RCS keywords may be entered into source files as "$keyword$", and once stored under RCS or CVS [6], they are expanded to "$keyword: expansion text $". For example, a "Status" field will be transformed to a "status" element:

   :Status: $keyword: expansion text $

| [4]	Revision Control System.
| [5]	RCS keyword processing can be turned off (unimplemented).
| [6]	Concurrent Versions System. CVS uses the same keywords as RCS.

Processed, the "status" element's text will become simply "expansion text". The dollar sign delimiters and leading RCS keyword name are removed.

The RCS keyword processing only kicks in when the field list is in bibliographic context (first non-comment construct in the document, after a document title if there is one).

| These lines are
| broken exactly like in
| the source file.

Header 3.1.2
+++++++++++++++++++++++

-a         Output all.

-b         Output both (this description is
           quite long).

-c arg     Output just arg.

--long     Output all day long.

-p         This option has two paragraphs in the description.
           This is the first.

           This is the second.  Blank lines may be omitted between
           options (as above) or left in (as here and below).

--very-long-option  A VMS-style option.  Note the adjustment for
                    the required two spaces.

--an-even-longer-option
           The description can also start on the next line.

-2, --two  This option has two variants.

-f FILE, --file=FILE  These two options are synonyms; both have
                      arguments.

/V         A VMS/DOS-style option.

Header 3.2
-----------------------

Header 3.2.1
+++++++++++++++++++++++

This is a typical paragraph.  An indented literal block follows.

::

    for a in [5,4,3,2,1]:   # this is program code, shown as-is
        print a
    print "it's..."
    # a literal block continues until the indentation ends

This text has returned to the indentation of the first paragraph,
is outside of the literal block, and is therefore treated as an
ordinary paragraph.


Paragraph:

::

    Literal block

Paragraph: ::

    Literal block

Paragraph::

    Literal block

Header 3.2.2
+++++++++++++++++++++++

This is an ordinary paragraph.

>>> print 'this is a Doctest block'
this is a Doctest block

The following is a literal block::

    >>> This is not recognized as a doctest block by
    reStructuredText.  It *will* be recognized by the doctest
    module, though!


Header 3.2.3
+++++++++++++++++++++++

This is a paragraph that 
contains `https://google.com <https://google.com>`_


This is a paragraph that contains `google link`_.

.. _google link: https://google.com/


Header 3.3
-----------------------

Header 3.3.1
+++++++++++++++++++++++

.. DANGER::
   Beware killer rabbits!

.. note:: This is a note admonition.
   This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.

"To Ma Own Beloved Lassie: A Poem on her 17th Birthday", by
Ewan McTeagle (for Lassie O'Shea):

    .. line-block::

        Lend us a couple of bob till Thursday.
        I'm absolutely skint.
        But I'm expecting a postal order and I can pay you back
            as soon as it comes.
        Love, Ewan.

.. code:: python

  def my_function():
      "just a test"
      print 8/2

.. math::

  α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)

.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai

translate to html ::

  <block_quote classes="epigraph">
    <paragraph>
        No matter where you go, there you are.
    <attribution>
        Buckaroo Banzai

.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.

.. container:: custom

   This paragraph might be rendered in a custom way.

translate to html ::

  <container classes="custom">
    <paragraph>
        This paragraph might be rendered in a custom way.



Header 3.3.2
+++++++++++++++++++++++

.. contents:: Here's a very long Table of
   Contents title for current file only


.. contents:: Table of Contents
   :depth: 2


Header 3.3.3
+++++++++++++++++++++++

.. sidebar:: Optional Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.


Header 3.3.4
+++++++++++++++++++++++

.. class:: special

This is a "special" paragraph.

.. class:: exceptional remarkable

An Exceptional Section
======================

This is an ordinary paragraph.

.. class:: multiple

   First paragraph.

   Second paragraph.

html translate ::

  <paragraph classes="special">
    This is a "special" paragraph.
    <section classes="exceptional remarkable">
        <title>
            An Exceptional Section
        <paragraph>
            This is an ordinary paragraph.
        <paragraph classes="multiple">
            First paragraph.
        <paragraph classes="multiple">
            Second paragraph.

Header 3.4
-----------------------

Header 3.4.1
+++++++++++++++++++++++

.. default-role:: subscript
  
An example of a `default` role.

html translate ::
  
  <paragraph>
    An example of a
    <subscript>
        default
     role.



.. role:: custom

An example of using :custom:`interpreted text`

html translate ::
  
  <paragraph>
    An example of using
    <inline classes="custom">
        interpreted text


.. role:: custom(emphasis)

:custom:`text`

html translate ::
  
  <paragraph>
    <emphasis classes="custom">
        text



.. role:: custom
   :class: special

:custom:`interpreted text`

html translate ::
  
  <paragraph>
    <inline classes="special">
        interpreted text

Header 3.4.2
+++++++++++++++++++++++

.. _my-reference-label:

Section to cross-reference
--------------------------

This is the text of the section.

It refers to the section itself, see :ref:`my-reference-label`.

Header 3.4.3
+++++++++++++++++++++++