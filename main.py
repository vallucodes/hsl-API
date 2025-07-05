import time
import sys
from src.led import setColor
from src.wifi import connect_to_wifi
from src.queries import query_stops_within_radius, get_shortest_arrival_time
from cfg.config import WIFI_SSID, WIFI_PASSWORD

#wifi must be 2.4GHz for ESP32

def	main():

	setColor(0, 0, 0)
	connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)

	stop_ids = query_stops_within_radius()

	if not stop_ids:
		print("No HSL stops found in radius")
		sys.exit(1)

	while True:

		shortest_arrival_time = get_shortest_arrival_time(stop_ids)

		if shortest_arrival_time < 2:
			setColor(255,0, 0)
		elif shortest_arrival_time < 5:
			setColor(0,0, 255)
		else:
			setColor(0,250, 0)

		time.sleep(5)

main()
