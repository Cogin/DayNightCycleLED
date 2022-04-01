from ctypes.wintypes import RGB
from urllib import response
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
import json
from flask_cors import CORS
import board
import neopixel
RGB = [0,0,0]
pixels = neopixel.NeoPixel(board.D18, 50, brightness = 1)
CORS(app)

@app.route('/rgb',methods = ['POST', 'GET'])
def rgb():
    if request.method == 'POST':
        RGB = request.json
        print(RGB['RGB'])
        print(type(RGB['RGB']))
        pixels.fill((RGB['RGB'][1],RGB['RGB'][0],RGB['RGB'][2]))
        return 'OK'
        return '200'
    if request.method == 'GET':
        return RGB

app.run(debug = True)