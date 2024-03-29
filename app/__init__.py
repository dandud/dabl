from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
admin = Admin()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import batches as batches_blueprint
    app.register_blueprint(batches_blueprint)

    from .actions import actions as actions_blueprint
    app.register_blueprint(actions_blueprint)

    from .measurements import measurements as measurements_blueprint
    app.register_blueprint(measurements_blueprint)

    from .containers import containers as containers_blueprint
    app.register_blueprint(containers_blueprint)

    from .vessels import vessels as vessels_blueprint
    app.register_blueprint(vessels_blueprint)

    return app

