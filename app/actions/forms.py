from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField, SelectField, DecimalField
from wtforms.validators import DataRequired, InputRequired, Length
from wtforms.fields import DateField


class ActionAddForm(FlaskForm):
    time_performed = DateTimeField(u'Performed Timestpamp', [InputRequired()])
    actiontype_id = SelectField(u'Action Type', [InputRequired()])
    submit = SubmitField(u'Save Action')