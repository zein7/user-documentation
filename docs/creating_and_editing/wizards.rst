Using wizards to create metadata
================================

To get to the creation wizards, go to "create metadata" on your dashboard side panel, or the creation tool in the header bar and select "see all..."

Data element and data element concept wizards
----------------------------------------------

Wizards help make metadata creation and reuse of metadata items easier. Using these wizards, you will be stepped through creating either a Data Element, and within the wizard you will create an object class, property, and value domain. Or, you can select to create a Data Element Concept, where you will create an object class and a property.

.. screenshot:: 
   :server_path: /create
   :login: {'url': '/login', "username": "vicky", "password": "Viewer"}
   :crop_element: ul[class="list-group"]
   :crop_element_padding: (200,50,10,50)
   
This is the form you will see when selecting to create a new data element

.. screenshot:: 
   :server_path: /create/wizard/aristotle_mdr/dataelement
   :login: {'url': '/login', "username": "vicky", "password": "Viewer"}

Single item creation wizards
----------------------------

These wizards are useful if you know you want to create just one item

.. screenshot:: 
   :server_path: /create
   :login: {'url': '/login', "username": "vicky", "password": "Viewer"}
   :crop_element: div[class="container admin-wrap"]
   :crop_element_padding: (-420,50,10,50)
   
This is the form you will see when selecting to create an object class   
   
.. screenshot:: 
   :server_path: /create/aristotle_mdr/objectclass
   :alt: A basic search screen
   :login: {'url': '/login', "username": "vicky", "password": "Viewer"}
   :form_data: [
      {'initial-name': 'Person', 'initial-definition': 'A human being.', '__submit__': False}  
      ]
      
Because reuse is important, each wizard will search for the name of your item and give you results if there are any matching or similar to your item      
        
.. screenshot:: 
   :form_data: [
      {'initial-name': 'Person', 'initial-definition': 'A human being.', '__submit__': True},
      ]
      
   import time
   time.sleep(2)
   
