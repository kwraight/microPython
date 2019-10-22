# microPython

A Playground for [Arduino](#arduino-tricks) and [ESP](#esp-tricks) code

**Useful links**
* [tutorial](http://docs.micropython.org/en/v1.9.4/esp8266/esp8266/tutorial/intro.html)
* [basic “operating system” services](https://docs.micropython.org/en/latest/library/uos.html)
* [online uploader](http://micropython.org/webrepl/)

## Quick recipe
1. upload boot.py file (and any supporting files for import)
> /opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/ampy --port /dev/tty.SLAB_USBtoUART put repositories/microPython/connect_homeTemp.py boot.py

2. upload main.py file (and any supporting files for import)
> /opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/ampy --port /dev/tty.SLAB_USBtoUART put repositories/microPython/server_homeTemp.py main.py

3. monitor with picocom
> picocom /dev/tty.SLAB_USBtoUART -b115200
* reset (bootoin or commande) ESP once connected

---

# ESP tricks

* [General Recipe](#general-recipe-to-use-ESP-module)
* [Server Example](#server-example)

## General recipe to use ESP module

**Connect module via USB and check for connection**
* Mac/Linux:
  > ls -ltr /dev/tty\*

  * will be recent, e.g. *tty.SLAB_USBtoUART* (mac) or */dev/ttyUSB0* (linux)
  * make sure it is writable, if necessary:
    > sudo chmod a+rw /dev/ttyUSB0

* Windows: Probably com port 3

**Get esptool**
> sudo python -m install esptool


**Wipe firmware from module**
> esptool.py --port PATH_TO_MODULE erase_flash

**Upload new firmware**
* Download latest stable *.bin* file from [here](http://micropython.org/download#esp8266), **NB** use correct module type, e.g. 8266, 32
  > esptool.py  --port PATH_TO_MODULE --baud 460800 write_flash --flash_size=detect 0 PATH_TO_BIN_FILE

  * esp32 requires some extra flags (see [page](http://micropython.org/download#esp32)): 
  > esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 PATH_TO_BIN_FILE

**Install commandline interface**
* Mac/Linux: picocom
  > sudo yum install picocom

  > picocom PATH_TO_MODULE -b115200

* Windows: TeraTerm: https://tera-term.en.lo4d.com/windows
	* Open and choose serial port (e.g. COM3)
  * Set baud rate to 115200 (settings>choose serial)

**Install ampy**
> sudo python -m pip install adafruit-ampy

**Run/upload code without interface**
* run code
  > ampy --port PATH_TO_MODULE run file.py

* upload code
  > ampy --port PATH_TO_MODULE put sourceName.py destinationName.py

  * Windows: add delay time (0.1 above) may need some playing with (0.1…0.5)

## Server Example

**Upload boot files**
Upload file to connect to WiFi
> ampy --port PATH_TO_MODULE put connect.py boot.py

**Upload file with webpage**
> ampy --port PATH_TO_MODULE put server.py main.py

**Monitor for IP and debugging**
* Connect to device via picocom
* Reset device (press "EN" button)
* Get module IP from terminal output
  > E.g. ('192.168.1.223', '255.255.255.0', '192.168.1.254', '192.168.1.254')

  * 192.168.1.223 is the IP here

---

## Green and Red LED Toggler
Two button webpage for toggling green and red LEDs independently
* LEDs connected to ESP GPIO pins 5 (D1) & 4 (D2)

**Upload boot files**
Upload file to connect to WiFi, e.g.:
> ampy --port PATH_TO_MODULE put connect_GreenRed.py boot.py

**Upload credentials**
Upload file to get WiFi credentials required by connect file, e.g.:
> ampy --port PATH_TO_MODULE put myDetails.py myDetails.py

**Upload file with webpage**
Upload file with webpage layout and functions, e.g.:
> ampy --port PATH_TO_MODULE put server_GreenRed.py main.py

## Popularity Poll
Webpage for counting clicks:

* bootfile
> ampy --port PATH_TO_MODULE put connect_work.py boot.py

* credentials
> ampy --port PATH_TO_MODULE put myDetails.py myDetails.py

* webpage
> ampy --port PATH_TO_MODULE put server_work.py main.py


# Arduino tricks
