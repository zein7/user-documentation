How to add a new discussion post from a Workgroup page
======================================================

1. Go to your Workgroups

    On your Dashboard side panel select "Workgroups".
    
    .. screenshot::
        :server_path: /account/home
        :alt:
        :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
        :crop_element: nav.main.navbar
        :box: #user_sidebar a[href="/account/workgroups"]
        :crop_element_padding: 0,000,600,0
        
2. Select the Workgroup you want to post in

    This is a list of all the Workgroups you are a member of. You are able to view content for this Workgroup and post a discussion in it. Click the Workgroups name to view the Workgroups page.  
    
    .. screenshot::
      :server_path: /account/workgroups
      :alt:
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav.main.navbar
      :clicker: a[href="/workgroup/4-example-workgroup"]
      :crop_element_padding: 0,000,600,0

3. Click "view all posts"

    Here you will see all conversations for this Workgroup.
    
    .. screenshot::
      :server_path: /workgroup/4-example-workgroup
      :alt:
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav.main.navbar
      :clicker: a[href="/discussions/workgroup/4"]
      :crop_element_padding: 0,000,600,0
   
4. Select "New Discussion"
	
    To create a new discussion post, click the "New Discussion" button. There is one at the top of the page, and one at the bottom. 
    
    .. screenshot::
      :server_path: /discussions/workgroup/4
      :alt:
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav.main.navbar
      :clicker: a[href="/discussions/new?workgroup=4"]
      :crop_element_padding: 0,000,600,0
    
5. Create your discussion post

    Type in a title for your post and a message. You can even link to different items within the registry. The Workgroup is already pre-selected for your convenience. 
    
    .. screenshot::
      :server_path: /discussions/new?workgroup=4
      :form_data: [
         {'title':"Hello",'body':"Example post", '__submit__': False}
         ]
      :alt:
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav.main.navbar
      :crop_element_padding: 0,000,600,0
    
6. Click "New Post" to create

    Once your happy with your post, select "New Post" to save and create it. 
    
    .. screenshot::
      :server_path: /discussions/new?workgroup=4
      :form_data: [
         {'title':"Hello",'body':"Example post", '__submit__': False}
         ]
      :alt:
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav.main.navbar
      :clicker: i.fa-pencil
      :crop_element_padding: 0,000,600,0
      
      
    After saving, you will be taken to the newly created posts page. From here you can comment, edit, delete, or close your post.
      
    .. screenshot::
      :server_path: /discussions/new?workgroup=4
      :form_data: [
         {'title':"Hello",'body':"Example post", '__submit__': False}
         ]
      :alt:
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav.main.navbar
      :crop_element_padding: 0,000,600,0
      
      browser.find_element_by_css_selector('i.fa-pencil').click()
      
   
   
