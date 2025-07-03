import json
import requests
from datetime import datetime, timedelta
import time

url = "https://api.digitransit.fi/routing/v2/finland/gtfs/v1"

headers = {
	"digitransit-subscription-key": "62640b56a6db4d0085cb7d08884990d4",
	"Content-Type": "application/json"
}

target_headsign = "Tikkurila"
location_lat = 60.181
location_lon = 24.958

while True:
	# query of stops within radius
	query1 = """{
		stopsByRadius(lat:60.181, lon:24.958, radius:350) {
			edges {
				node {
					stop {
					gtfsId
					code
					}
				}
			}
		}
	}"""

	stop_ids = []
	resp1 = requests.post(url, json={"query": query1}, headers=headers)

	# print(f"Status code1: {resp1.status_code}")

	data1 = resp1.json()
	# print(json.dumps(data1, indent=2))

	if resp1.status_code == 200:
		data1 = resp1.json()
		for edge in data1['data']['stopsByRadius']['edges']:
			stop_id = edge['node']['stop']['gtfsId']
			stop_ids.append(stop_id)
	else:
		print("Failed to fetch stop IDs")

	# print("Stops fetched")
	# for i, stop_id in enumerate(stop_ids):
	# 	print(f"{stop_id}")

	# get current time
	now = datetime.now()
	seconds_now = now.hour * 3600 + now.minute * 60 + now.second

	# queries of each stop that is within radius
	queries = []
	shortest_arrival_time = 9999
	for stop_id in stop_ids:
		query = f"""{{ stop(id: "{stop_id}") {{
			name
			code
			stoptimesWithoutPatterns {{
				realtimeArrival
				headsign
				trip {{
					route {{
						shortName
					}}
				}}
			}}
		}} }}"""

		resp = requests.post(url, json={"query": query}, headers=headers)

		if resp.status_code == 200:
			data = resp.json()
			print(f"\nStop: {stop_id}")
			stop_code = data['data']['stop']['code']
			print(f"Stop code: {stop_code}")
			stoptimes = data['data']['stop']['stoptimesWithoutPatterns']
			for st in stoptimes:
				if target_headsign in st['headsign']:
					short_name = st['trip']['route']['shortName']
					arrival = st['realtimeArrival']
					diff = arrival - seconds_now
					if diff < 0:
						minutes_until_arrival = 0
					else:
						minutes_until_arrival = diff // 60
					print(f"Bus to {st['headsign']}: {short_name}, Arrival in {minutes_until_arrival} min")
					if (minutes_until_arrival < shortest_arrival_time):
						shortest_arrival_time = minutes_until_arrival
		else:
			print(f"Failed for stop {stop_id}")

	# print(shortest_arrival_time)
	if shortest_arrival_time < 1:
		print("Blink red")
	elif shortest_arrival_time < 3:
		print("Blink yellow")
	else:
		print("Blink green")

	time.sleep(5)
