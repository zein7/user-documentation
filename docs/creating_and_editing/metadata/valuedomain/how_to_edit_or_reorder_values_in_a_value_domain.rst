How to reorder and edit values in a Value Domain
================================================

1. Open a Value Domain item page

    .. screenshot::
      :server_path: /item/57/valuedomain/gender-code-x
      :alt:
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav.main.navbar
      :crop_element_padding: 0,000,600,0
      
2. Select "edit" next to permissible values
    
    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :box: a[data-target="#value_domain_modal"]
      :crop_element_padding: 0,000,600,0
      
    The permissible values edit modal will appear. You can reorder, edit, and even delete the items from here. 
    
    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :crop_element_padding: 0,000,700,0
      
      browser.find_element_by_css_selector('a[data-target="#value_domain_modal"]').click()   
      
      import time
      time.sleep(2)  
    
3. Edit and reorder the items

    Selecting the "three lines" next to each of the values lets you drag and move the items elsewhere in the list. 
    
    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :box: i[class="fa fa-bars grabber ui-sortable-handle"]
      :crop_element_padding: 0,000,700,0
      
4. After reordering or editing the items, select "Save"

    Your items will be updated on the items page. 
      
 
      
   
      




