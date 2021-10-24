from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
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


class Brewstyle(db.Model):
    __tablename__ = 'brewstyles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))


class Status(db.Model):
    __tablename__ = 'statuses'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))


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

    type = db.relationship('Brewtype')
    style = db.relationship('Brewstyle')
    status = db.relationship('Status')


class Measurement(db.Model):
    __tablename__ = 'measurements'
    id = db.Column(db.Integer, primary_key = True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    time_measured = db.Column(db.DateTime)
    measurementtype_id = db.Column(db.Integer, db.ForeignKey('measurementtypes.id'))
    value = db.Column(db.Float)

    batch = db.relationship('Batch')
    measurmenttype_rel = db.relationship('Measurementtype')


class Measurementtype(db.Model):
    __tablename__ = 'measurementtypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    eng_units = db.Column(db.String(32))


class Action(db.Model):
    __tablename__ = 'actions'
    id = db.Column(db.Integer, primary_key = True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    time_performed = db.Column(db.DateTime)
    actiontype_id = db.Column(db.Integer, db.ForeignKey('actiontypes.id'))
    value = db.Column(db.Float)

    batch = db.relationship('Batch')
    actiontype_rel = db.relationship('Actiontype')


class Actiontype(db.Model):
    __tablename__ = 'actiontypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))


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


class Componentclass(db.Model):
    __tablename__ = 'componentclasses'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))


class Componenttype(db.Model):
    __tablename__ = 'componenttypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))


class Containertype(db.Model):
    __tablename__ = 'containertypes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    volume_max = db.Column(db.Float)


class Container(db.Model):
    __tablename__ = 'containers'
    id = db.Column(db.Integer, primary_key = True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('containertypes.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'))
    name = db.Column(db.String(32))
    volume_actual = db.Column(db.Float)
    is_vessel = db.Column(db.Boolean)
    time_created = db.Column(db.DateTime)

    batch = db.relationship('Batch')
    status = db.relationship('Status')
    location = db.relationship('Location')
    containertype_rel = db.relationship('Containertype')