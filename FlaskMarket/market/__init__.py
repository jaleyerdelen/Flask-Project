from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"

secret_key = os.getenv("SECRET_KEY")
app.config["SECRET_KEY"] = {secret_key}


db = SQLAlchemy(app)

from market import routes

