import board
import neopixel
import time

pixels = neopixel.Neopixel(board.D18, 50, brightness = 1)
pixels.fill(0,0,0)

time.sleep(2)
pixels.fill(0,0,255)
pixels.show()