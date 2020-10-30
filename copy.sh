#!/bin/bash
ampy --port /dev/tty.SLAB_USBtoUART put boot.py
echo -e "copied boot.py"
ampy --port /dev/tty.SLAB_USBtoUART put install_pkg.py
echo -e "copied install_pkg.py"
ampy --port /dev/tty.SLAB_USBtoUART put switch_data.json
echo -e "copied switch data"
ampy --port /dev/tty.SLAB_USBtoUART reset
sleep 10s
ampy --port /dev/tty.SLAB_USBtoUART run install_pkg.py
echo -e "running install package"
sleep 20s
ampy --port /dev/tty.SLAB_USBtoUART put testserver.py
echo -e "copied testserver.py"
echo -e " going to reset the circuit"
ampy --port /dev/tty.SLAB_USBtoUART reset

sleep 30s


