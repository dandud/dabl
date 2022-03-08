from flask import Blueprint, render_template, session, redirect, url_for, current_app, flash
from werkzeug.wrappers import StreamOnlyMixin
from .. import db
from ..models import Container, Containertype, Vessel, Vesseltype, Status, Batch
from . import vessels
from .forms import VesselMoveContentsForm, VesselUpdateStatusForm, VesselFillForm, VesselCreateForm

_label_base_url = "http://"+"192.168.1.101:5000"

@vessels.route('/vessel_overview', methods=['GET', 'POST'])
def all_vessels():
    _all_vessels = Vessel.query.join(Vessel.vesseltype_rel)\
        .all()
        #.filter(Vessel.status_id != 199)\
        #.all()
    return render_template('vessels/vessel_overview.html',
                           all_vessels=_all_vessels)


@vessels.route('/vessel_create', methods=['GET', 'POST'])
def vessel_create():
    form = VesselCreateForm()
    _vessel = Vessel()
    
    if form.validate_on_submit():
        form.populate_obj(_vessel)
        db.session.add(_vessel)
        db.session.commit()

        db.session.refresh(_vessel)
        flash('Vessel created.', 'success')
        return redirect(url_for("vessels.all_vessels"))
    
    return render_template('vessels/vessel_create.html',
                           form=form,
                           vessel=_vessel)


@vessels.route('/vessel_lookup/<container_id>', methods=['GET', 'POST'])
def vessel_lookup(container_id):
    _all_vessels = Container.query.join(Container.containertype_rel).filter(Containertype.is_vessel.is_(True)).all()
    _vessel = Container.query.join(Container.containertype_rel).filter(Container.id==container_id).first()

    if _vessel.batch_id:
        return redirect(url_for('batches.batch_view', name=_vessel.batch.name))
    
    flash('Container not associated with batch.', 'success')
    return redirect(url_for('vessels.all_vessels'))


@vessels.route('/vessel_label/<vessel_id>', methods=['GET', 'POST'])
def vessel_label(vessel_id):
    
    _vessel = Vessel.query.join(Vessel.vesseltype_rel).filter(Vessel.id==vessel_id).first()

    return render_template('vessels/vessel_label.html',
                           vessel=_vessel,
                           base_url = _label_base_url)


@vessels.route('/vessel_move_contents/<container_id>', methods=['GET', 'POST'])
def vessel_move_contents(container_id):
    _all_vessels = Container.query.join(Container.containertype_rel) \
        .filter(Containertype.is_vessel.is_(True)) \
        .filter(Container.status_id == 100) \
        .filter((Container.batch_id.is_(None) | Container.batch_id.is_('')))\
        .all()
    _current_vessel = Container.query.join(Container.containertype_rel).filter(Container.id==container_id).first()
    _batch = Batch.query.filter_by(id=_current_vessel.batch_id).first()

    form = VesselMoveContentsForm()

    form.name.choices = [(row.id, row.name) for row in _all_vessels]

    if form.validate_on_submit():
        
        new_vessel_id = form.name.data
        _new_vessel = Container.query.join(Container.containertype_rel).filter(Container.id==new_vessel_id).first()
        _new_vessel.batch_id = _current_vessel.batch_id
        _new_vessel.status_id = 102 
        _current_vessel.batch_id = ''
        _current_vessel.status_id = 101

        db.session.add(_new_vessel)
        db.session.commit()

        db.session.refresh(_new_vessel)
        flash('Vessel contents moved.', 'success')
        return redirect(url_for('vessels.all_vessels'))
    
    return render_template('containers/vessel_move_contents.html',
                           form=form,
                           vessel=_current_vessel,
                           batch=_batch)


@vessels.route('/vessel_update_status/<container_id>', methods=['GET', 'POST'])
def vessel_update_status(container_id):
    _vessel = Container.query.join(Container.containertype_rel).filter(Container.id==container_id).first()
    
    form = VesselUpdateStatusForm(obj=_vessel)

    form.status_id.choices = [(row.id, row.name) for row in Status.query.filter_by(type='Container').all()]

    if form.validate_on_submit():
        form.populate_obj(_vessel)
        db.session.add(_vessel)
        db.session.commit()

        db.session.refresh(_vessel)
        flash('Vessel status updated.', 'success')
        return redirect(url_for('vessels.all_vessels'))
    
    return render_template('containers/vessel_update_status.html',
                           form=form,
                           vessel=_vessel)


@vessels.route('/vessel_fill/<batch_id>', methods=['GET', 'POST'])
def vessel_fill(batch_id):
    _all_vessels = Container.query.join(Container.containertype_rel) \
        .filter(Containertype.is_vessel.is_(True)) \
        .filter(Container.status_id == 100) \
        .filter((Container.batch_id.is_(None) | Container.batch_id.is_('')))\
        .all()
    _batch = Batch.query.filter_by(id=batch_id).first()
    
    form = VesselFillForm()

    form.name.choices = [(row.id, row.name) for row in _all_vessels]

    if form.validate_on_submit():
        _vessel = Container.query.join(Container.containertype_rel).filter(Container.id==form.name.data).first()
        _vessel.batch_id = batch_id
        _vessel.status_id = 102 
        db.session.add(_vessel)
        db.session.commit()

        db.session.refresh(_vessel)
        flash('Vessel status updated.', 'success')
        return redirect(url_for('batches.batch_view', name=_batch.name))
    
    return render_template('containers/vessel_fill.html',
                           form=form,
                           batch=_batch)