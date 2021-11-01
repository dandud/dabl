from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField, SelectField, DecimalField, BooleanField
from wtforms.validators import DataRequired, Required, Length
from wtforms.fields.html5 import DateField

class ContainerAddForm(FlaskForm):
    volume_actual = DecimalField(u'Actual Volume', [Required()])
    submit = SubmitField(u'Create Container')

class VesselMoveContentsForm(FlaskForm):
    name = SelectField(u'New Vessel', [Required()])
    submit = SubmitField(u'Move Contents')

class VesselUpdateStatusForm(FlaskForm):
    name = StringField(u'Vessel Name', [Required()], render_kw={'readonly': True})
    status_id = SelectField(u'Vessel Status', [Required()])
    submit = SubmitField(u'Update Status')
