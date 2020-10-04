from flask import Flask, render_template, request, g, redirect
import json
import time
import os
import flask_sijax
import random
import string
import base64
from google.cloud import automl_v1beta1 as automl

# path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app = Flask(__name__)

def predict_model(object_with_all_inputs):
    # TODO(developer): Uncomment and set the following variables
    project_id = 'PROJECT_ID_HERE'
    compute_region = 'COMPUTE_REGION_HERE'
    model_display_name = 'MODEL_DISPLAY_NAME_HERE'
    inputs = object_with_all_inputs #{'value': 3, ...}

    client = automl.TablesClient(project=project_id, region=compute_region)

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
    for result in response.payload:
        print(
            "Predicted class name: {}".format(result.tables.value)
        )
        print("Predicted class score: {}".format(result.tables.score))

@app.route('/')
def show_main():
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
    #result = predict_model()
    return json.dumps({'result':result})


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
