from flask_wtf import FlaskForm  # Corrected import statement
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskform(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    #email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
