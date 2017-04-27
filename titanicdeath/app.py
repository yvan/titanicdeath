import os
import re
import pandas as pd
import numpy as np

from sklearn.externals import joblib
from functools import wraps
from datetime import datetime, timedelta

from flask import g, session, abort, redirect, url_for, request, Flask, render_template, jsonify, flash
from flask_bootstrap import Bootstrap

from titanicdeath.forms.feature_input_form import FeatureInput

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
logreg = joblib.load(os.path.join(app.config['APP_STATIC'], 'logreg.pkl'))
age_bands =[[-0.08, 16], [17, 32], [33, 48], [49, 64], [65, 80]]
df = pd.read_csv(os.path.join(app.config['APP_STATIC'], 'X_train.csv'))
sex_title_cross = pd.crosstab(df['Title'], df['Sex'])
df_orig = pd.read_csv(os.path.join(app.config['APP_STATIC'], 'train.csv'))

@app.route('/', methods=['GET'])
def main_page():
    feature_input = FeatureInput()
    return render_template('main.html', form=feature_input)

@app.route('/prediction/<string:p>', methods=['GET'])
def prediction_page(p):
    return render_template('prediction.html', prediction=p)

@app.route('/internal/submit_user_features', methods=['POST'])
def get_features():
    feature_input = FeatureInput(request.form)
    if request.form and feature_input.validate_on_submit():
        pred  = get_model_result(
        request.form['age'], 
        request.form['sex'], 
        request.form['siblings'],
        request.form['married'],
        request.form['pclass'])
        pred = 'S' if pred[0] else 'D'
        return redirect(url_for('prediction_page', p=pred))
    else:
        flash('you need to fill each field properly!')
        return redirect(url_for('main_page'))

def get_model_result(age, sex, siblings, married, pclass):
    # make a dataframe with columns passed in
    # get new ageband category
    if int(age) >= 80:
        age = 80
    else:
        age =  [i for i,band in enumerate(age_bands) if int(age) <= band[1] and int(age) >= band[0]][0]
    sex = 0 if sex == 'man' else 1
    pclass = int(pclass)
    embarkation = int(df['Embarked'].sample(1).values[0])
    parents_children = int(df_orig['Parch'].sample(1).values[0])
    siblings_spouses = int(df_orig['SibSp'].sample(1).values[0]) + int(siblings)
    is_alone = (parents_children + siblings_spouses) > 0
    title = int(df['Title'][df['Sex'] == sex].sample(1))
    fare = int(df['Fare'][df['Pclass'] == int(pclass)].sample(1))
    # pclass, sex, age, fare, embarked, title, isalone, int(age)*int(pclass)
    X_df = pd.DataFrame([[pclass, sex, age, fare, embarkation, title, is_alone, age*pclass]], columns=['Pclass','Sex','Age','Fare','Embarked','Title','IsAlone','Age*Class'])
    return logreg.predict(X_df)
