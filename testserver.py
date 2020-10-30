import picoweb
import ubinascii
from machine import Pin
import network
import ujson
import utime
import _thread
sta_if = network.WLAN(network.STA_IF)
local_addr = sta_if.ifconfig()[0]
relay = Pin(17, Pin.OUT)
relay.on()
relay1 = Pin(16, Pin.OUT)
relay1.on()
app = picoweb.WebApp(__name__)
def require_auth(func):

    def auth(req, resp):
        auth = req.headers.get(b"Authorization")
        if not auth:
            yield from resp.awrite(
                'HTTP/1.0 401 NA\r\n'
                'WWW-Authenticate: Basic realm="Picoweb Realm"\r\n'
                '\r\n'
            )
            return

        auth = auth.split(None, 1)[1]
        auth = ubinascii.a2b_base64(auth).decode()
        req.username, req.passwd = auth.split(":", 1)
        yield from func(req, resp)

    return auth
@app.route("/")
@require_auth
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello World")
    #picoweb.jsonify(resp,{"message":"Hello World"})
@app.route("/on0")
def on0(req,resp):
    yield relay.off()
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Switch ON")
    yield wr_fp(0,0)
@app.route("/off0")
def off0(req,resp):
    yield relay.on()
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Switch OFF")
    yield wr_fp(0,1)
@app.route("/on1")
def on1(req,resp):
    yield relay1.off()
    yield from picowb.start_response(resp)
    yield from resp.awrite("switch on")
    yield from utime.sleep(2)
    yield wr_fp(1,0)
@app.route("/off1")
def off1(req,resp):
    yield relay1.on()
    yield from picoweb.start_response(resp)
    yield from resp.awrite("switch off")
    yield from utime.sleep(2)
    yield wr_fp(1,1)
def wr_fp(switch,value):
    fp = open('switch_data.json','r+')
    extract = ujson.load(fp)
    str_sw = "state" + str(switch)
    extract["data"][switch][str_sw] = value
    fp.seek(0)
    fp.write(ujson.dumps(extract))
    fp.truncate()
    fp.close()    
fp = open('switch_data.json' , 'r+')
extract = ujson.load(fp)
status = extract["data"][0]["state0"]
relay.value(status)
utime.sleep(1)
status1 = extract["data"][1]["state1"]
relay1.value(status1)
fp.close()
#def testThread():
app.run(debug=True, host=local_addr)
#_thread.start_new_thread(testThread, ())
