# IT PUTS THE LOTION ON
#### Video Demo:  <https://youtu.be/PgCKzvTBFas>
#### Description:

## OVERVIEW
This is a Flask-based Weather API application that leverages current weather data from the openweathermap.org site. This project capitalises on the simplicity and efficiency of the Flask framework and its compatibility with Python.

This is a a single-page app that functions as a dynamic web app. Search engine optimisation was not a concern for this project, so there was no need to create a multi-page application.

There was some consideration of UI. I’ve employed Flask’s flash methods to provide the user with helpful feedback as to the success of failure of their posts. I avoided making use of Bulma's foreboding is-danger modifier class and swapped it with a friendlier is-warning yellow modifier.

This application makes use of Flask’s extension for SQLAlchemy allowing for uncomplicated database access. For this project’s functionality, it was not necessary to create a database with multiple tables and fields — id and city name were sufficient to allow for Flask’s message flashing triggered by database commits and deletions.

As mentioned, I made use of the Bulma framework for some easy frontend styling. It’s lightweight, responsive, and felt more intuitive and less cluttered to use than Bootstrap. It also made sense, given that I was not making use of JavaScript for this project. Again, I used Flask’s message categories to alternate message box colours.

Security-wise, this application uses a secret key to sign session cookies for protection against cookie data meddling.

This application incorporates environment variables in a .env file to ensure that sensitive information is not enclosed and stored in source control; this includes the secret key and personal API key.

### SOME LIMITATIONS
Admittedly, there are some limitations to this application:
- It’s quirky, which could limit its appeal.
- It could convey more information, i.e. wind speed might inform the user whether or not they need a jacket, but this would alter the humour in the application, which is meant to offer health advice regardless of temperatures. The code could further filter messaging based on associated weather icons. For example, prompt the user to bring an umbrella if the icon indicates rain.
- Additional testing is missing, but that’s an endeavour for another project.

### PROJECT FILES
#### app.py
This is the application's root. Flask uses an app object as an instance of Flask. This is where the main functionality of the app is kept. Specifically, it contains the application’s routes. As a single page application, this project is defined by a single route, the index, however, a ‘get’ and ‘post’ function determine what information is presented to the user in the index.

#### weather.html
This file contains the basic page structure for the app, which draws on Jinja's placeholder templates to render dynamic data, specifically, json current weather data requested from the openweathermap API.

#### config.py
These files are used for configuration required to be set prior to startup. Config files are used to store key value pairs or some configurable information that could be read or accessed in the code

#### .env
I’ve added Python-dotenv to the application to make it load the configuration from a .env file when it is present (e.g. in development) while remaining configurable via the environment. In here, I’ve stored the API KEY and secret key.

#### test_weather_api.py
I’ve provided two simple assertion tests.

I've tried to emphasise best practice in this project. This project, uninvolved though it may be, recognises the need for well-tested code. In the interest of time, I’ve only incorporated a status code check and a content type check. However, the status code repeatedly printed a 401. When asserting equivalence between the API KEY in the .env file and the key itself, the test passed.

While the request works, the API returns 401 for some unknown reason when run from pytest in the CS50 environment. When running pytest out of the CS50 environment, the test passes. Finally, when running from that environment without pytest, using CURL, I receive a 200 status.

Alternatively, the API itself didn't like being called from pytest in the CS50 IDE. The test was run in a non-virtual IDE and it passed! I’m not crazy!

#### weather.db
I manually set up the tables and columns for this database in weather.db via sqlite3, specifying the table name and fields accordingly. Database commits and deletions occur based on user inputs: requesting city weather data or deleting a weather pop-up. The City table is queried in the index, in which the API is called, it’s returned data is then appended to a variable that is rendered in the HTML.

#### Pipfile
Pipfile is the dedicated file used by the Pipenv virtual environment to manage project dependencies. In this case, flask-sqlalchemy and python requests.

#### Pipfile.lock
Describes the dependencies of the necessary dependencies or packages and libraries needed to run the application, such as: greenbelt and charset-normalizer, and Werkzeug, which is a WSGI web application library.

### SET-UP
pipenv install flask_sqlalchemy
pipenv install requests
Export FLASK_APP=app.py (this allows us to simply use flask run)

Check your Python version with:
- python —version
- If you don’t have python3, then type: pip3 install pipenv
- pipenv shell (activates your virtual environment)

#### Database set-up:
There are a few steps to setting up your weather database. Type the following sequentially:
- sqlite3 weather.db
- .tables
- .exit
- now just run: python
- from app import db
- db.create_all()

#### Pytest set-up:
- pip install pytest
- now just run: pytesy -k test_weather_api.py
