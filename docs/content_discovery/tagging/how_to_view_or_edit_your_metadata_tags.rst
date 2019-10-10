How to view/edit your metadata tags
===================================

1. Go to "Favourites and Tags" on your Dashboard side panel

    .. screenshot::
       :server_path: /account/home
       :alt:
       :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
       :crop_element: nav.main.navbar
       :clicker: a[href="/favourites/savedItems"]
       :crop_element_padding: 0,000,600,0
       
    This is your Favourites and Tags page
    
    .. screenshot::
       :server_path: /favourites/savedItems
       :alt:
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0    
        
2. Select "view all tags"  

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: a[href="/favourites/allTag"]
       :crop_element_padding: 0,000,600,0
       
    You will be able to see all the tags you've created within the system.
       
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0  
       
       browser.find_element_by_css_selector('a[href="/favourites/allTag"]').click() 
       
       import time
       time.sleep(2) 
       
3. Click on tag name to view all items associated
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: a[href="/favourites/tag/9"]
       :crop_element_padding: 0,000,600,0    
    
    Once you click on one of the tags, you will see all the items you've "tagged" with that tag.    
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0
       
       browser.find_element_by_css_selector('a[href="/favourites/tag/9"]').click() 

4. Perform bulk actions on items and add description to tags

    On this tag page, you will be able to perform bulk actions on the items, and even add a description to for the tag by going to "edit". 
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: a[class="inline-action pull-right"]
       :crop_element_padding: 0,000,600,0    
    


