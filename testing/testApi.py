#This file is for testing API without microcontroller

import json
import requests
from  time import sleep
from datetime import datetime

# Correct GraphQL endpoint for routing API
url = "https://api.digitransit.fi/routing/v2/finland/gtfs/v1"

headers = {
    "digitransit-subscription-key": "62640b56a6db4d0085cb7d08884990d4",
    "Content-Type": "application/json"
}

target_headsign = "Munkki"
location_lat = 60.196
location_lon = 24.884
radius = 350

query = """
query GetStopsByRadius($lat: Float!, $lon: Float!, $radius: Int!) {
	stopsByRadius(lat: $lat, lon: $lon, radius: $radius) {
		edges {
			node {
				stop {
					gtfsId
					code
					name
					routes {
						agency{
							gtfsId
							name
							url
							phone
						}
					}
				}
			}
		}
	}
}
"""

variables = {
	"lat": location_lat,
	"lon": location_lon,
	"radius": radius
}

resp = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
data = resp.json()
print(json.dumps(data, indent=2))
stop_id = ""
# for d in data2:
#   if (d["stoptimesWithoutPatterns"])

#print(resp2.json())
# Use POST for GraphQL queries

while True:
	resp = requests.post(url, json={"query": query}, headers=headers)

	print(f"Status code: {resp.status_code}")
	# print(f"Response: {resp.text}")
	data = resp.json()
	data = data["data"]["stop"]["stoptimesWithoutPatterns"]
	buses_to_rauta = {}
	for d in data:
		if d["headsign"] == "Rautatientori":
		bus_number = d["trip"]["route"]["shortName"]
		buses_to_rauta[bus_number] = d["realtimeArrival"]
		#print(d["realtimeArrival"])
		#print(
	print(buses_to_rauta)

	sleep(5)
