import requests

def get_hourly_nasa_data(latitude, longitude, api_parameters, start_date, end_date):
  request = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + api_parameters + "&community=RE&longitude=" + str(longitude) + "&latitude=" + str(latitude) + "&start=" + start_date + "&end=" + end_date + "&format=JSON"
  response = requests.get(request).json()

  return response["properties"]["parameter"]