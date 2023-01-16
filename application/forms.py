from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    department=StringField("Department",validators=[DataRequired()]) 
    year=StringField("Year",validators=[DataRequired()]) 
    submit= SubmitField("submit")