from flask import Blueprint, render_template, session, redirect, url_for, current_app, flash
from .. import db
from ..models import Container, Containertype
from . import containers
from .forms import ContainerAddForm


_label_base_url = "http://"+"192.168.1.101:5000"

@containers.route('/vessel_overview', methods=['GET', 'POST'])
def all_vessels():
    _all_vessels = Container.query.join(Container.containertype_rel).filter(Containertype.is_vessel.is_(True)).all()
    
    return render_template('containers/vessel_overview.html',
                           all_vessels=_all_vessels)


@containers.route('/container_add', methods=['GET', 'POST'])
def container_add():
    form = ContainerAddForm()
    _container = Container()
    
    if form.validate_on_submit():
        form.populate_obj(_container)
        db.session.add(_container)
        db.session.commit()

        db.session.refresh(_container)
        flash('Container added.', 'success')
        return redirect(url_for("batches.all_batches"))
    
    return render_template('containers/container_add.html',
                           form=form,
                           container=_container)


@containers.route('/vessel_lookup/<container_id>', methods=['GET', 'POST'])
def vessel_lookup(container_id):
    _all_vessels = Container.query.join(Container.containertype_rel).filter(Containertype.is_vessel.is_(True)).all()
    _vessel = Container.query.join(Container.containertype_rel).filter(Container.id==container_id).first()

    if _vessel.batch_id:
        return redirect(url_for('batches.batch_view', name=_vessel.batch.name))
    
    flash('Container not associated with batch.', 'success')
    return redirect(url_for('containers.all_vessels'))


@containers.route('/vessel_label/<container_id>', methods=['GET', 'POST'])
def vessel_label(container_id):
    
    _vessel = Container.query.join(Container.containertype_rel).filter(Container.id==container_id).first()

    return render_template('containers/container_label.html',
                           vessel=_vessel,
                           base_url = _label_base_url)
