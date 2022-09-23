from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
secret_key = os.getenv("SECRET_KEY")
app.config["SECRET_KEY"] = {secret_key}
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from market import routes

