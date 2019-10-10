How to assign a metadata item to a new Workgroup
================================================

.. attention:: You will only be able to assign items to another Workgroup from the items current Workgroup if you: 

    a. Are a member of the Workgroup the item is currently in, and a member of the 
       Workgroup you are moving the item to, and 
    b. Have the necessary permissions to do so as specified by the Registry Administrator
    
------------------------------------------------------------------------

1. Go to the items page

    .. screenshot::
      :server_path: /item/57/valuedomain/gender-code-x
      :alt:
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav.main.navbar
      :crop_element_padding: 0,000,600,0
      
2. Select the "Open Item Editor" from the Actions Bar
    
    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :box: a[data-target="#infobox_adv_edit"]
      :crop_element_padding: 0,000,600,0

      browser.find_element_by_css_selector('button[id="metadata_action_menu_action"]').click()

      import time
      time.sleep(2)
      
    The item editor modal will appear.
      
    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :box: a[data-target="#infobox_adv_edit"]
      :crop_element_padding: 0,000,600,0

      browser.find_element_by_css_selector('a[data-target="#infobox_adv_edit"]').click()

      import time
      time.sleep(3)
      
3. Select Workgroup 

    In the editor under "Workgroup" select the Workgroup you would like to move the item to. 
    
    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :box: select[name="workgroup"]+span.select2 span.select2-selection__arrow
      :crop_element_padding: 0,000,600,0

      browser.find_element_by_css_selector('select[name="workgroup"]+span.select2 span.select2-selection__arrow').click()

      import time
      time.sleep(3)


    The Workgroups you are a member of will appear in the drop-down for you to select from. 

    .. screenshot::
      :alt:
      :crop_element: nav.main.navbar
      :crop_element_padding: 0,0,600,0

      browser.find_element_by_css_selector('span[class="select2-results"] ul li').click()

      
4. Once done, click "Save Changes"

    Once saved, the item will appear in the new Workgroup. 

