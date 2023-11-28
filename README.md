# URL-Shortener Application
   ![alt-text](https://github.com/soopertramp/url-shortner/blob/main/flask.png)
   
 ## Flask
  1. Create a project required environment
  2. Install a pipenv 
      ```
      pip3 install pipenv
      ```
  3. To create virtual env for project
     ```
     pipenv install 
     ```
   **Note: it will Creating a virtualenv for this project… and it will create the pipfile.lock for [dev-packages] and        	[packages].**

  4. To activate this project's virtualenv, run
     ```
     pipenv shell
     ```
  5. Create project in flask and install
     ```
     pipenv install flask
     ```
  7. Go to the your virtualenv in command prompt for windows
     ```
     set FLASK_APP=urlshort
     ```
     **Note: Go to the your virtualenv in terminal  for windows**
     ```
     export FLASK_APP=urlshort
     ``` 
  8. Run the flask app  
      ```
      flask run
      ``` 
  9. How to move on to the flask app to production to development in command prompt 
      ```
      set FLASK_ENV=development
      ```
 10. Then run app
       ```
       flask run
       ```

   **Credits - Nick Walter**
