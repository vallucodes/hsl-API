# HSL API combined with microcontroller

Picture here of real world

Picture next to it with electrical scheme

## Overview

This program fetches nearby public transport stops in Helsinki with given **radius**, **longitude** and **latitude**. Based on given **destination** of the bus, LED will shine with certain color depending on time to arrival to that direction withing given **radius**.


| LED COLOR | Time to arrival |
|---|---|
| RED | < 2 minutes |
| BLUE | < 5 minutes |
| GREEN | >= 5 minutes |

## Features

Setup parameters in cfg/config.py

 - **headsign**
 - **latitude**
 - **longitude**
 - **radius**
 - **wifi name**
 - **wifi password**

## How to run

Setup parameters in cfg/config.py.

Find which tty USB is microcontrolles using. \
Replace `<nb>` with correct number
``` shell
ls /dev/ttyUSB*
chmod 666 /dev/ttyUSB<nb>
```

Erase everything from microcontroller
``` shell
esptool.py --port /dev/ttyUSB<nb> erase_flash
```

Flash microcontoller ESP-32
``` shell
esptool.py --baud 460800 write_flash 0x1000 ESP32_GENERIC-20250415-v1.25.0.bin
```

Copy program to the microcontoller
``` shell
./replace.sh
```

Run it by
``` shell
mpremote connect /dev/ttyUSB<nb> exec "exec(open('main.py').read())"
```

## Technical elements



## Dependencies

### Download
- Mpremote
- Esptool
- Microcontroller firmaware https://micropython.org/download/ESP32_GENERIC/

## Useful information

> [!TIP]
> Useful tip

Might have to run like this if esptool was installed by hand
``` shell
python3 -m esptool --port /dev/ttyUSB<nb> erase_flash
python3 -m esptool --baud 460800 write_flash 0x1000 ESP32_GENERIC-20250415-v1.25.0.bin
```

Any problems with wifi? It must be 2.4GHz. \
Still? Try running
``` shell
mpremote connect /dev/ttyUSB<nb> exec "exec(open('reset_network.py').read())"
```

### API
Register in digitransit to get api key. Build GraphQL query with help of their tool below:
https://portal-api.digitransit.fi/api-details#api=routing-v2-finland-gtfs

## Creators

- [Vladimir Lopatinski](https://github.com/vallucodes)
- [Matias Quero](https://github.com/kerito-cl)
- Saara-Leena Niemelä

