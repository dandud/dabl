from flask import Blueprint

actions = Blueprint('actions', __name__)

from .views import actions
from app.main import errors