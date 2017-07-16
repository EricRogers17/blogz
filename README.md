OVERVIEW OF IMPROVEMENTS TO THE BUILD-A-BLOG APP

WHAT: 
1. Add the following templates: signup.html, login.html, and index.html

2. Add singleUser.html template that will be used to display only the blogs associated with a single given author. It will be used when we dynamically generate a page using a GET request with a user query parameter on the /blog route

3.Add the following route handler functions: signup, login, and index.

4.Create a logout function that handles a POST request to /logout and redirects to the user to /blog after deleting the username from the session.

5.Create a User class to make all this new functionality possible.

