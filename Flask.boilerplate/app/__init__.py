from flask import Flask
from flask_migrate import Migrate
from db import db
from config import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)