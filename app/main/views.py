from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import Measurement, User, Batch, Action
from ..email import send_email
from . import main, batches, actions
from .forms import NameForm, ActionAddForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))



@batches.route('/batch_overview', methods=['GET', 'POST'])
def all_batches():
    _all_batches = Batch.query.all()

    return render_template('batch_overview.html',
                           all_batches=_all_batches)


@batches.route('/batch_view/<name>', methods=['GET', 'POST'])
def batch_view(name):
    _batch = Batch.query.filter_by(name=name).first()
    _measurements = Measurement.query.filter_by(batch_id=_batch.id).all()
    _actions = Action.query.filter_by(batch_id=_batch.id).all()
    if not _batch:
        #flash('Oops! Something went wrong!.', 'danger')
        return redirect(url_for("batches.all_batches"))

    return render_template('batch_view.html',
                           batch=_batch, 
                           measurements=_measurements,
                           actions=_actions)


@actions.route('/action_add/<batch_name>', methods=['GET', 'POST'])
def action_add(batch_name):
    form = ActionAddForm()
    _action = Action()
    _batch = Batch.query.filter_by(name=batch_name).first()
    print (_batch)
    #_action.batch = _batch.name
    _action.batch_id = _batch.id

    if form.validate_on_submit():
        print(_action.batch , _action.batch_id , _action.actiontype_id , _action.time_performed)
        form.populate_obj(_action)
        print(_action.batch , _action.batch_id , _action.actiontype_id , _action.time_performed)
        db.session.add(_action)
        db.session.commit()

        db.session.refresh(_action)
        #flash('Your task is added successfully!', 'success')
        return redirect(url_for("batches.batch_view", name = _batch.name))
    
    return render_template('action_add.html',
                           form=form,
                           action=_action)