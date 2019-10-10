How to add custom identifiers to metadata items
===============================================

1. Go to the items page

    .. screenshot::
       :server_path: /item/58/objectclass/address
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
       
3. Select the tab marked "identifiers" 
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: a[href="#tab_identifiers"]
       :crop_element_padding: 0,000,600,0  
        
4. Add in content

    Select "add a identifier" to start filling in content.

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: #tab_identifiers .btn-primary
       :crop_element_padding: 0,000,600,0
       
       browser.find_element_by_css_selector('a[href="#tab_identifiers"]').click() 
       
    You can add in multiple identifiers.              

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0
       
       browser.find_element_by_css_selector('#tab_identifiers .btn-primary').click() 
       
5. Save changes

    Once you've added in the indentifiers, select the "save changes" button and you will be able to view the idnetifiers on the item page in the "info box". 
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: input[value="Save changes"]
       :crop_element_padding: 0,000,600,0
      
