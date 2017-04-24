from flask_wtf import FlaskForm
from wtforms.fields import StringField, FloatField, RadioField
from wtforms import validators

class FeatureInput(FlaskForm):
    sex = RadioField('sex', choices=[('man','a man'),('woman','a woman')], validators=[validators.Required()])
    pclass = RadioField('passenger_class', choices=[('1','first class'),('2','business'), ('3','economy')], validators=[validators.Required()], render_kw={"placeholder": "what class is your ticket in?"})
    married = RadioField('married', choices=[('married','married'),('unmarried','unmarried')], validators=[validators.Required()]) 
    age = StringField('age', validators=[validators.Required()], render_kw={"placeholder": "how old are you?"})
    siblings = StringField('siblings', validators=[validators.Required()], render_kw={"placeholder": "how many siblings do you have?"})

'''
author @yvan
'''