from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_prefixed_env()

csrf = CSRFProtect(app)
db = SQLAlchemy(app)

from url_shortener import commands
from url_shortener import routes
