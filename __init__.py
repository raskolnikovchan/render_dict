from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '.gitignore', '.env'))

app = Flask(__name__)

# PostgreSQL接続の設定
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# データベースとマイグレーションの設定
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.secret_key = 'db_test_key'

import main  



