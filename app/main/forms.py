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
