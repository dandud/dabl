from flask import Blueprint

containers = Blueprint('containers', __name__)

from .views import containers
from app.main import errors