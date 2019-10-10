How to change your password
===========================

.. attention:: This help page is for changing your password while already logged into the system
  If you have forgotten your password please use the "forgot password" on the login page of the system,
  it will help you step through retreiving your forgotten password. 

1. Go to "My profile" on the Dashboard side panel

    .. screenshot::
       :server_path: /account/home
       :alt:
       :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
       :crop_element: nav.main.navbar
       :box: a[href="/account/profile"]
       :crop_element_padding: 0,000,600,0
            
2. Select "change password"

    Under "Actions" on you profile page.
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: a.list-group-item[href="/account/password/change"]
       :crop_element_padding: 0,000,600,0
       
       browser.find_element_by_css_selector('a[href="/account/profile"]').click()

3. Change your password

    Type in your current password and the new password twice and select "change my password" to save your new password. 
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0
       
       browser.find_element_by_css_selector('a.list-group-item[href="/account/password/change"]').click()    





