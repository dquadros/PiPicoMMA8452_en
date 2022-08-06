# Using the MMA8452Q Accelerometer with the Raspberry Pi Pico

This repository has two MicroPython modules:

* MMA8452.py: defines a MMA8452 class to interface with the accelerometer
* demoAcel.py: demonstration using an OLED display

Components for using the demo:

* Raspberry Pi Pico
* OLED 128x64 display, with SSD1306 controller and I2C interface (standard address, 0x3C) 
* MMA8452Q accelerometer module (standard address, 0x1C)

The display and accelerometer module must be powered by 3.3V. The SDA signal from both should be connected to the GP8 pin in the Raspberry Pi Pico and the SCL signal to the GP9 pin. Pin SA0 of the accelerometer module should be connected to GND. 

Load in the Pi Pico:

* MicroPython interpreter 
* [driver SSD1306.py](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py)
* MMA8452.py
* demoAcel.py

In the demo three bars are shown to indicate the acceleration in the three axis, There is also a square with a dot to show the sensor's orientation.

More details at my blog:
https://raspico.blogspot.com/
