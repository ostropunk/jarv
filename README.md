# jarv

Jarv is a simple webbapp built on Flask to track goal fullfillment. You declare your mission and set your goals. Each goal has a deadline and a quantyfiable action. In order to track if the goal is fullfilled you register events as you do the actions.

This app was made for a very specific usecase. You are wellcome to use it in any way you want but dont expect updates or further development of the code to be regular.

## Getting started

In order to get this up and running you will need to have Python 3 installed. It is recommended that you create a virtual enviroment for your install. You vill also need to have postgresql installed and make a database for your aplication.

Please edit the file database.py and insert you database information.

Download the files and place them where you want them.

Make sure you have activated your virtual enviroment.

While in the root folder of Jarv run:
```
pip install --editable .
```

This should install jarv and all dependensies. Else you can install them using pip.

```
pip install flask flask-security flask-sqlalchemy bcrypt psycopg2
```

To start the app run:

```
export FLASK_APP=flaskr
export FLASK_DEBUG=true
flask run
```
In windows you use 'set' instead of export or in PowerShell you write:

```
$env:FLASK_APP = 'jarv'
$env:FLASK_DEBUG = 'true'
flask run
```

This will start a localy accessible version. If you want to deploy it on the webb you will need to serve it via a webbserver.
Please comment out the following code in after running the application for the first time and restart the app.

´´´
@app.before_first_request
def create_user():
    init_db()
    user_datastore.create_user(email='email@email.com', password='password')
    db_session.commit()
´´´



## Built with
* [Flask](http://flask.pocoo.org/) - Flask is a micro webdevelopment framework for Python.
* [Flask-Security](https://pythonhosted.org/Flask-Security/) - Flask-Security is an opinionated Flask extension which adds basic security and authentication features to your Flask apps quickly and easily.
* [SQLAlchemy](https://www.sqlalchemy.org/) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
* bcrypt
* [psycopg](http://initd.org/psycopg/)
* [Bootstrap](https://getbootstrap.com/) - Bootstrap is an open source toolkit for developing with HTML, CSS, and JS.
* [Chartist.js](https://gionkunz.github.io/chartist-js/index.html) - SIMPLE RESPONSIVE CHARTS
