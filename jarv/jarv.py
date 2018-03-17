from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask_security import Security, login_required, \
     SQLAlchemySessionUserDatastore
from jarv.database import db_session, init_db
from jarv.models import User, Role, Goal, Event, Mission


# Create app
app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , flaskr.py
app.config.update(dict(
    SECRET_KEY='development key',
    DEBUG=True,
    SECURITY_PASSWORD_HASH='bcrypt',
    SECURITY_PASSWORD_SALT='thisismybreadandsalt'
))


app.config.from_envvar('JARV_SETTINGS', silent=True)
# After 'Create app'

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)


# Create a user to test with
'''
@app.before_first_request
def create_user():
    init_db()
    user_datastore.create_user(email='email@email.com', password='password')
    db_session.commit()
'''


# Views
@app.route('/')
@login_required
def home():
    title = "Home"
    message = 'Here you go!'
    return render_template('index.html', title=title, message=message)


@app.route('/mal/')
@app.route('/mal')
@login_required
def missions():
    missions = db_session.query(Mission).order_by(Mission.id)
    return render_template('missions.html', missions=missions)


@app.route('/mal/add/', methods=['GET', 'POST'])
@app.route('/mal/add', methods=['GET', 'POST'])
@login_required
def add_missions():
    if request.method == 'POST':
        mission = Mission(description=request.form['description'])
        db_session.add(mission)
        db_session.commit()

        return redirect(url_for('missions'))

    else:
        return render_template('add_mission.html')


@app.route('/mal/<mission_id>/')
@app.route('/mal/<mission_id>')
@login_required
def show_mission(mission_id):
    mission = db_session.query(Mission).get(mission_id)
    return render_template('show_mission.html', mission=mission)


@app.route('/mal/<mission_id>/matt/')
@app.route('/mal/<mission_id>/matt')
@login_required
def goals(mission_id):
    goals = db_session.query(Goal).order_by(Goal.id)
    return render_template('goals.html', goals=goals, mission_id=mission_id)


@app.route('/mal/<mission_id>/matt/add/', methods=['GET', 'POST'])
@app.route('/mal/<mission_id>/matt/add', methods=['GET', 'POST'])
@login_required
def add_goals(mission_id):
    if request.method == 'POST':
        goal = Goal(title=request.form['title'],
                    mission_id=mission_id,
                    description=request.form['description'],
                    goal_count=request.form['goal_count'],
                    deadline=datetime.strptime(request.form['deadline'],
                                               '%Y-%m-%d'))
        db_session.add(goal)
        db_session.commit()

        return redirect(url_for('show_mission', mission_id=mission_id))

    else:
        return render_template('add_goal.html', mission_id=mission_id)


@app.route('/mal/<mission_id>/matt/<goal_id>/')
@app.route('/mal/<mission_id>/matt/<goal_id>')
def show_goal(mission_id, goal_id):
    goal_id = int(goal_id)
    goal = db_session.query(Goal).get(goal_id)
    events = goal.events
    return render_template('show_goal.html', goal=goal, goal_id=goal_id,
                           mission_id=mission_id,
                           deadline=goal.deadline.strftime("%Y-%m-%d"),
                           events=len(events))


@app.route('/mal/<mission_id>/matt/<goal_id>/event/', methods=['GET', 'POST'])
@app.route('/mal/<mission_id>/matt/<goal_id>/event', methods=['GET', 'POST'])
@login_required
def goal_events(mission_id, goal_id):
    goal_id = int(goal_id)
    if request.method == 'POST':
        event = Event(description=request.form['description'],
                      goal_id=int(goal_id))
        db_session.add(event)
        db_session.commit()

        return redirect(url_for('goal_events', goal_id=goal_id,
                        mission_id=mission_id))
    else:
        events = db_session.query(Event).filter_by(goal_id=goal_id).all()
        return render_template('events.html', events=events, goal_id=goal_id,
                               mission_id=mission_id)


@app.route('/installningar/')
@app.route('/installningar')
@login_required
def settings():
    pass


@app.route('/installningar/roller/')
@app.route('/installningar/roller')
@login_required
def roles():
    roles = db_session.query(Role).order_by(Role.id)
    return render_template('roles.html', roles=roles)


@app.route('/installningar/roller/add/', methods=['GET', 'POST'])
@app.route('/installningar/roller/add', methods=['GET', 'POST'])
@login_required
def add_roles():
    if request.method == 'POST':
        role = Role(name=request.form['name'],
                    description=request.form['description'])
        db_session.add(role)
        db_session.commit()

        return redirect(url_for('roles'))

    else:
        return render_template('add_role.html')


@app.route('/installningar/users/')
@app.route('/installningar/users')
@login_required
def users():
    users = db_session.query(User).order_by(User.id)
    return render_template('users.html', users=users)


@app.route('/installningar/users/add/')
@app.route('/installningar/users/add')
@login_required
def add_users():
    if request.method == 'POST':
        user = Role(name=request.form['name'],
                    description=request.form['description'],
                    email=)

                    email = Column(String(255), unique=True)
                    username = Column(String(255))
                    password = Column(String(255))
        db_session.add(user)
        db_session.commit()

        return redirect(url_for('users'))

    else:
        return render_template('add_user.html')


if __name__ == '__main__':
    app.run()
