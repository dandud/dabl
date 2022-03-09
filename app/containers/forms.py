from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField, SelectField, DecimalField, BooleanField
from wtforms.validators import DataRequired, Required, Length
from wtforms.fields.html5 import DateField

class ContainerAddForm(FlaskForm):
    name = StringField(u'Container Name')
    containertype_id = SelectField(u'Container Type', [Required()])
    volume_actual = DecimalField(u'Actual Volume', [Required()])
    time_created = DateTimeField(u'Create Time')
    submit = SubmitField(u'Create Container')

class VesselMoveContentsForm(FlaskForm):
    name = SelectField(u'New Vessel', [Required()])
    submit = SubmitField(u'Move Contents')

class VesselUpdateStatusForm(FlaskForm):
    name = StringField(u'Vessel Name', [Required()], render_kw={'readonly': True})
    status_id = SelectField(u'Vessel Status', [Required()])
    submit = SubmitField(u'Update Status')

class VesselFillForm(FlaskForm):
    name = SelectField(u'Vessel', [Required()])
    submit = SubmitField(u'Fill Vessel')
