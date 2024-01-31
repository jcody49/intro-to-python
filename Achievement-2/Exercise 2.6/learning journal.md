# Exercise 2.6

## Reflection Questions

1. In your own words, write down the importance of incorporating authentication into an application. You can take an example application to explain your answer.
   -    Authentication is integral to any modern app for two main reasons: online protection and personalized user experience. First and foremost, the user needs to be protected in a number of ways for a variety of reasons. Users need their identity to be protected--that only their eyes see their sensitive information. It also ensures that only the authenticated user can complete actions as said user. In short, it keeps user information private and protected. Also, authentication allows you to enhance and personalize the user experience. This way you can allow users to build their own profiles with content specific to them. For instance, with Netflix, you want to be able to add movies to watch later.

2. In your own words, explain the steps you should take to create a login for your Django web application.
   
   - First, You define the view at the project level. 
     - Import AuthenticationForm for Django's easy authentication. Clean the data to ensure its validity. Call authenticate() on username and password and provide a redirect path.
   - Second, create the template at the src level.
     - This view is outside of the apps, so it should be at the src level. Add a new templates folder; in that, put an auth folder; in that, put the html template. Implement a POST form element with a csrf_token and include a button for the login single-click. Then, update your 'DIRS' template in settings.py, to: 'DIRS': [BASE_DIR  / 'templates']. 
   - Third, specify url mapping.
     - Typically, specify mapping with app/urls.py.
   - Fourth, register the URL.
     - Import login_view at the project level views.py. Include you path in your url patterns at the project level.
   
3. Look up the following three Django functions on Django’s official documentation and/or other trusted sources and write a brief description of each. 
   - authenticate():
     - This function is a part of Django's authentication system. It verifies user credentials, such as username and password, attempting to authenticate the user. If successful, it returns a user object representing the authenticated user; otherwise, it returns None.
   - redirect():
     - Just call this with a url as an argument, and it generates an http response to redirect the user to the specified view.
   - include():
     - The include() function allows you to include other URL patterns from different modules or appsmaking it modular and re-usable.