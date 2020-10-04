from flask import Flask, render_template, request, g, redirect
import json
import time
import os
import flask_sijax
import random
import string
import base64

# path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app = Flask(__name__)

app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'

flask_sijax.Sijax(app)

allbrainwaves = {
                 'att':[ [], [] ],
                 'rlx':[ [], [] ],
                 'del':[ [], [] ],
                 'the':[ [], [] ],
                 'lal':[ [], [] ],
                 'hal':[ [], [] ],
                 'hbe':[ [], [] ],
                 'lbe':[ [], [] ],
                 'lga':[ [], [] ],
                 'mga':[ [], [] ]
                 }


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

    return json.dumps({'result':123})


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
