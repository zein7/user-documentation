How to create or update a Share Link from your Sandbox
======================================================

1. Go to your Sandbox

    From your Dashboard side panel, select "My Sandbox".
    
    .. screenshot::
        :server_path: /account/home
        :alt:
        :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
        :crop_element: nav.main.navbar
        :box: #user_sidebar a[href="/account/sandbox"]
        :crop_element_padding: 0,000,600,0
        
2. Select "Create Share Link"

    In the top right corner of the page, select the "Create Share Link" button.
    
    .. screenshot::
        :server_path: /account/sandbox
        :alt:
        :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
        :crop_element: nav.main.navbar
        :box: button[class="btn btn-primary pull-right"]
        :crop_element_padding: 0,000,600,0
        
3. Enter emails

    Once you click the "Create Share Link" button, a pop-up modal will appear. You will be able to enter emails for people you want to share your Sandbox content with. 
    
    .. screenshot::
        :server_path: /account/sandbox
        :form_data: [
         {'emails-0':"reggie@aristotle.example.com", '__submit__': False}
         ]
        :alt:
        :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
        :crop_element: nav.main.navbar
        :crop_element_padding: 0,000,600,0
        

        browser.find_element_by_css_selector('button.btn.btn-primary.pull-right').click()
        
        import time
        time.sleep(2)
        
        
    You are only allowed to enter one email address per line, but selecting "Add" will let you add more emails. 
    
    **Only emails with this Registry's credentials will be allowed to access the content from the Share Link.**
    
4. Create or Update the share link

    Once you've entered the emails select "Create" or "Update" to generate or update a Share Link. 
    
    If this is your first time generating a share link, the modal will exit and the link will show up in a blue box at the top of your Sandbox. 
    
    .. screenshot::
        :server_path: /account/sandbox
        :form_data: [
         {'emails-0':"reggie@aristotle.example.com", '__submit__': False}
         ]
        :alt:
        :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
        :crop_element: nav.main.navbar
        :clicker: .modal-content button[type="submit"]
        :crop_element_padding: 0,000,600,0
    
        browser.find_element_by_css_selector('button.btn.btn-primary.pull-right').click()
        
        
        import time
        time.sleep(2)
        
    If you are updating the emails for the share link, once you select "Update" a green box will tell you that you've updated the share permissions.         
        
    .. screenshot::
        :alt:
        :crop_element: nav.main.navbar
        :crop_element_padding: 0,000,600,0
    
        browser.find_element_by_css_selector('.modal-content button[type="submit"]').click()
        
        
        import time
        time.sleep(2)


    
    
