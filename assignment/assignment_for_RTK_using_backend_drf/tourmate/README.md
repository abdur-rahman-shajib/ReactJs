Tourmate Project Description:

Tourmate is a famous web platform for providing tourists with information of several places. There is login system for admin users. They can create account from command/terminal window and login. Users of all types can see tourist places information both as list and single item. Admin can create new tourist place, Update and delete an existing place only if it was created by him.

Technical Requirements:

This is the backend project developed with python 3.7.9. You must have python (preferred version 3.7) installed on your machine to run this project locally. If you don't have python setup in your machine, you can directly download python from the official site https://www.python.org/downloads/. Then run the intaller file (exe for windows) to setup python. if you are in windows, don't forget to check 'Add python to environment path' while installing. After installation, restart your pc.

Again, Several python library/framework like Django, DjangoRestFramework, Pillow, SqlAlchemy are needed for running this project. Required versions for these libraries can be found in the requirements.txt file. You can optionally install postman app if you want to test the API without browser. Download postman from here https://www.postman.com/downloads/ and setup.

How to run this project?

- After cloning the source code, open a command/terminal window in the folder you cloned
- Then create a virtual environment for running this project following these commands:
  - `python -m venv env`
  - `env\Scripts\Activate`
- Setup required packages by running this command:
  - `pip install -r requirements.txt`
- run `cd tourmate`
- If you want to create a new user, run `python manage.py createsuperuser` and provide credential
- Now run `python manage.py runserver`
- This should open a link in your browser
- That's it, you have run the project explore codebase and play with the APIs in postman(preferred)
- Alternatively, you can run it in browser by setting the DEBUG to True in /tourmate/tourmate/settings.py
- Note that you need to use valid authentication for adding/removing/updating a tourist places (While updating/removing, the tourist place must the created by the same user)

API Documentation:

- /touristplaces/
      - retrieves all existing touristplaces information by using a get request
      - adds a new touristplace by using a post request
- /touristplace_detail/:id
      - updates an existing tourist place information using a put request
      - deletes a tourist place information using delete request
      - while adding/updating a tourist place, you can send image along with data
          - In postman, provide username and password in Authorization tab with type of 'Basic Auth'
          - Select Header tab of Request section and add one Field like: "Content-Type: multipart/form-data"
          - Then select Body tab of Request section, click on form-data add text values for name, address, rating, type (4 types available: hill, fountain, beach, landmark)
        - If you want to send image, you may add another field in the form-data named 'picture' and select it's type as file (By default, it's type is text)
          - Browse and select an image file
          - Select appropriate request type and send the request
- /users/
      - retrieves all existing admin users
- /user_detail/:id
      - Displays user information for corresponding id along with the places created by him
- /auth/createuser/
    - creates an user via post request
    - you need to provide username, password, email in header
    - also provide ContentType application/json
