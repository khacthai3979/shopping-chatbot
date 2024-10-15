
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '8f3e15c7d22850b3a72a693d77c63245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://user:password@server/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

@app.before_request
def create_tables():
    db.create_all()

from app import routes
