from flask import Blueprint, render_template, session, redirect, url_for, current_app
from .. import db
from ..models import Batch

batches1 = Blueprint('batches', __name__)

@batches1.route('/batch_overview1', methods=['GET', 'POST'])
def all_batches():
    print('all_batches function 2 executed')
    _all_batches = Batch.query.all()

    return render_template('batches/batch_overview.html',
                           all_batches=_all_batches)