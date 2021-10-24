from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField, SelectField, DecimalField
from wtforms.validators import DataRequired, Required, Length
from wtforms.fields.html5 import DateField

class ContainerAddForm(FlaskForm):
    volume_actual = DecimalField(u'Actual Volume', [Required()])
    submit = SubmitField(u'Save Measurement')