How to view supersede relationships between metadata
=====================================================

1. Go to an item page 

    .. screenshot::
       :server_path: /item/35/dataelement/age
       :alt:
       :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
       :crop_element: nav.main.navbar
       :crop_element_padding: 0,000,600,0
            
2. See if item has been superseded or has superseded content

    The item's "Info box" will show you whether or not the item has any supersede content. If there are no supersedes you will see "*None*" under the supersedes.      
    
    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: div[id="infobox"]
       :crop_element_padding: 0,000,600,0

3. View the superseded content

    If there are supersedes for the item, you will be able to click and view the content. 

    .. screenshot::
       :alt:
       :crop_element: nav.main.navbar
       :box: a[href="/item/33"]
       :crop_element_padding: 0,000,600,0




