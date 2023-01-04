from flask import Blueprint, render_template, session, redirect, url_for, current_app, flash
#from werkzeug.wrappers import StreamOnlyMixin
from .. import db
from ..models import Action, Actiontype, Batch
from . import actions
from .forms import ActionAddForm
from datetime import datetime


@actions.route('/action_add/<batch_name>', methods=['GET', 'POST'])
def action_add(batch_name):
    form = ActionAddForm()
    _action = Action()
    _batch = Batch.query.filter_by(name=batch_name).first()
    print (_batch)
    _action.batch_id = _batch.id
    
    time_now = datetime.now()
    form.time_performed.data = time_now

    form.actiontype_id.choices = [(row.id, row.name) for row in Actiontype.query.all()]

    if form.validate_on_submit():
        form.populate_obj(_action)
        db.session.add(_action)
        db.session.commit()

        db.session.refresh(_action)
        flash('Action added.', 'success')
        return redirect(url_for('batches.batch_view', name = _batch.name))
    
    return render_template('actions/action_add.html',
                           form=form,
                           action=_action)