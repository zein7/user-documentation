How to view your recently viewed items
======================================

1. Go to your Dashboard

    .. screenshot::
       :server_path: /account/home
       :alt:
       :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0
            
2. See your recently view metadata 

    In the top right corner of your Dashboard you will be able to see your recently viewed metadata items.  
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: a[href="/account/recently_viewed"]
       :crop_element_padding: 0,000,600,0

3. Select "See more" 

    To view more of your recently viewed metadata and additional information regarding the recently viewed metadata items, select "see more".  
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :clicker: a[href="/account/recently_viewed"]
       :crop_element_padding: 0,000,600,0
       
    From here, you will be able to clear your history and see more detail about your recently viewed items.       
       
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0
       
       browser.find_element_by_css_selector('a[href="/account/recently_viewed"]').click()




