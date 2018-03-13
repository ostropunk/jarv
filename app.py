from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
from flask_security import Security, login_required, \
     SQLAlchemySessionUserDatastore
from database import db_session, init_db
from models import User, Role, Goal, Event
from flask_mail import Mail

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = 'thisismybreadandsalt'
app.config['SECURITY_REGISTERABLE'] = True

# After 'Create app'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'fredrik@ostro.se'
app.config['MAIL_PASSWORD'] = 'c6937e36c27ef25dba52f4c5932c4742'
mail = Mail(app)

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session,
                                                User, Role)
security = Security(app, user_datastore)


# Create a user to test with
'''
@app.before_first_request
def create_user():
    init_db()
    user_datastore.create_user(email='fredrik@ostro.se', password='password')
    db_session.commit()
'''


# Views
@app.route('/')
@login_required
def home():
    title = "Home"
    message = 'Here you go!'
    return render_template('index.html', title=title, message=message)


@app.route('/users')
@login_required
def users():
    user = db_session.query(User).order_by(User.id)
    return render_template('users.html', user=user)


if __name__ == '__main__':
    app.run()
