# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import uos, machine
esp.osdebug(None)
#import webrepl
#webrepl.start()
import gc
gc.collect()
import network
import utime
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("sujayhub", "1161290982")
tmo = 50
while not sta_if.isconnected():
    utime.sleep_ms(100)
    tmo -= 1
    if tmo == 0:
        break

if sta_if.isconnected():
    try:
        mdns = network.mDNS()
        mdns.start("mPy","MicroPython with mDNS")
        _ = mdns.addService('_ftp', '_tcp', 21, "MicroPython", {"board": "ESP32", "service": "mPy FTP File transfer", "passive": "True"})
        _ = mdns.addService('_telnet', '_tcp', 23, "MicroPython", {"board": "ESP32", "service": "mPy Telnet REPL"})
        _ = mdns.addService('_http', '_tcp', 80, "MicroPython", {"board": "ESP32", "service": "mPy Web server"})
    except:
        print("mDNS not started")

import webrepl
webrepl.start()
import testserver
