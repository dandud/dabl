from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Required, Length
from wtforms.fields.html5 import DateField

class NameForm(FlaskForm):
    name = StringField('Ready to Go?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ActionAddForm(FlaskForm):
    #batch = TextAreaField(u'Your Batch', [Required(), Length(1, 32)])
    time_performed = DateTimeField(u'Performed Datetime', [Required()])
    actiontype_id = IntegerField(u'Type', [Required()]) 

    submit = SubmitField(u'Save Action')