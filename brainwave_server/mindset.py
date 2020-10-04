from NeuroPyThree import NeuroPy
import time
import os
import json
from datetime import datetime

object1=NeuroPy("COM4")

allbrainwaves = {
                 'att':[],
                 'rlx':[],
                 'del':[],
                 'the':[],
                 'lal':[],
                 'hal':[],
                 'hbe':[],
                 'lbe':[],
                 'lga':[],
                 'mga':[]
                 }

def attention_callback(value):
    if value != 0:
        allbrainwaves['att'].append(value)
        with open('att.txt', "w") as outfile:
            outfile.write(str(value))

def meditation_callback(value):
    if value != 0:
        allbrainwaves['rlx'].append(value)
        with open('rlx.txt', 'w') as outfile:
            outfile.write(str(value))

def delta_waves_callback(value):
    if value != 0:
        allbrainwaves['del'].append(value)
        with open('del.txt', 'w') as outfile:
            outfile.write(str(value))

def theta_waves_callback(value):
    if value != 0:
        allbrainwaves['the'].append(value)
        with open('the.txt', 'w') as outfile:
            outfile.write(str(value))

def lowalpha_waves_callback(value):
    if value != 0:
        allbrainwaves['lal'].append(value)
        with open('lal.txt', 'w') as outfile:
            outfile.write(str(value))

def highalpha_waves_callback(value):
    if value != 0:
        allbrainwaves['hal'].append(value)
        with open('hal.txt', 'w') as outfile:
            outfile.write(str(value))


def lowbeta_waves_callback(value):
    if value != 0:
        allbrainwaves['lbe'].append(value)
        with open('lbe.txt', 'w') as outfile:
            outfile.write(str(value))

def highbeta_waves_callback(value):
    if value != 0:
        allbrainwaves['hbe'].append(value)
        with open('hbe.txt', 'w') as outfile:
            outfile.write(str(value))


def lowgamma_waves_callback(value):
    if value != 0:
        allbrainwaves['lga'].append(value)
        with open('lga.txt', 'w') as outfile:
            outfile.write(str(value))

def midgamma_waves_callback(value):
    if value != 0:
        allbrainwaves['mga'].append(value)
        with open('mga.txt', 'w') as outfile:
            outfile.write(str(value))

#set call backs:
object1.setCallBack("attention",attention_callback)
object1.setCallBack("meditation",meditation_callback)

object1.setCallBack("delta",delta_waves_callback)

object1.setCallBack("theta",theta_waves_callback)

object1.setCallBack("lowAlpha",lowalpha_waves_callback)
object1.setCallBack("highAlpha",highalpha_waves_callback)

object1.setCallBack("lowBeta",lowbeta_waves_callback)
object1.setCallBack("highBeta",highbeta_waves_callback)

object1.setCallBack("lowGamma",lowgamma_waves_callback)
object1.setCallBack("midGamma",midgamma_waves_callback)

object1.start()
time.sleep(4)
now = datetime.now().time()

while True:
    time.sleep(2)
    fin = open("complete_data.txt","w")
    fin.write(json.dumps(allbrainwaves))
    print(allbrainwaves['att'])
