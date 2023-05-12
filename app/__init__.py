import logging
from logging.handlers import SMTPHandler
# importer la classe Flask depuis le flask package
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user

# instance de la classe Flask dans la variable app
# __name__ variable from python fourni le nom du package (flask package)
app = Flask(__name__)


# instance de la classe Config :
app.config.from_object(Config)

# contexte : 
# app.app_context.push()

# instance de la bdd :
db = SQLAlchemy(app)

# instance de la migration :
migrate = Migrate(app, db)

# instance de la classe Login :
login = LoginManager(app)
login.init_app(app)
login.login_view = 'login'

# instance de la classe serveur de mail :
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Le Blog des poètes - Erreurs',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


# pour éviter les import circulaires :
from app import routes, models, errors