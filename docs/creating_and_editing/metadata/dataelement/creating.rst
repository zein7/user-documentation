Creating a Data Element
=======================

1. Go to "create metadata" under the Dashboard

    .. screenshot::
      :server_path: /create
      :alt: 
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav.main.navbar
      :crop_element_padding: 0,000,600,0

2. Scroll to the section titled "Just create a single metadata item"

    .. screenshot::
       :alt: 
       :crop_element: h2 .fa.fa-plus
       :crop_element_padding: 100,600,100,100

3. Under this section, scroll down to find the section titled "Data Element"
   
    This will be under the section titled **Aristotle Metadata Registry**.

    Other metadata types will be available and grouped by their add-on.

    .. screenshot::
       :alt: 
       :crop_element: td>a[href="/create/aristotle_mdr/dataelement"]:not(.btn)
       :crop_element_padding: 100,800,200,100
       :box: td>a[href="/create/aristotle_mdr/dataelement"]:not(.btn)

    Click either the name of the object you wish to create, or click the "Create" button on the right of the page

    .. screenshot::
       :alt: 
       :crop_element: td>a.btn[href="/create/aristotle_mdr/dataelement"]
       :crop_element_padding: 100,50,100,850
       :clicker: td>a.btn[href="/create/aristotle_mdr/dataelement"]

    After clicking you will be taken to the first page of the metadata creation process

4. Fill search fields and submit

    Use the first page to begin the creation process by entering the name of the metadata you are creating.
    **At this step only the name is required**, but on this page you can also add an optional description and version.
    The registry will use this information to find similar items.

    .. screenshot::
       :server_path: /create/aristotle_mdr/dataelement
       :alt: 
       :form_data: [
          {'initial-name': 'Employee - date of employment', 'initial-definition': '', '__submit__': False}
          ]

5. Fill in metadata description

    After submitting, if similar content was found, this will be shown at the top of the page

    .. screenshot::
       :server_path: /create/aristotle_mdr/dataelement
       :alt: 
       :form_data: [
          {'initial-name': 'Employee - date of employment', 'initial-definition': '', '__submit__': True}
          ]

    To continue saving, you will need to select the box marking that you have reviewed these items.

    .. screenshot::
       :crop_element: input[name="results-make_new_item"]
       :clicker: input[name="results-make_new_item"]
       :crop_element_padding: 100,450,150,80

    If no new content was found, no warning will appear.

    .. screenshot::
       :server_path: /create/aristotle_mdr/dataelement
       :alt: 
       :form_data: [
          {'initial-name': 'Person - Name, Text', 'initial-definition': 'The full name of a human being stored as text..', '__submit__': True}
          ]

6. Add extra context

    Additional fields for recording references and extra content can be added to fields under the "Names & References" tab of the editor.

    .. screenshot::
       :alt: 
       :clicker: a[href="#tab_names"]
       :crop_element: a[href="#tab_names"]

       browser.find_element_by_css_selector('a[href="#tab_names"]').click()



7. Add extra components

    Some metadata types have special fields for recording context specific information and links to other metadata in the registry.


    .. screenshot::
       :alt: 
       :clicker: a[href="#tab_components"]
       :crop_element: a[href="#tab_components"]

       browser.find_element_by_css_selector('a[href="#tab_components"]').click()

    From this section, you can can add a **Value Domain** and a **Data Element Concept** from the drop down search boxes.

    .. screenshot::
       :alt: 
       :crop_element: #tab_components

8.  Click "Save" to complete

     When done, scroll down and click the "Save" button.
     Once saved you will be redirected to the page of the new item.

     .. screenshot::
        :alt: 
        :clicker: .fa.fa-save
        :crop_element: .fa.fa-save
        :crop_element_padding: 100,350,150,350
