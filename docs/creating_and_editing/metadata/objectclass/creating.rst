Creating an Object Class
========================

1. Go to "create metadata" under the Dashboard

.. screenshot::
   :server_path: /create
   :alt: Create items page
   :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
   :crop_element: nav.main.navbar
   :crop_element_padding: 0,000,600,0


2. Scroll down to find the section titled "Just create a single metadata item"

.. screenshot::
   :alt: 
   :crop_element: h2 .fa.fa-plus
   :crop_element_padding: 100,600,100,100

3. Under this section, scroll down to find the section titled "Object Class".

.. screenshot::
   :alt: Create object class link
   :crop_element: td>a[href="/create/aristotle_mdr/objectclass"]:not(.btn)
   :crop_element_padding: 100,800,200,100
   :box: td>a[href="/create/aristotle_mdr/objectclass"]:not(.btn)

Click either the name of the object, or click the "Create" button on the right of the page

.. screenshot::
   :alt: Create object class link
   :crop_element: td>a.btn[href="/create/aristotle_mdr/objectclass"]
   :crop_element_padding: 100,50,100,850
   :clicker: td>a.btn[href="/create/aristotle_mdr/objectclass"]

4. After clicking you will be taken to the first page of the metadata creation process.
Use this page to begin the creation process by entering a name. On this page you can also add an optional description and version. The registry will use this information to find similar items.


.. screenshot::
   :server_path: /create/aristotle_mdr/objectclass
   :alt: Create object class link
   :form_data: [
      {'initial-name': 'Person', 'initial-definition': 'A human being.', '__submit__': False}
      ]

6. After submitting, if similar content was found, this will be shown at the top of the page.

.. screenshot::
   :server_path: /create/aristotle_mdr/objectclass
   :alt: Create object class link
   :form_data: [
      {'initial-name': 'Person', 'initial-definition': 'A human being.', '__submit__': True}
      ]

To continue saving, you will need to select the box marking that you have reviewed these items.

.. screenshot::
   :crop_element: input[name="results-make_new_item"]
   :clicker: input[name="results-make_new_item"]
   :crop_element_padding: 100,450,150,80

If no new content was found, no warning will appear.

.. screenshot::
   :server_path: /create/aristotle_mdr/objectclass
   :alt: Create object class link
   :form_data: [
      {'initial-name': 'Place of Business', 'initial-definition': 'A location conducting commmerce or trade.', '__submit__': True}
      ]

8. Additional references and content can be added to fields under the "Names & References" tab of the editor.

.. screenshot::
   :alt: Create object class link
   :clicker: a[href="#tab_names"]
   :crop_element: a[href="#tab_names"]

   browser.find_element_by_css_selector('a[href="#tab_names"]').click()


9. When done, scroll down and click the "Save" button. Once saved you will be redirected to the page of the new item.

.. screenshot::
   :alt: Create object class link
   :clicker: .fa.fa-save
   :crop_element: .fa.fa-save
   :crop_element_padding: 100,350,150,350
