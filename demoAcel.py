'''
MMA9452 sensor use demonstration
(C) 2021, Daniel Quadros

Licença: Beerware license (http://en.wikipedia.org/wiki/Beerware)
'''
from machine import I2C
from time import sleep
from MMA8452 import MMA8452
import ssd1306

# Uses standard I2C configuration
i2c = I2C(0)

# Init the display
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.rect (80, 0, 30, 30, 1)
display.show()

# Init the sensor
sensor = MMA8452(i2c)
if not sensor.begin():
    print ("Sensor not found")
    quit()
sensor.active()
sensor.setupPL()
oldpos = -1

# Convert reading to coordinate
# Assumes reading between -1g and +1g
def conv(acel):
    coord = int ((acel+1)*31)
    if coord > 63:
        coord = 63
    elif coord < 0:
        coord = 0
    return coord

# Forever while it lasts
while True:
    # Time between readings
    sleep (0.3)

    # Tests if orientation changed
    acel = sensor.getCalclulatedAcel()
    newpos = sensor.readPL()
    if newpos != oldpos:
        # Changed, show new orientation
        display.fill_rect (81, 1, 28, 28, 0)
        if newpos == sensor.LOCKOUT:
            display.fill_rect (93, 13, 4, 4, 1)
        elif newpos == sensor.LANDSCAPE_R:
            display.fill_rect (83, 13, 4, 4, 1)
        elif newpos == sensor.LANDSCAPE_L:
            display.fill_rect (103, 13, 4, 4, 1)
        elif newpos == sensor.PORTRAIT_U:
            display.fill_rect (93, 3, 4, 4, 1)
        elif newpos == sensor.PORTRAIT_D:
            display.fill_rect (93, 23, 4, 4, 1)
        oldpos = newpos
        
    # Show acceleration (assumes between -1g and +1g)
    x = conv(acel[0])
    y = conv(acel[1])
    z = conv(acel[2])
    display.rect (0, 0, 64, 10, 1)
    display.fill_rect (1, 1, 62, 8, 0)
    if x < 32:
        display.fill_rect (x+1, 1, 33-x, 8, 1)
    else:
        display.fill_rect (32, 1, x-31, 8, 1)
    display.rect (0, 20, 64, 10, 1)
    display.fill_rect (1, 21, 62, 8, 0)
    if y < 32:
        display.fill_rect (y+1, 21, 33-y, 8, 1)
    else:
        display.fill_rect (32, 21, y-31, 8, 1)
    display.rect (0, 40, 64, 10, 1)
    display.fill_rect (1, 41, 62, 8, 0)
    if z < 32:
        display.fill_rect (z+1, 41, 33-z, 8, 1)
    else:
        display.fill_rect (32, 41, z-31, 8, 1)
    display.show()

