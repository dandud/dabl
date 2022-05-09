from flask import Blueprint

main = Blueprint('main', __name__)
batches = Blueprint('batches', __name__)
actions = Blueprint('actions', __name__)

from . import views, errors
