from flask import Blueprint, render_template, session, redirect, url_for, current_app, flash
from .. import db
from ..models import Container, Containertype
from . import containers
from .forms import ContainerAddForm

@containers.route('/vessel_overview', methods=['GET', 'POST'])
def all_vessels():
    #User.query.join(User.spaces).filter(User.username=='Bob', Space.name=='Mainspace').first()
    _all_vessels = Container.query.join(Container.containertype_rel).filter(Containertype.is_vessel.is_(True)).all()
    #_all_vessels = Container.query.filter(Container.containertype_rel.has(Containertype.is_vessel.is_(True))).all()
    print(_all_vessels)
    return render_template('containers/vessel_overview.html',
                           all_vessels=_all_vessels)

@containers.route('/container_add', methods=['GET', 'POST'])
def container_add():
    form = ContainerAddForm()
    _container = Container()
    
    print("container!")
    

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