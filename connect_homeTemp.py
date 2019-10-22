# Complete project details at https://RandomNerdTutorials.com

try:
    import usocket as socket
except:
    import socket

from machine import Pin
import network
import myDetails

import esp
esp.osdebug(None)

import gc
gc.collect()

myWifi = myDetails.SetHomeWifi()
ssid = myWifi.ssid
password = myWifi.pwd

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
led.value(0)
green = Pin(5, Pin.OUT)
red = Pin(4, Pin.OUT)
