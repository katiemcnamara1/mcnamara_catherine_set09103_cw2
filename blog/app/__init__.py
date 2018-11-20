import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import Config
from flask_babel import Babel, lazy_gettext as _loginbabel 
from flask import request

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = _loginbabel('Please log in to access this page.')
bootstrap = Bootstrap(app)
babel = Babel(app)


@babel.localeselector
def get_locale():
 return request.accept_languages.best_match(app.config['LANGUAGES'])
 #  return 'es'
    
from app import routes, models
