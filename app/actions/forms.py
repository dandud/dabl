from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField, SelectField, DecimalField
from wtforms.validators import DataRequired, Required, Length
from wtforms.fields.html5 import DateField


class ActionAddForm(FlaskForm):
    time_performed = DateTimeField(u'Performed Timestpamp', [Required()])
    actiontype_id = SelectField(u'Action Type', [Required()])
    submit = SubmitField(u'Save Action')