How to view registration states of an item
==========================================

1. Go to an item page 

    .. screenshot::
       :server_path: /item/35/dataelement/age
       :alt:
       :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0
            
2. Check the Item's Info box

    In the items info box you will see if the item has been endorsed and when. Items in your Sandbox can only be visible to you or a Workgroup if you've added it to a Workgroup. 

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: div#infobox dd[class="large"]
       :crop_element_padding: 0,000,600,0

3. Select "View registration history"

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: a[href="/item/35/registrationHistory"]
       :crop_element_padding: 0,000,600,0

    If the item has been endorsed, you will be able to view its registration history. From here, you will see the state each Registration Authority has the item in. 

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0

       browser.find_element_by_css_selector('a[href="/item/35/registrationHistory"]').click()
