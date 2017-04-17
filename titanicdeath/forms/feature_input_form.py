from flask_wtf import FlaskForm
from wtforms.fields import StringField, FloatField, IntegerField
from wtforms.validators import DataRequired

class FeatureInput(FlaskForm):
    age = FloatField('age', validators=[DataRequired()], render_kw={"placeholder": "how old are you?"})
    sex = StringField('sex', validators=[DataRequired()], render_kw={"placeholder": "are you a man or a woman?"})
    siblings = FloatField('siblings', validators=[DataRequired()], render_kw={"placeholder": "how many brothers and sisters do you have?"})
    parents = FloatField('parents', validators=[DataRequired()], render_kw={"placeholder": "how many parents do you have?"}) 
    pclass = IntegerField('passenger_class', validators=[DataRequired()], render_kw={"placeholder": "what class is your ticket in?"})

'''
author @yvan
'''