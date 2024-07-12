from flask import Flask
from flask_mongoengine import MongoEngine
from flask_mail import Mail


from flask_cors import CORS
# cross_origin

from subprocess import call

from settings import MONGODB_SETTINGS, mail_settings

db = MongoEngine()






app = Flask(__name__)
mail=Mail(app)
def create_app(**config_overrides):
    
    # mail = Mail(app)
    CORS().init_app(app=app, resources={r"/*": {"origins": "*"}})
    CORS(app)


    # Load Config File
    app.config.from_pyfile('settings.py')

    # Apply Overrides for tests
    app.config.update(config_overrides)
    app.config.update(mail_settings)

    # Set up db
    db.init_app(app)

    # import blueprints
    from prints.auth.views import auth_app
    from prints.payments.views import payments_app
    from prints.homepage.views import homepage_app



    # register blueprints    
    app.register_blueprint(auth_app)
    app.register_blueprint(payments_app)
    app.register_blueprint(homepage_app)

    return app
