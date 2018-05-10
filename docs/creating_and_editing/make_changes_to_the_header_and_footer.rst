How to Make Changes to the Header and Footer 
============================================

.. note:: Only Administrators have access to the Aristotle Cloud Dashboard, to change the look of the header and 
          footer in the registry

Once logged into the registry, navigate to your Dashboard

.. screenshot::
   :server_path: /account/home
   :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}

On your Dashboard, go over to your side panel and select "Aristotle Cloud Dashboard" which is located at the bottom of the panel

.. screenshot::
   :server_path: /account/home
   :crop_element: nav[id="user_sidebar"]
   :clicker: a[href="/account/cloud"]
   
You will be taken to a page that shows your current plan and task histories. To edit the look of the header and footer select "view registry settings" at the top of the page

.. screenshot::
   :server_path: /account/cloud
   :clicker: a[href="/account/cloud/settings"]

On this page, you will be able to change the "visual settings" of the header and footer. This section let's you put in hex color codes (ex:"#0032FF"), or simple color names (ex:"blue"). You can even change the logo that sits in the upper left hand corner of the registry.

.. screenshot::
   :server_path: /account/cloud/settings
   :crop_element: div[data-schemapath="root.visual"]
   
   import time
   time.sleep(3)
   
You will also be able to edit additional "registry settings".

.. screenshot::
   :server_path: /account/cloud/settings
   :crop_element: div[data-schemapath="root.registry"]
   
   import time
   time.sleep(4)
   
After you make your changes, make sure to save changes at the bottom of the page. 

.. screenshot::
   :crop_element: form[method="post"] 
   :crop_element_padding: -2200,-550,100,100

   import time
   time.sleep(4)
   
   
   
