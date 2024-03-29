# based on https://github.com/Lepeshka92/TelegaGraph
import gc
import network
import myDetails

myWifi = myDetails.SetHomeWifi()

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(myWifi.ssid, myWifi.pwd)
    while not sta_if.isconnected():
        pass
    print('connected!')

gc.collect()
