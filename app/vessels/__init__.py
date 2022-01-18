from flask import Blueprint

vessels = Blueprint('vessels', __name__)

from .views import vessels
from app.main import errors