Aristotle User Documentation
============================

.. contents:: On this page
   :local:

Previewing the registry
-----------------------

A preview registry is available at https://user-doc-2.herokuapp.com. This site is rebuild everytime a change is made to this code and documentation.

User accounts for the site are available in this file: https://github.com/aristotle-mdr/user-documentation/blob/draft/server/fixtures/test_metadata.json

Style guide
-----------

* Keep pages short - cover one topic, and have lots of links to other pages.

* Titles (and subtitles) can be styled with symbols like this::

    My heading
    ==========
    
    My subheading
    -------------
    
    My deeper subheading
    ++++++++++++++++++++
    
    An even deeper one (but this is getting too deep)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* If there are more than a few headings on the page, insert a table
    of contents for the page at the top of the page with the following ::

      .. contents:: On this page
         :local:
    

* Use attention boxes to help users understand the documentation:

  - Notes (blue):
 
    Use notes for generic information::
 
        .. note::
           Using the API requires having the Aristotle-MDR API extension installed on your registry.
           If you cannot access these screens, check with your registry administrator to check
           if it is installed.


  - Hints (green):

    Use hints to show a user something that might not be obvious but will make doing actions
    quicker or easier.::

        .. hint::
           You can access the quicksearch bar by hitting 'Alt+Q' on Windows or 'Cmd+Q'
           on Mac.

  - Attention (orange):
    
    Use attention boxes to explain why the screen shot might look
    different to the users screen. This includes 
    
    For example::
   
   
       .. attention:: If an edit link doesn't show on your screen, you may not have 
          permission to edit this metadata.

  - Warning (red):

    Let the user know if they are about to do something that they might not want or can't
    be undone, like deleting things, making things that should be private public, etc...

    Like so::
        
       .. warning:: If an edit link doesn't show on your screen, you may not have 
          permission to edit this metadata.

Inserting links
---------------

Link to another part of the documentation
+++++++++++++++++++++++++++++++++++++++++

A link to another section can be added with the ``:doc`` directive, in side text::
 
   For more help see the chapter :doc:`/user_help/index`

If a file ``user_help/index.rst`` exists, then a link will be added, with the text of the title of that page added in. This means, that if the title changes the link will too.

If a custom text for the link is needed, use angle brackets (``<``  and ``>``) around the link with the custom text before hand.::

    :doc:`my custom text </user_help/index>`
 
Link to an external webpage
+++++++++++++++++++++++++++

When a link to an external page is needed, we stick to using `External hyperlinks`_ only as if/when we make a print version of the documentation, links in this form can be display with footnotes easier.

* If the link text is a single word, adding an underscore straight makes it a link: ``link_``.
* If the link text is multiple words, add backticks around the words, anding an underscore makes it a link: ```a longer link`_``.

For example::

      External hyperlinks, like Python_ or `Aristotle Metadata Registry`_.

      .. _Python: http://www.python.org/
      .. _Aristotle Metadata Registry: http://www.aristotlemetadata.com

.. _External Hyperlinks: http://docutils.sourceforge.net/docs/user/rst/quickref.html#external-hyperlink-targets


Adding images
-------------

How to include normal images
++++++++++++++++++++++++++++

Sphinx and RST allow images to be inserted using the following directive.::

       .. image:: /_static/aristotle_square_small.png
          :alt: The Aristotle-MDR logo
          :align: right

The image path (the first unnamed argument), needs to be relative to the `docs directory`_, and most images will be underneath ``_static`` directory.

.. _docs directory: https://github.com/aristotle-mdr/user-documentation/tree/draft/docs

How to include screenshots
++++++++++++++++++++++++++

Where ever a screen shot is necessary insert a screenshot directive like this::

    .. screenshot::
       :server_path: /        <- this it the url of the page to insert into the documentation
       :alt: alternate text   <- alt tag for the inserted image
       :login: {'url': '/login', "username": "vicky", "password": "Viewer"}
       :alt: alternate text   <- alt tag for the inserted image

When the documentation is built, the screenshot will be generate from a test server.
Always include a short alt tag for images and screenshots to explain them.

For pages that need a user to be logged in to be logged, insert a ``:login:`` argument

To put a circle 'clicker' over a link you can use::

    .. screenshot::
       :server_path: /
       :clicker: a[href="/account/roles"]

Alternatively, if it has a class you can use::

       :clicker: div.row

Or if there is an id::

       :clicker: div#content

For more information on cropping or making marks on screenshots see here: https://github.com/LegoStormtroopr/sphinx-selenium-screenshots/

Inserting raw HTML
------------------

Where possible, all help text should be in RST format, but when migrating content in, if it is easier in some cases to paste in plain html, it can be done like this::

    .. raw:: html
        <p> This will be rendered as <b>bold text</b> in a paragraph!!</p>

Branches for draft and publishing
---------------------------------

We have two main branches:

1. Draft - this is the working branch, and may have incomplete copies of content in, when ready it can be previewed at https://aristotle-mdr.github.io/user-documentation/
2. Publish - this is the final documentation branch, when published it is available at https://aristotle-mdr.github.io/published-documentation/

All work goes onto draft and is pulled into publish when we are ready to publish a new edition
of the documentation.

Troubleshooting pages
---------------------

If pages aren't updating, review the `publishing tool`_, it should show the most recent build and there should be lots of green ticks. If there are red crosses, the build failed. Skip to the bottom of the page and it will tell you how, or why, it failed. - 


We have a `live updating editor`_  that shows RST and the HTML side-by-side, with errors, to help debug failing pages, or pages that aren't rendering properly.

There is a `server specifically for documentation purposes`_ that is rebuilt with
every change. Logins for users and their credentials are in the
`server fixtures`_.

.. _publishing tool: https://travis-ci.org/aristotle-mdr/user-documentation/
.. _live updating editor: https://aristotle-user-doc.herokuapp.com/fafl/
.. _server specifically for documentation purposes: https://aristotle-user-doc.herokuapp.com
.. _server fixtures: https://github.com/aristotle-mdr/user-documentation/blob/draft/server/fixtures/test_metadata.json

Glossary of terms
-----------------

If a term isn't here, make an issue and it can be added in.

Argument
    An extra piece of information that a directive can accept. Arguments can be optional or required::
    
      .. image: image_name.png
         :alt: The alt tag is a named argument. But image_name.png is an unnamed argument.

Directive
    A command that comes after two dots - ``.. image:``

RST
    Restructured Text - the text format we use to build our documentation
