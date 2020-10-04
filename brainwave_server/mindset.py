from NeuroPyThree import NeuroPy
import time
import os
import json


object1=NeuroPy("COM4")


def attention_callback(value):
    if value != 0:
        with open('att.txt', "w") as outfile:
            outfile.write(str(value))

def meditation_callback(value):
    if value != 0:
        with open('rlx.txt', 'w') as outfile:
            outfile.write(str(value))

def delta_waves_callback(value):
    if value != 0:
        with open('del.txt', 'w') as outfile:
            outfile.write(str(value))

def theta_waves_callback(value):
    if value != 0:
        with open('the.txt', 'w') as outfile:
            outfile.write(str(value))

def lowalpha_waves_callback(value):
    if value != 0:
        with open('lal.txt', 'w') as outfile:
            outfile.write(str(value))

def highalpha_waves_callback(value):
    if value != 0:
        with open('hal.txt', 'w') as outfile:
            outfile.write(str(value))


def lowbeta_waves_callback(value):
    if value != 0:
        with open('lbe.txt', 'w') as outfile:
            outfile.write(str(value))

def highbeta_waves_callback(value):
    if value != 0:
        with open('hbe.txt', 'w') as outfile:
            outfile.write(str(value))


def lowgamma_waves_callback(value):
    if value != 0:
        with open('lga.txt', 'w') as outfile:
            outfile.write(str(value))

def midgamma_waves_callback(value):
    if value != 0:
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
time.sleep(2)

while True:
    time.sleep(0.2)
