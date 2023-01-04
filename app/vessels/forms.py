from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField, SelectField, DecimalField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Length
from wtforms.fields import DateField

class VesselCreateForm(FlaskForm):
    name = StringField(u'Vessel Name', [InputRequired()])
    vesseltype_id = SelectField(u'Container Type', [InputRequired()])
    volume_actual = DecimalField(u'Actual Volume', [InputRequired()])
    submit = SubmitField(u'Create Vessel')

class VesselMoveContentsForm(FlaskForm):
    name = SelectField(u'New Vessel', [InputRequired()])
    submit = SubmitField(u'Move Contents')

class VesselUpdateStatusForm(FlaskForm):
    name = StringField(u'Vessel Name', [InputRequired()], render_kw={'readonly': True})
    status_id = SelectField(u'Vessel Status', [InputRequired()])
    submit = SubmitField(u'Update Status')

class VesselFillForm(FlaskForm):
    name = SelectField(u'Vessel', [InputRequired()])
    submit = SubmitField(u'Fill Vessel')
