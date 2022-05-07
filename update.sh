# erase flash_size
echo " ### erase ### "
esptool.py --port /dev/tty.wchusbserial1410 erase_flash
# set flash
echo " ### flash ### "
esptool.py --port /dev/tty.wchusbserial1410 --baud 460800 write_flash --flash_size=detect 0 ~/Downloads/esp8266-20190125-v1.10.bin
# upload
echo " ### boot ### "
/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/ampy --port /dev/tty.wchusbserial1410 -d1 put ~/repositories/microPython/tele_boot.py boot.py
echo " ### main ### "
/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/ampy --port /dev/tty.wchusbserial1410 -d1 put ~/repositories/microPython/tele_main.py main.py
echo " ### api ### "
/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/ampy --port /dev/tty.wchusbserial1410 -d1 put ~/repositories/microPython/tele_api.py tele_api.py
echo " ### details ### "
/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/ampy --port /dev/tty.wchusbserial1410 -d1 put ~/repositories/microPython/myDetails.py myDetails.py
echo " ### bots ### "
/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/ampy --port /dev/tty.wchusbserial1410 -d1 put ~/repositories/microPython/myBots.py myBots.py

echo " ### done!"
