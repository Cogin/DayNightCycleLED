from ctypes.wintypes import RGB
from urllib import response
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
import json
from flask_cors import CORS, cross_origin
import board
import neopixel
RGB = [0,0,0]
pixels = neopixel.NeoPixel(board.D18, 50, brightness = 1)
CORS(app)

@app.route('/',methods = ['POST', 'GET'])
def rgb(): 
    global RGB
    if request.method == 'POST':
        print(request)
        print(request.json)
        RGB = request.json
        print(RGB['RGB'])
        print(type(RGB['RGB']))
       	pixels.fill((int(RGB['RGB'][1]),int(RGB['RGB'][0]),int(RGB['RGB'][2])))
        print(RGB)
        return 'OK'
        return '200'
    if request.method == 'GET':
        return 'got'

app.run(debug = True, host='0.0.0.0')
