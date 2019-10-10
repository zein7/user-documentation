Recovering a forgotten password
===============================

.. attention:: This help page is for resetting your password if you are not logged in.

1. Go to the login page

    When attempting to browse to private pages, such as your dashboard or a Workgroup page you will be directed here first.

    .. screenshot::
       :logout: {"url": "/logout"}
       :server_path: /home
       :crop: 0,0,1000,1

    .. screenshot::
       :server_path: /login
       :alt:
       :crop_element: div.account-wall
       :crop_element_padding: 50,50,50,50
            
2. Select "Forgotten your password"

    This link will appear near the field to enter your password.
    
    .. screenshot::
       :alt:
       :crop_element: div.account-wall
       :box: a[href="/user/password/reset/"]
       :crop_element_padding: 50,50,50,50

3. Enter your email address in the field and click "Reset Password"

    If your email address is registered against an account, and email will be sent to you with a link
    that can be used to reset your password. This email may be filtered, so check your spam folder
    or other folders in your email inbox.
    
    .. screenshot::
       :alt:
       :server_path: /user/password/reset/
       :crop_element: button[value="Reset password"]
       :box: button[value="Reset password"]
       :crop_element_padding: 140,300,80,80
