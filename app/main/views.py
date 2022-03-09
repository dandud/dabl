from flask import render_template, session, redirect, url_for, current_app, flash
from .. import db
from ..models import Measurement, Measurementtype, User, Batch, Action, Actiontype, Brewtype, Brewstyle, Status, Container, Containertype, Vessel, Vesseltype
from ..email import send_email
from . import main, batches, actions, measurements
from .forms import NameForm, ActionAddForm, MeasurementAddForm, BatchAddForm, BatchEditForm, BatchMoveForm
from datetime import datetime



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


@batches.route('/batch_add', methods=['GET', 'POST'])
def batch_add():
    form = BatchAddForm()
    _batch = Batch()
  
    time_now = datetime.now()
    form.time_start.data = time_now

    form.type_id.choices = [(row.id, row.name) for row in Brewtype.query.all()]
    form.style_id.choices = [(row.id, row.name) for row in Brewstyle.query.all()]


    if form.validate_on_submit():
        _batch.time_updated = time_now
        _batch.status_id = 1000
        form.populate_obj(_batch)
        db.session.add(_batch)
        db.session.commit()

        db.session.refresh(_batch)
        flash('Batch added.', 'success')
        return redirect(url_for('batches.all_batches'))
    
    return render_template('batch_add.html',
                           form=form,
                           batch=_batch)


@batches.route('/batch_move/<batch_name>', methods=['GET', 'POST'])
def batch_move(batch_name):
    _batch = Batch.query.filter_by(name=batch_name).first()
    _vessels = Container.query.join(Container.containertype_rel).filter(Containertype.is_vessel.is_(True), Container.batch_id==_batch.id).all
    _all_vessels = Container.query.join(Container.containertype_rel).filter(Containertype.is_vessel.is_(True)).all()


    form = BatchMoveForm(obj=_batch)

    time_now = datetime.now()

    form.type_id.choices = [(row.id, row.name) for row in Brewtype.query.all()]
    form.style_id.choices = [(row.id, row.name) for row in Brewstyle.query.all()]
    form.status_id.choices = [(row.id, row.name) for row in Status.query.filter_by(type='Batch').all()]
    form.status_id.choices = [(row.id, row.name) for row in Status.query.filter_by(type='Batch').all()]

    if form.validate_on_submit():
        _batch.time_updated = time_now
        form.populate_obj(_batch)
        db.session.add(_batch)
        db.session.commit()

        db.session.refresh(_batch)
        flash('Batch updated.', 'success')
        return redirect(url_for("batches.all_batches"))
    
    return render_template('batch_move.html',
                           form=form,
                           batch=_batch)


@batches.route('/batch_edit/<batch_name>', methods=['GET', 'POST'])
def batch_edit(batch_name):
    _batch = Batch.query.filter_by(name=batch_name).first()
    
    form = BatchEditForm(obj=_batch)

    time_now = datetime.now()

    form.type_id.choices = [(row.id, row.name) for row in Brewtype.query.all()]
    form.style_id.choices = [(row.id, row.name) for row in Brewstyle.query.all()]
    form.status_id.choices = [(row.id, row.name) for row in Status.query.filter_by(type='Batch').all()]

    if form.validate_on_submit():
        _batch.time_updated = time_now
        form.populate_obj(_batch)
        db.session.add(_batch)
        db.session.commit()

        db.session.refresh(_batch)
        flash('Batch updated.', 'success')
        return redirect(url_for('batches.all_batches'))
    
    return render_template('batch_edit.html',
                           form=form,
                           batch=_batch)


@batches.route('/batch_view/<name>', methods=['GET', 'POST'])
def batch_view(name):
    _batch = Batch.query.filter_by(name=name).first()
    _measurements = Measurement.query.filter_by(batch_id=_batch.id).all()
    _actions = Action.query.filter_by(batch_id=_batch.id).all()
    _vessels = Vessel.query.join(Vessel.vesseltype_rel).filter(Vessel.batch_id==_batch.id).first()
    _containers = Container.query.join(Container.containertype_rel).filter(Container.batch_id==_batch.id).all()

    if not _batch:
        flash('Oops! Something went wrong!.', 'danger')
        return redirect(url_for('batches.all_batches'))

    return render_template('batch_view.html',
                           batch=_batch, 
                           measurements=_measurements,
                           actions=_actions,
                           vessels=_vessels,
                           containers=_containers)


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
    
    return render_template('action_add.html',
                           form=form,
                           action=_action)


@measurements.route('/measurement_add/<batch_name>', methods=['GET', 'POST'])
def measurement_add(batch_name):
    form = MeasurementAddForm()
    _measurement = Measurement()
    _batch = Batch.query.filter_by(name=batch_name).first()

    _measurement.batch_id = _batch.id
    
    time_now = datetime.now()
    form.time_measured.data = time_now

    form.measurementtype_id.choices = [(row.id, row.name) for row in Measurementtype.query.all()]

    if form.validate_on_submit():
        form.populate_obj(_measurement)
        db.session.add(_measurement)
        db.session.commit()

        db.session.refresh(_measurement)
        flash('Measurement added.', 'success')
        return redirect(url_for('batches.batch_view', name = _batch.name))
    
    return render_template('measurement_add.html',
                           form=form,
                           measurement=_measurement)