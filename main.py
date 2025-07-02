import json
import requests
from datetime import datetime

# Correct GraphQL endpoint for routing API
url = "https://api.digitransit.fi/routing/v2/finland/gtfs/v1"

headers = {
	"digitransit-subscription-key": "62640b56a6db4d0085cb7d08884990d4",
	"Content-Type": "application/json"
}

query = """{
	stop(id: "HSL:1111146") {
		name
		code
		gtfsId
		lat
		lon
		direction
		locationType
		stoptimesWithoutPatterns {
			realtimeArrival
			headsign
			trip {
				gtfsId
				route {
					shortName
					bikesAllowed
				}
			}
		}
	}
}"""


# Use POST for GraphQL queries
resp = requests.post(url, json={"query": query}, headers=headers)

print(f"Status code: {resp.status_code}")
# print(f"Response: {resp.text}")
data = resp.json()
# print(json.dumps(data, indent=2))

for
print(data["data"]["stop"]["stoptimesWithoutPatterns"][i]["headsign"])
