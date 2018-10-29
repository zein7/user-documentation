How to apply tags to items
==========================

.. note:: You can apply tags to any items that are viewable to you in the registry. **Tags are private and only viewable by you.**

1. Select item you would like to tag

    .. screenshot::
       :server_path: /item/33/dataelement/age
       :alt:
       :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0
        
2. Select "Tag" in the Actions Bar

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: a[data-target="#TagEditorModal"]
       :crop_element_padding: 0,000,600,0
       
    A pop-up modal will appear where you can start adding tags. 
       
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0  
       
       browser.find_element_by_css_selector('a[data-target="#TagEditorModal"]').click() 
       
       import time
       time.sleep(2) 
       
3. Seperate individual tags

    You can do this by pushing "enter" or using the space bar on your keyboard. If you have used tags before, when you start typing it will automatically suggest tags you've used before. 
    
4. Save your tags

    Once happy with your tags, select "save changes" to add the tags to the item. 
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: button[id="tag-editor-submit"]
       :crop_element_padding: 0,000,600,0    
       
5. Tags will appear at the bottom of the "Info Box" 

    You will now be able to view your tags for this specific item in the info box on the items page. 
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: ul[class="taggle_list"]
       :crop_element_padding: 0,000,600,0     
    
       browser.find_element_by_css_selector('button[id="tag-editor-submit"]').click() 

       import time
       time.sleep(2) 
       
    You can click each individual tag to be taken to the tags page. Learn more about Tags by going to the "View tags" help page. 

