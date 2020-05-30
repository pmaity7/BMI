from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired

class BmiForm(FlaskForm):
    weight = IntegerField('Weight in kg', validators=[DataRequired()])
    height = FloatField('Height in m', validators=[DataRequired()])
    submit = SubmitField('Check BMI')

