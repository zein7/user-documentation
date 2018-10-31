How to view verison history of an item
======================================

.. attention:: You will need permission to view the version history of content. If you are a member of the Workgroup the item sits in, you will be able to see the version history. 

1. Go to an item page 

    .. screenshot::
       :server_path: /item/35/dataelement/age
       :alt:
       :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0
            
2. Select "last updated" in the info box

    The time the item was last updated will be a clickable link, if it is not - you do not have permission to view the verison history for this item. 

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: div#infobox a[href="/item/35/history"]
       :crop_element_padding: 0,000,600,0

3. View history or compare 

    On this page you will see all changes made to this item, the user who made the changes and a brief comment about the changes that were made. You will also be able to compare changes that were made to the item.   

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0

       browser.find_element_by_css_selector('div#infobox a[href="/item/35/history"]').click()
