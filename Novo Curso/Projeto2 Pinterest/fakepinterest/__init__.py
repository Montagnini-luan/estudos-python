from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
database = SQLAlchemy(app)
app.config['SECRET_KEY'] = '13797612f03684a56c72c6c5ce588580'
app.config['UPLOAD_FOLDER'] = 'static/fotos_posts'

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

from fakepinterest import routes