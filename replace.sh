#!/bin/bash

mpremote connect /dev/ttyUSB0 rm main.py reset_network.py

mpremote connect /dev/ttyUSB0 rm \
							src/led.py \
							src/queries.py \
							src/setup_time.py \
							src/time_ntp.py \
							src/wifi.py

mpremote connect /dev/ttyUSB0 rm cfg/config.py

mpremote connect /dev/ttyUSB0 rmdir src cfg

mpremote connect /dev/ttyUSB0 mkdir src
mpremote connect /dev/ttyUSB0 mkdir cfg

mpremote connect /dev/ttyUSB0 cp main.py reset_network.py :

mpremote connect /dev/ttyUSB0 cp cfg/config.py :cfg/config.py

mpremote connect /dev/ttyUSB0 cp src/led.py :src/led.py
mpremote connect /dev/ttyUSB0 cp src/queries.py :src/queries.py
mpremote connect /dev/ttyUSB0 cp src/setup_time.py :src/setup_time.py
mpremote connect /dev/ttyUSB0 cp src/time_ntp.py :src/time_ntp.py
mpremote connect /dev/ttyUSB0 cp src/wifi.py :src/wifi.py
