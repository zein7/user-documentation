How to supersede metadata items 
===============================

1. Go to the item that is to be superseded
    
    .. screenshot::
        :server_path: /item/33/dataelement/age
        :alt:
        :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
        :crop_element: nav.main.navbar
        :crop_element_padding: 0,000,600,0
        
2. Select "Supersede item" from Actions Bar
    
    .. screenshot::
        :alt:
        :crop_element: nav.main.navbar
        :box: a[href="/action/supersede/33"]
        :crop_element_padding: 0,000,600,0
                 
        browser.find_element_by_css_selector('button[id="metadata_action_menu_action"]').click()
          
        import time
        time.sleep(2)
        
3. Add an item to Supersede current item

    .. screenshot::
        :alt:
        :crop_element: nav.main.navbar
        :box: a[class="btn btn-primary add_code_button"]
        :crop_element_padding: 0,000,600,0
                 
        browser.find_element_by_css_selector('a[href="/action/supersede/33"]').click()
          
        import time
        time.sleep(2)
        
    Select the "Add a relationship" to start searching for the item you want to supersede the current item.         
        
    .. screenshot::
        :alt:
        :crop_element: nav.main.navbar
        :crop_element_padding: 0,000,600,0
        
        
        browser.find_element_by_css_selector('a.btn.btn-primary.add_code_button').click()
        
4. Add in additional information 

    After selecting the item you want to supersede with, select the Registration Authority and date you want this superseded relationship to take place on. **If you select a future date, the superseded relationship will not show up until that date.** You can also choose to add in a message. 
    
    .. screenshot::
        :alt:
        :crop_element: nav.main.navbar
        :box: button[accesskey="s"]
        :crop_element_padding: 0,000,900,0
        
    Once you are done, select "Save", and if the date you've selected is today, or in the past it will show up in the "Info box" on the items page.
        
    .. screenshot::
        :server_path: /item/33/dataelement/age
        :alt:
        :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
        :crop_element: nav.main.navbar
        :box: a[href="/item/34"]
        :crop_element_padding: 0,000,600,0
        
        
        
        

    
    

   


    
    

