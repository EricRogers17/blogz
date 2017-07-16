OVERVIEW OF IMPROVEMENTS TO THE BUILD-A-BLOG APP

WHAT: 
1. Add the following templates: signup.html, login.html, and index.html

2. Add singleUser.html template that will be used to display only the blogs associated with a single given author. It will be used when we dynamically generate a page using a GET request with a user query parameter on the /blog route

3.Add the following route handler functions: signup, login, and index.

4.Create a logout function that handles a POST request to /logout and redirects to the user to /blog after deleting the username from the session.

5.Create a User class to make all this new functionality possible.

FUNCTIONALITY OF LOGIN AND SIGNUP PAGES
--- For /login page ---
- user logins successfully and is redirected to /newpost page with their username being stored in a session.

- if user enters an invalide password they are redirected to the /login page with a relevant error message.

- user tries to login with username that is not in stored in the db and is redirected to the /login page with a message "This username does not exist".

- user does not have an account and clicks "Create Account" and is directed to the /signup page.

--- For /signup page ---
- User enters new, valid username, a valid password, and verifies password correctly and is redirected to the '/newpost' page with their username being stored in a session.

- User leaves any of the username, password, or verify fields blank and gets an error message that one or more fields are invalid.

- User enters a username that already exists and gets an error message that username already exists.

- User enters different strings into the password and verify fields and gets an error message that the passwords do not match.

- User enters a password or username less than 3 characters long and gets either an invalid username or an invalid password message.