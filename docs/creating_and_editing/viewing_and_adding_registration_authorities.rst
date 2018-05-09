How to View and Add Registration Authorities
=============================================

.. note:: This can only be done if you are an Administrator

To get started, click on Administrator Tools at the bottom of the left menu

.. screenshot:: 
   :server_path: /account/home
   :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
   :clicker: #dashboard-nav a[href='/account/admin']
   

Click the Add Registration Authority link

.. screenshot:: 
   :server_path: /account/admin
   :clicker: a[href="/registrationauthority/create"] 
   
   
Type in the name of the new Registration Authority and a definition for the new registration authority. After putting in a name and a definition, select "Create new Registration Authority" and you will be taken to the newly created registration authority page. 

.. screenshot:: 
   :server_path: /registrationauthority/create
   :box: div.admin-wrap button[type="Submit"]
   :form_data: [
      {'name': 'Test RA 1', 'definition': 'Test RA to show as example', '__submit__': False},
      ]
   
   import time
   time.sleep(2)   
   
From here, you can change when metadata items are publicly viewable and locked, by selecting "edit"    
   
.. screenshot:: 
   :server_path: /registrationauthority/create
   :box: div.admin-wrap button[type="Submit"]
   :form_data: [
      {'name': 'Test RA 1', 'definition': 'Test RA to show as example', '__submit__': True},
      ]
   
   import time
   time.sleep(2)
   
