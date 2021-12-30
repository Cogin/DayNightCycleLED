import datetime
import board
import neopixel
import time
import random


Red=34  # Red starting color 1-255.
Green=45  # Green starting color 1-255.
Blue=54  # Blue starting color 1-255.
RedSpeed=3  # Red change speed 1-10. Default is 1.
GreenSpeed=2  # Green change speed 1-10. Default is 1.
BlueSpeed=1  # Blue change speed 1-10. Default is 1.
Tickspeed=4  # Speed at which the color updates take place.

# Maths, dont change unless to change the min and max ranges
yn=input('Print Values? y/n\n')
if input('Random Numbers? y/n\n') == 'y':
    seed=input('Input seed, (Can be anything)\n')
    random.seed(seed)
    Red = random.randint(1, 254)
    Blue = random.randint(1, 254)
    Green = random.randint(1, 254)
    RedSpeed = random.randint(1, 8)
    BlueSpeed = random.randint(1, 8)
    GreenSpeed = random.randint(1, 8)
TRedSpeed=RedSpeed
TGreenSpeed=GreenSpeed
TBlueSpeed=BlueSpeed
RedMrange=254 - RedSpeed
BlueMrange=254 - BlueSpeed
GreenMrange=254 - RedSpeed
RedLrange=1 + RedSpeed
BlueLrange=1 + BlueSpeed
GreenLrange=1 + GreenSpeed
# Tick Calculator
dorf='0.'
Tick=dorf.ljust(Tickspeed, '0')
Tick=(Tick + '1')
print(Tick)
Tick=float(Tick)


# Color Calc
def RLoop():
    global Red
    global RedSpeed
    global TRedSpeed
    Red=Red + RedSpeed
    if Red in range(RedMrange, 255):
        RedSpeed=(-TRedSpeed)
    if Red in range(1, RedLrange):
        RedSpeed=TRedSpeed


def BLoop():
    global Blue
    global BlueSpeed
    global TBlueSpeed
    Blue=Blue + BlueSpeed
    if Blue in range(BlueMrange, 255):
        BlueSpeed=(-TBlueSpeed)
    if Blue in range(1, BlueLrange):
        BlueSpeed=TBlueSpeed


def GLoop():
    global Green
    global GreenSpeed
    global TGreenSpeed
    Green=Green + GreenSpeed
    if Green in range(GreenMrange, 255):
        GreenSpeed=(-TGreenSpeed)
    if Green in range(1, GreenLrange):
        GreenSpeed=TGreenSpeed

try:
    pixels = neopixel.NeoPixel(board.D18, 50, brightness = 1)
    pixels.fill((0,0,0))
    B = 0
    G = 53
    R = 5
    while True:
        for i in range(50):
            RLoop()
            GLoop()
            BLoop()
            time.sleep(0.05)
            pixels[i] = (Green,Red,Blue)









except KeyboardInterrupt as error:
    time.sleep(0.5)
    print(error)
    pixels.fill((0,0,0))
    exit()
