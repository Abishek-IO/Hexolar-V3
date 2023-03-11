import requests
parameters = "SI_EF_TILTED_SURFACE"
latitude = input("Enter Latitude\n")
longitude = input("Enter Longitute\n")



request_hourly = "https://power.larc.nasa.gov/api/temporal/climatology/point?parameters=" + parameters + "&community=SB&longitude=" + longitude + "&latitude=" + latitude + "&format=JSON" + "&start=2018" + "&end=2019"  

print(request_hourly)
response_hourly = requests.get(request_hourly).json()
print(response_hourly)
api_response_hourly = response_hourly["properties"]["parameter"]["SI_EF_TILTED_SURFACE_OPTIMAL_ANG"]
api_response_hourly1 = response_hourly["properties"]["parameter"]["SI_EF_TILTED_SURFACE_OPTIMAL_ANG_ORT"]
print(api_response_hourly)
print(api_response_hourly1)
