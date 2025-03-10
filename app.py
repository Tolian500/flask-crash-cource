from flask import Flask, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder ='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    app.secret_key = 'secretkey'


    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def log_user(uid):
        return User.query.get(uid)

    @login_manager.user_loader
    def unauthorised_callback():
        return redirect(url_for('index'))

    bcrypt = Bcrypt(app)



    # import later on
    from routes import register_routes
    register_routes(app, db, bcrypt)


    migrate = Migrate(app, db)

    return app