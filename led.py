import board
import neopixel
import time, psutil

pixels = neopixel.NeoPixel(board.D18, 2)
pixels.fill((0, 0, 0))
oldLoad = 0;
newLoad = 0;

while True:

    newLoad = round(psutil.cpu_percent())

    time.sleep(.5)

    while oldLoad != newLoad:
        if oldLoad < newLoad:
            oldLoad += 1
        else:
            oldLoad -= 1
        pixels.fill((oldLoad*2.55, oldLoad/2, 255 - oldLoad*2.55))
        # pixels.fill((0, 0, 0))
        print(oldLoad, newLoad)
        time.sleep(.02)
        