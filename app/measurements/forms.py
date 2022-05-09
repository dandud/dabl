from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField, SelectField, DecimalField
from wtforms.validators import DataRequired, Required, Length
from wtforms.fields.html5 import DateField


class MeasurementAddForm(FlaskForm):
    time_measured = DateTimeField(u'Measurement Timestamp', [Required()])
    measurementtype_id = SelectField(u'Measurment Type', [Required()])
    value = DecimalField(u'Measured Value', [Required()])

    submit = SubmitField(u'Save Measurement')