from flask import Blueprint, render_template, session, redirect, url_for, current_app, flash
from werkzeug.wrappers import StreamOnlyMixin
from .. import db
from ..models import Measurement, Measurementtype, Batch
from . import measurements
from .forms import MeasurementAddForm
from datetime import datetime

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