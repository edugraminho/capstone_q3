from flask import Flask
from flask_jwt_extended import JWTManager
from secrets import token_hex
from app.views.home import bp_home
from app.views.owner_views import bp_owner
from environs import Env
from app.views.authorization_view import bp_authorization
from app.models import db, ma, mg


def create_app():

    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = env.bool(
        "SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config["SQLALCHEMY_DATABASE_URI"] = env.str("SQLALCHEMY_DATABASE_URI")
    app.config['JWT_SECRET_KEY'] = token_hex(16)

    JWTManager(app)

    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_authorization)
    app.register_blueprint(bp_owner)

    return app
