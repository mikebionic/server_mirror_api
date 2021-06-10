from flask import Blueprint

api = Blueprint('main_api', __name__)

from main.api import server_mirrors_api