from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField, SelectField, DecimalField
from wtforms.validators import DataRequired, InputRequired, Length
from wtforms.fields import DateField


class MeasurementAddForm(FlaskForm):
    time_measured = DateTimeField(u'Measurement Timestamp', [InputRequired()])
    measurementtype_id = SelectField(u'Measurment Type', [InputRequired()])
    value = DecimalField(u'Measured Value', [InputRequired()])

    submit = SubmitField(u'Save Measurement')