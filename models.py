from database import Base
from datetime import datetime
from flask_security import UserMixin, RoleMixin
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                       String, ForeignKey, Table, Text


class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('users.id'))
    role_id = Column('role_id', Integer(), ForeignKey('roles.id'))


class Role(Base, RoleMixin):
    __tablename__ = 'roles'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255))
    password = Column(String(255))
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))


class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    description = Column(Text, nullable=False)
    pub_date = Column(DateTime, nullable=False,
                      default=datetime.utcnow)
    deadline = Column(DateTime())

    events = relationship('Event', backref='goals', lazy=True)

    def __repr__(self):
        return '<Goal %r>' % self.title


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    pub_date = Column(DateTime, nullable=False,
                      default=datetime.utcnow)
    goal_id = Column(Integer, ForeignKey('goals.id'),
                     nullable=False)

    def __repr__(self):
        return '<Event %r>' % self.name
