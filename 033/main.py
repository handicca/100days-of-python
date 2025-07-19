import requests
from datetime import datetime

"""
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
iss_position = data.get("iss_position")
print(iss_position)
"""

parameters = {"lat": -6.917464, "lng": 107.619125, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", parameters)
response.raise_for_status()

sunset = response.json().get("results")["sunset"]
sunrise = response.json().get("results")["sunrise"]

print(sunset)
print(datetime.now())
