from datetime import datetime
from typing import DefaultDict
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager, admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import event
from flask_login import UserMixin, AnonymousUserMixin

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


class Brewtype(db.Model):
    __tablename__ = 'brewtypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))

    def __repr__(self):
        return '<Brewtype %r>' % (self.name)


class Brewstyle(db.Model):
    __tablename__ = 'brewstyles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))

    def __repr__(self):
        return '<Brewstyle %r>' % (self.name)

class Status(db.Model):
    __tablename__ = 'statuses'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))

    def __repr__(self):
        return '<Status %r>' % (self.name)

class Engunit(db.Model):
    __tablename__ = 'engunits'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))

    def __repr__(self):
        return '<Engunit %r>' % (self.name)

class Batch(db.Model):
    __tablename__ = 'batches'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique=True, index=True)
    time_start = db.Column(db.DateTime)
    time_end = db.Column(db.DateTime)
    time_updated = db.Column(db.DateTime)
    type_id = db.Column(db.Integer, db.ForeignKey('brewtypes.id'))
    style_id = db.Column(db.Integer, db.ForeignKey('brewstyles.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String(128))
    abv = db.Column(db.Float)

    type = db.relationship('Brewtype')
    style = db.relationship('Brewstyle')
    status = db.relationship('Status')

    def get_age(self):
        if self.time_start:
            now = datetime.now()
            age = now - self.time_start
            return str(age.days)
        
    def __repr__(self):
        return '<Batch %r>' % (self.name)


@event.listens_for(Batch, "after_insert")
def insert_container_log(mapper, connection, target):
    history_table = Batch_history.__table__
    connection.execute(history_table.insert().values(user_id=1, name=target.name, status_id=target.status_id ))


@event.listens_for(Batch, "after_update")
def insert_container_log(mapper, connection, target):
    history_table = Batch_history.__table__
    connection.execute(history_table.insert().values(user_id=1, name=target.name, status_id=target.status_id ))


class Batch_history(db.Model):
    __tablename__ = "batch_history"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    modified_on = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(32))
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'))


class Measurement(db.Model):
    __tablename__ = 'measurements'
    id = db.Column(db.Integer, primary_key = True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    time_measured = db.Column(db.DateTime)
    measurementtype_id = db.Column(db.Integer, db.ForeignKey('measurementtypes.id'))
    value = db.Column(db.Float)

    batch = db.relationship('Batch')
    measurmenttype_rel = db.relationship('Measurementtype')

    def __repr__(self):
        return '<Measurement %r>' % (self.name)


class Measurementtype(db.Model):
    __tablename__ = 'measurementtypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    eng_units = db.Column(db.String(32))

    def __repr__(self):
        return '<Measurementtype %r>' % (self.name)


class Action(db.Model):
    __tablename__ = 'actions'
    id = db.Column(db.Integer, primary_key = True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    time_performed = db.Column(db.DateTime)
    actiontype_id = db.Column(db.Integer, db.ForeignKey('actiontypes.id'))
    value = db.Column(db.Float)

    batch = db.relationship('Batch')
    actiontype_rel = db.relationship('Actiontype')

    def __repr__(self):
        return '<Action %r>' % (self.name)


class Actiontype(db.Model):
    __tablename__ = 'actiontypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))

    def __repr__(self):
        return '<Actiontype %r>' % (self.name)


class Component(db.Model):
    __tablename__ = 'components'
    id = db.Column(db.Integer, primary_key = True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    componentclass_id = db.Column(db.Integer, db.ForeignKey('componentclasses.id'))
    componenttype_id = db.Column(db.Integer, db.ForeignKey('componenttypes.id'))
    value = db.Column(db.Float)

    batch = db.relationship('Batch')
    componentclass_rel = db.relationship('Componentclass')
    componenttype_rel = db.relationship('Componenttype')

    def __repr__(self):
        return '<Component %r>' % (self.name)


class Componentclass(db.Model):
    __tablename__ = 'componentclasses'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))

    def __repr__(self):
        return '<Componentclass %r>' % (self.name)


class Componenttype(db.Model):
    __tablename__ = 'componenttypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))

    def __repr__(self):
        return '<Componenttype %r>' % (self.name)


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))

    def __repr__(self):
        return '<Location %r>' % (self.name)


