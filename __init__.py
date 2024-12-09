from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
import os


app = Flask(__name__)


# PostgreSQL接続の設定
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = "5432"
database = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{username}:{password}@{host}:{port}/{database}?sslmode=require"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



# データベースとマイグレーションの設定
db = SQLAlchemy(app)

migrate = Migrate(app, db)
secret_key = os.getenv("SECRET_KEY")
app.secret_key = secret_key

import main  



