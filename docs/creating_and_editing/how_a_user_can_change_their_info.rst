How a User can Change Their Information
=======================================

Go to "My Dashboard" and in the left side menu, and click "My Profile".

.. screenshot::
   :server_path: /account/home
   :alt:
   :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
   :crop_element: a[href="/account/profile"]
   :clicker: a[href="/account/profile"]

This will take you to your profile page.

.. screenshot::
   :server_path: /account/profile

From your profile page, select "Edit Profile" in the actions list

.. screenshot::
   :alt:
   :crop_element: div.list-group
   :clicker: div.list-group a[href="/account/edit"]

This lets the user change their account details, like their name and email address.

.. screenshot::
   :server_path: /account/edit
   :alt:


How to change your password
===========================

From your profile page, select "Change Password" in the actions list

.. screenshot::
   :server_path: /account/profile
   :crop_element: div.list-group
   :clicker: div.list-group a[href="/account/password/change"]
   
The user can then change their password.

.. screenshot::
   :server_path: /account/password/change
   :crop_element: div[id="content"]
   :crop_element_padding: 100,-200,0,0
