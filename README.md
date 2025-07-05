API:
Register in digitransit to get api key. Build GraphQL query with help of their tool below:
https://portal-api.digitransit.fi/api-details#api=routing-v2-finland-gtfs

Esptool:
Download esptool to flash microcontoller from git or via pipx:
sudo apt install pipx
pipx install esptool
pipx ensurepath
source ~/.bashrc
https://github.com/espressif/esptool

Microcontroller:
Download microcontroller ESP-32 micropython firmware:
https://micropython.org/download/ESP32_GENERIC/

install mpremote

Erase everything from the microcontroller
python3 -m esptool --port /dev/ttyUSB0 erase_flash
or
esptool.py --port /dev/ttyUSB0 erase_flash

Install new binary tool to the microcontroller
remember to be inside where esptool.py is
python3 -m esptool --baud 460800 write_flash 0x1000 ESP32_GENERIC-20250415-v1.25.0.bin
or
esptool.py --baud 460800 write_flash 0x1000 ESP32_GENERIC-20250415-v1.25.0.bin

Copy files to the microcontroller:
./replace.sh

Run the program
mpremote connect /dev/ttyUSB0 exec "exec(open('main.py').read())"

General connection
mpremote connect /dev/ttyUSB0

Find ttyusb
ls /dev/ttyUSB*
chmod 666 /dev/ttyUSB0
