import upip
import utime

upip.install('picoweb')
utime.sleep(20)
upip.install('micropython-ulogging')
utime.sleep(10)
upip.install('micropython-uasyncio')
utime.sleep(10)
upip.install('micropython-pkg_resources')