class Containertype(db.Model):
    __tablename__ = 'containertypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    volume_max = db.Column(db.Float)

    def __repr__(self):
        return '<Containertype %r>' % (self.name)


class Container(db.Model):
    __tablename__ = 'containers'
    id = db.Column(db.Integer, primary_key = True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    containertype_id = db.Column(db.Integer, db.ForeignKey('containertypes.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'))
    name = db.Column(db.String(32))
    volume_actual = db.Column(db.Float)
    volume_engunit_id = db.Column(db.Integer, db.ForeignKey('engunits.id'))
    time_created = db.Column(db.DateTime)

    batch = db.relationship('Batch')
    status = db.relationship('Status')
    location = db.relationship('Location')
    containertype_rel = db.relationship('Containertype')
    volume_engunit_rel = db.relationship('Engunit')


    def get_age(self):
        if self.time_created:
            now = datetime.now()
            age = now - self.time_created
            return str(age.days)
    
    def __repr__(self):
        return '<Container %r>' % (self.name)


class Vesseltype(db.Model):
    __tablename__ = 'vesseltypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    volume_max = db.Column(db.Float)

    def __repr__(self):
        return '<Vesseltype %r>' % (self.name)


class Vessel(db.Model):
    __tablename__ = 'vessels'
    id = db.Column(db.Integer, primary_key = True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    vesseltype_id = db.Column(db.Integer, db.ForeignKey('vesseltypes.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'))
    name = db.Column(db.String(32))
    volume_actual = db.Column(db.Float)
    time_created = db.Column(db.DateTime)

    batch = db.relationship('Batch')
    status = db.relationship('Status')
    location = db.relationship('Location')
    vesseltype_rel = db.relationship('Vesseltype')

    def __repr__(self):
        return '<Vessel %r>' % (self.name)

admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Role,db.session))
admin.add_view(ModelView(Batch,db.session))
admin.add_view(ModelView(Brewstyle,db.session))
admin.add_view(ModelView(Brewtype,db.session))
admin.add_view(ModelView(Engunit,db.session))
admin.add_view(ModelView(Measurementtype,db.session))
admin.add_view(ModelView(Measurement,db.session))
admin.add_view(ModelView(Actiontype,db.session))
admin.add_view(ModelView(Action,db.session))
admin.add_view(ModelView(Componentclass,db.session))
admin.add_view(ModelView(Componenttype,db.session))
admin.add_view(ModelView(Component,db.session))
admin.add_view(ModelView(Vesseltype,db.session))
admin.add_view(ModelView(Vessel,db.session))
admin.add_view(ModelView(Containertype,db.session))
admin.add_view(ModelView(Container,db.session))

@event.listens_for(Container, "after_insert")
def insert_container_log(mapper, connection, target):
    history_table = Container_history.__table__
    connection.execute(history_table.insert().values(user_id=1, container_id=target.id, location_id=target.location_id, containertype_id=target.containertype_id, status_id=target.status_id ))


@event.listens_for(Container, "after_update")
def insert_container_log(mapper, connection, target):
    history_table = Container_history.__table__
    connection.execute(history_table.insert().values(user_id=1, container_id=target.id, location_id=target.location_id, containertype_id=target.containertype_id, status_id=target.status_id ))


class Container_history(db.Model):
    __tablename__ = "container_history"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    modified_on = db.Column(db.DateTime, default=datetime.utcnow)
    container_id = db.Column(db.Integer, db.ForeignKey('containers.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    containertype_id = db.Column(db.Integer, db.ForeignKey('containertypes.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'))