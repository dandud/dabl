from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField, SelectField, DecimalField
from wtforms.validators import DataRequired, InputRequired, Length
from wtforms.fields import DateField

class NameForm(FlaskForm):
    name = StringField('Ready to Go?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class BatchAddForm(FlaskForm):
    name = StringField(u'Batch Name', [InputRequired()])
    type_id = SelectField(u'Type', [InputRequired()])
    style_id = SelectField(u'Style', [InputRequired()])
    time_start = DateTimeField(u'Start Time', [InputRequired()])
    submit = SubmitField(u'Create Batch')


class BatchEditForm(FlaskForm):
    name = StringField(u'Batch Name', [InputRequired()], render_kw={'readonly': True})
    type_id = SelectField(u'Type', [InputRequired()], render_kw={'readonly': True})
    style_id = SelectField(u'Style', [InputRequired()], render_kw={'readonly': True})
    time_start = DateTimeField(u'Start Time', [InputRequired()])
    status_id = SelectField(u'Status', [InputRequired()])
    submit = SubmitField(u'Save Changes')


class BatchMoveForm(FlaskForm):
    name = StringField(u'Batch Name', [InputRequired()], render_kw={'readonly': True})
    type_id = SelectField(u'Type', [InputRequired()], render_kw={'readonly': True})
    style_id = SelectField(u'Style', [InputRequired()], render_kw={'readonly': True})
    time_start = DateTimeField(u'Start Time', [InputRequired()], render_kw={'readonly': True})
    status_id = SelectField(u'Status', [InputRequired()])
    
    submit = SubmitField(u'Save Changes')