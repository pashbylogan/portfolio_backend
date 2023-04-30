from flask import Blueprint

bp = Blueprint('fictionary', __name__)

from api.fictionary import routes
