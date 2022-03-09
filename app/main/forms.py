from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField, SelectField, DecimalField
from wtforms.validators import DataRequired, Required, Length
from wtforms.fields.html5 import DateField

class NameForm(FlaskForm):
    name = StringField('Ready to Go?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ActionAddForm(FlaskForm):
    time_performed = DateTimeField(u'Performed Timestpamp', [Required()])
    actiontype_id = SelectField(u'Action Type', [Required()])
    submit = SubmitField(u'Save Action')


class MeasurementAddForm(FlaskForm):
    time_measured = DateTimeField(u'Measurement Timestamp', [Required()])
    measurementtype_id = SelectField(u'Measurment Type', [Required()])
    value = DecimalField(u'Measured Value', [Required()])
    submit = SubmitField(u'Save Measurement')


class BatchAddForm(FlaskForm):
    name = StringField(u'Batch Name', [Required()])
    type_id = SelectField(u'Type', [Required()])
    style_id = SelectField(u'Style', [Required()])
    time_start = DateTimeField(u'Start Time', [Required()])
    submit = SubmitField(u'Create Batch')


class BatchEditForm(FlaskForm):
    name = StringField(u'Batch Name', [Required()], render_kw={'readonly': True})
    type_id = SelectField(u'Type', [Required()], render_kw={'readonly': True})
    style_id = SelectField(u'Style', [Required()], render_kw={'readonly': True})
    time_start = DateTimeField(u'Start Time', [Required()])
    status_id = SelectField(u'Status', [Required()])
    submit = SubmitField(u'Save Changes')


class BatchMoveForm(FlaskForm):
    name = StringField(u'Batch Name', [Required()], render_kw={'readonly': True})
    type_id = SelectField(u'Type', [Required()], render_kw={'readonly': True})
    style_id = SelectField(u'Style', [Required()], render_kw={'readonly': True})
    time_start = DateTimeField(u'Start Time', [Required()], render_kw={'readonly': True})
    status_id = SelectField(u'Status', [Required()])
    
    submit = SubmitField(u'Save Changes')