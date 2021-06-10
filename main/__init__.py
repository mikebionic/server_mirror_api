from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from main.config import Config
db = SQLAlchemy()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)

	from main.api import api as main_api
	app.register_blueprint(main_api, url_prefix = Config.MIRROR_API_URL_PREFIX)

	return app