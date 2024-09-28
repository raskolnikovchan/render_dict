from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
import os


app = Flask(__name__)


db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_USER")
db_host = os.getenv("DB_USER")
db_name = os.getenv("DB_USER")

# PostgreSQL接続の設定
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{db_user}:{db_password}"
    f"@{db_host}/{db_name}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# データベースとマイグレーションの設定
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.secret_key = 'db_test_key'

import main  



