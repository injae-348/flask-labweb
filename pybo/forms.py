from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, FileField, MultipleFileField
from wtforms.validators import DataRequired, Email
from datetime import datetime

class CurrentStudentForm(FlaskForm):
    kname = StringField('Korean Name', validators=[DataRequired()])
    ename = StringField('English Name', validators=[DataRequired()])
    degree = StringField('Degree', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image = FileField('Image')
    
class AlumniForm(FlaskForm):
    kname = StringField('Korean Name', validators=[DataRequired()])
    ename = StringField('English Name', validators=[DataRequired()])
    degree = StringField('Degree', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    image = FileField('Image')

class NewsForm(FlaskForm):
    activity_date = StringField('Activity Date', validators=[DataRequired()])
    activity = StringField('Activity', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    images = MultipleFileField('Images', validators=[DataRequired()])
    
class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    duration = StringField('Duration', validators=[DataRequired()])
    agency = StringField('Agency', validators=[DataRequired()])
    image = FileField('Image')
    period = StringField('Period', validators=[DataRequired()])

class PublicationForm(FlaskForm):
    date = StringField('Date', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    read_more = StringField('Read More')
    category = StringField('Category', validators=[DataRequired()]) 