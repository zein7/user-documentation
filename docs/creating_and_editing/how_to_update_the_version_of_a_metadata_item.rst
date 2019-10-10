How to update the version of a metadata item
============================================

1. Go to the items page

    .. screenshot::
       :server_path: /item/51/property/height
       :alt:
       :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0
        
2. Open "item editor" from Actions Bar

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: a[data-target="#infobox_adv_edit"]
       :crop_element_padding: 0,000,600,0
       
       browser.find_element_by_css_selector('i[class="fa fa-fw fa-pencil-square-o"]').click()     
       
    A pop-up modal will appear.
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0 
       
       browser.find_element_by_css_selector('a[data-target="#infobox_adv_edit"]').click() 
       
       import time
       time.sleep(4)
       
3. Update version

    In the box marked "verison". 
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: input[id="id_version"]
       :crop_element_padding: 0,000,600,0  
       
4. Save changes

    Once you save changes the version number will show up next to the name on the item page. 

    .. screenshot::
       :alt:
       :box: input[value="Save changes"]
       :crop_element_padding: 0,000,800,0 
      
