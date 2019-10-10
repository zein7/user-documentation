How to add code lists to a Value Domain
=======================================

1. Open a Value Domain item page

    .. screenshot::
      :server_path: /item/49/valuedomain/days-of-the-week-code-n
      :alt:
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav.main.navbar
      :crop_element_padding: 0,000,600,0
      
2. Select "Add permissible values" 
    
    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :box: a[href="/valuedomain/49/edit/values/permissible"]
      :crop_element_padding: 0,000,600,0

3. Add the values

    Select "Add a code" to start inputing codes.
    
    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :box: a[class="btn btn-primary add_code_button"]
      :crop_element_padding: 0,000,600,0
      
      browser.find_element_by_css_selector('a[href="/valuedomain/49/edit/values/permissible"]').click()

      import time
      time.sleep(2)   
      
    You can add more codes by clicking the button continuously.
    
    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :crop_element_padding: 0,000,700,0
      
      browser.find_element_by_css_selector('a[class="btn btn-primary add_code_button"]').click()
      browser.find_element_by_css_selector('a[class="btn btn-primary add_code_button"]').click()
      browser.find_element_by_css_selector('a[class="btn btn-primary add_code_button"]').click()
      browser.find_element_by_css_selector('a[class="btn btn-primary add_code_button"]').click()
      browser.find_element_by_css_selector('a[class="btn btn-primary add_code_button"]').click()
      browser.find_element_by_css_selector('a[class="btn btn-primary add_code_button"]').click()
      browser.find_element_by_css_selector('a[class="btn btn-primary add_code_button"]').click()
      
      import time
      time.sleep(2)    
      
4. Input the values information
    
    .. screenshot::
      :form_data: [
       {'permissiblevalue_set-0-value':"1", 'permissiblevalue_set-0-meaning':'Monday', 'permissiblevalue_set-1-value':'2', 'permissiblevalue_set-1-meaning':'Tuesday', 'permissiblevalue_set-2-value':'3', 'permissiblevalue_set-2-meaning':'Wednesday', 'permissiblevalue_set-3-value':'4', 'permissiblevalue_set-3-meaning':'Thursday', 'permissiblevalue_set-4-value':'5', 'permissiblevalue_set-4-meaning':'Friday', 'permissiblevalue_set-5-value':'6', 'permissiblevalue_set-5-meaning':'Saturday', 'permissiblevalue_set-6-value':'7', 'permissiblevalue_set-6-meaning':'Sunday', '__submit__': False}
       ]    
      :alt:
      :crop_element: nav.main.navbar
      :crop_element_padding: 0,000,700,0
      
5. Save the values

    Once done inputing the codes, select "Save".
    
    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :box: button[value="Save"]
      :crop_element_padding: 0,000,700,0
          
    The codes will now appear on the items page. 
     
 
      
    
     
