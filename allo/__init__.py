from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5824467ee6c2d43a976e80f0f48f2b88'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xdzeyawqpiassu:334f76d485cfa3dea4e57408c7d0200927cedf97c636904db662211cff9560d9@ec2-34-197-84-74.compute-1.amazonaws.com:5432/de9hbnuh1gvq95'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'TRUE'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from allo import routes
