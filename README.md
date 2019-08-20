# microPython

A Playground for [Arduino](#arduino-tricks) and [ESP](#esp-tricks) code

---

# ESP tricks

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

## Server

**Upload boot files**
Upload file to connect to WiFi
> ampy --port PATH_TO_MODULE put connect.py boot.py

Upload file with webpage
> ampy --port PATH_TO_MODULE put server.py main.py

---

# Arduino tricks
