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


@flask_sijax.route(app, '/play')
def play():

    currentIndex = 0
    
    def get_brainwave(obj_response,param):

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

        allbrainwaves['att'][0].append(attention_level)
        allbrainwaves['att'][1].append(param)

        allbrainwaves['rlx'][0].append(relax_level)
        allbrainwaves['rlx'][1].append(param)

        allbrainwaves['del'][0].append(del_level)
        allbrainwaves['del'][1].append(param)

        allbrainwaves['the'][0].append(the_level)
        allbrainwaves['the'][1].append(param)

        allbrainwaves['lal'][0].append(lal_level)
        allbrainwaves['lal'][1].append(param)

        allbrainwaves['hal'][0].append(hal_level)
        allbrainwaves['hal'][1].append(param)

        allbrainwaves['lbe'][0].append(lbe_level)
        allbrainwaves['lbe'][1].append(param)

        allbrainwaves['hbe'][0].append(hbe_level)
        allbrainwaves['hbe'][1].append(param)

        allbrainwaves['lga'][0].append(lga_level)
        allbrainwaves['lga'][1].append(param)

        allbrainwaves['mga'][0].append(mga_level)
        allbrainwaves['mga'][1].append(param)
        
        # print(allbrainwaves)
        
        obj_response.html('#rlx', relax_level)
        obj_response.html('#att', attention_level)


    if g.sijax.is_sijax_request: # Sijax request detected - let Sijax handle it
        
        
        g.sijax.register_callback('get_brainwave', get_brainwave)

        return g.sijax.process_request()

    else:
        return render_template('mainPage.html')


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
