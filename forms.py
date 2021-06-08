from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField 
from wtforms.validators import DataRequired, NumberRange, Email
import datetime

class VolunteerForm(FlaskForm):
    # create attributes
    student_name = StringField("Please enter your full name", validators=[DataRequired()])
    student_ID = StringField("Please enter your student ID", validators=[DataRequired()])
    hours = DecimalField("Please enter the number of hours worked: ",validators=[DataRequired(), NumberRange(max=10)])

    event = SelectField("Select which event you attended",
                 choices=[('WISE', 'WISE'), ('Food Drive', 'Food Drive'),('ARIS STEM Summit','ARIS STEM Summit'), ('Charity Miles','Charity Miles'),('Crocheting','Crocheting'), ('Animal Shelter','Animal Shelter'), ('FLL BoroBlast', 'FLL BoroBlast'), ('IBM', 'IBM')])

    submit = SubmitField("Enter")


class SpecificUser(FlaskForm):
    # create attributes
    student_ID = StringField("Please enter your Student ID", validators=[DataRequired()])
 
    submit = SubmitField("Enter")



