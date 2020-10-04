from flask import Flask, render_template, request, g, redirect
import json
import time
import os
import flask_sijax
import random
import string
import base64
import math
from google.cloud import automl_v1beta1 as automl

# path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app = Flask(__name__)

def predict_model(object_with_all_inputs):
    # TODO(developer): Uncomment and set the following variables
    project_id = 'astrowaves'
    compute_region = 'us-central1'
    model_display_name = 'brainwave_directi_20201004012516'
    inputs = object_with_all_inputs #{'value': 3, ...}

    client = automl.TablesClient(project=project_id, region=compute_region)
    feature_importance = False
    if feature_importance:
        response = client.predict(
            model_display_name=model_display_name,
            inputs=inputs,
            feature_importance=True,
        )
    else:
        response = client.predict(
            model_display_name=model_display_name, inputs=inputs
        )

    print("Prediction results:")
    correct_label = ""
    confidence = 0
    for result in response.payload:
        if result.tables.score > confidence:
            confidence = result.tables.score
            correct_label = result.tables.value.string_value
        print("Predicted class name: {}".format(result.tables.value))
        print("Predicted class score: {}".format(result.tables.score))


    return [correct_label, confidence]

@app.route('/')
def show_main():
    return render_template('index.html')

@app.route('/predict-test')
def test():
    obj = {'att':75, 'rlx':90, 'del': 738101, 'the':39584, 'lal':16615, 'hal':35298, 'hbe':24041, 'lbe':9483, 'lga': 5281, 'mga':2970}
    print(predict_model(obj))
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def evaluate():
    fin = open("att.txt")
    attention_level = 0

    for each_line in fin:
        attention_level = int(each_line.rstrip())

    fin.close()

    fin = open("rlx.txt")
    relax_level = 0

    for each_line in fin:
        relax_level = int(each_line.rstrip())

    fin.close()

    fin = open("del.txt")

    del_level = 0
    for each_line in fin:
        del_level = int(each_line.rstrip())

    fin.close()

    fin = open("the.txt")

    the_level = 0
    for each_line in fin:
        the_level = int(each_line.rstrip())

    fin.close()

    fin = open("lal.txt")

    lal_level = 0
    for each_line in fin:
        lal_level = int(each_line.rstrip())

    fin.close()

    fin = open("hal.txt")

    hal_level = 0
    for each_line in fin:
        hal_level = int(each_line.rstrip())

    fin.close()

    fin = open("lbe.txt")

    lbe_level = 0
    for each_line in fin:
        lbe_level = int(each_line.rstrip())

    fin.close()

    fin = open("hbe.txt")

    hbe_level = 0
    for each_line in fin:
        hbe_level = int(each_line.rstrip())

    fin.close()

    fin = open("lga.txt")

    lga_level = 0
    for each_line in fin:
        lga_level = int(each_line.rstrip())

    fin.close()

    fin = open("mga.txt")

    mga_level = 0
    for each_line in fin:
        mga_level = int(each_line.rstrip())

    fin.close()
    #todo predict_model
    obj = {'att':attention_level, 'rlx':relax_level, 'del': del_level, 'the':the_level, 'lal':lal_level, 'hal':hal_level, 'hbe':hbe_level, 'lbe':lbe_level, 'lga': lga_level, 'mga':mga_level}
    result = predict_model(obj)
    return json.dumps({'move':result[0], 'confidence':round(result[1]*100,2)})

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
