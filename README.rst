Aristotle User Documentation
============================

.. contents:: On this page
   :local:

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
 
    Use notes for generic information
 
        .. note::
           Using the API requires having the Aristotle-MDR API extension installed on your registry.
           If you cannot access these screens, check with your registry administrator to check
           if it is installed.


  - Hints (green):

    Use hints to show a user something that might not be obvious but will make doing actions
    quicker or easier.

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
        
       .. attention:: If an edit link doesn't show on your screen, you may not have 
          permission to edit this metadata.

How to include screenshots
--------------------------

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

Alternatively, if it has a class use::

       :clicker: div.row

Or if there is an id::

       :clicker: div#content

For more information see here: https://github.com/LegoStormtroopr/sphinx-selenium-screenshots/

Using Git for Documenters
-------------------------

We have two main branches:

1. Draft
2. Publish

All work goes onto draft and is pulled into publish when we are ready to publish a new edition
of the documentation.

Troubleshooting pages
---------------------

This editor shows RST and the HTML side-by-side, with errors, to help debug fialing pages, or pages that aren't rendering properly - 
http://rst.ninjs.org/

RST Terminology
---------------

Argument
    An extra piece of information that a directive can accept. Arguments can be optional or required::
    
      .. image: image_name.png
         :alt: The alt tag is a named argument. But image_name.png is an unnamed argument.

Directive
    A command that comes after two dots - ``.. image:``

RST
    Restructured Text - the text format we use to build our documentation
