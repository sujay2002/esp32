#Erase Flash
esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART erase_flash

sleep 30


esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash -z 0x1000 esp32-idf3-20191220-v1.12.bin
