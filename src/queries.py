import urequests
import sys
from src.setup_time import setup_time
sys.path.append('../cfg')
from config import TARGET_HEADSIGN, LOCATION_LAT, LOCATION_LON, RADIUS, WIFI_SSID, WIFI_PASSWORD

url = "https://api.digitransit.fi/routing/v2/finland/gtfs/v1"

headers = {
	"digitransit-subscription-key": "",
	"Content-Type": "application/json"
}

def	save_stop_ids_to_list(data1, status_code):
	stop_ids = []

	if status_code == 200:
		for edge in data1['data']['stopsByRadius']['edges']:
			stop_id = edge['node']['stop']['gtfsId']
			if "HSL:" in stop_id:
				stop_ids.append(stop_id)
		print(f"{len(stop_ids)} stops fetched")
		return stop_ids
	else:
		print("Failed to fetch stop IDs")
		return []

def	query_stops_within_radius():
	# query of stops within radius
	query1 = """
	query GetStopsByRadius($lat: Float!, $lon: Float!, $radius: Int!) {
		stopsByRadius(lat: $lat, lon: $lon, radius: $radius) {
			edges {
				node {
					stop {
						gtfsId
						code
					}
				}
			}
		}
	}
	"""

	variables = {
		"lat": LOCATION_LAT,
		"lon": LOCATION_LON,
		"radius": RADIUS
	}

	resp1 = urequests.post(url, json={"query": query1, "variables": variables}, headers=headers)

	if resp1.status_code == 200:
		data1 = resp1.json()
		# print(json.dumps(data1, indent=2))
		stop_ids = save_stop_ids_to_list(data1, resp1.status_code)
	else:
		print(f"Failed to query stops. Query status code: {resp1.status_code}")
		sys.exit(1)

	resp1.close()
	return stop_ids

def	get_shortest_arrival_time(stop_ids):
	# get current time: seconds from midnight
	seconds_now = setup_time(3)

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

		resp = urequests.post(url, json={"query": query}, headers=headers)

		if resp.status_code == 200:
			data = resp.json()
			# print(f"\nStop: {stop_id}")
			stop_code = data['data']['stop']['code']
			print(f"\nStop: {stop_code}")
			stoptimes = data['data']['stop']['stoptimesWithoutPatterns']
			for st in stoptimes:
				if TARGET_HEADSIGN in st['headsign']:
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
			print(f"Query failed for stop {stop_id}")

		resp.close()
	return shortest_arrival_time
