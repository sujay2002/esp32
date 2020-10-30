import network
import slimDNS as d
import _thread
sta_if = network.WLAN(network.STA_IF)
local_addr = sta_if.ifconfig()[0]
def testThread1():
	server = d.SlimDNSServer(local_addr, "micropython")
	server.advertise_hostname("tvpython.local")
	server.run_forever()

_thread.start_new_thread(testThread1, ())

