How to Add a Workgroup
======================

.. note:: You have to be an Administrator to add a workgroup

Go to "Administrator Tools" at the bottom of the Dashboard side menu

.. screenshot::
   :server_path: /account/admin
   :alt: 
   :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
   :crop_element: div#dashboard-nav a[href="/account/admin"]
   
Select "add workgroup"

.. screenshot::
   :server_path: /account/admin
   :alt: 
   :crop_element: div#content a[href="/workgroups/create"]
   
You will then be asked to give the new workgroup a name, which helps members identify the workgroups they are in,
and a definition for the workgroup, which let's people know what the role of the workgroup is.Once done, click "create new workgroup" to finish creating your new workgroup, you will be taken to the new workgroups page.

.. screenshot::
   :server_path: /workgroups/create
   :box: div.admin-wrap button[type="Submit"]
   :form_data: [
      {'name': 'Test Workgroup 1', 'definition': 'Test workgroup to show examples', '__submit__': False},
      ]
     
   import time
   time.sleep(5)
   
   
Once you create the new workgroup, you will be able to add members to the workgroup, see a list of items that have been assigned to the workgroup, and view conversations that take place between members of the workgroup.   
   
.. screenshot::
   :server_path: /workgroups/create
   :form_data: [
      {'name': 'Test Workgroup 1', 'definition': 'Test workgroup to show examples', '__submit__': True},
      ]
      
   import time
   time.sleep(5)
   
