import requests

def get_hourly_esa_data(latitude, longitude, start_year, end_year):
  request = "https://re.jrc.ec.europa.eu/api/v5_2/seriescalc?lat=" + str(latitude) + "&lon=" + str(longitude) + "&raddatabase=PVGIS-ERA5&outputformat=json&angle=28&aspect=0&startyear=" + start_year + "&endyear=" + end_year + "&select_database_hourly=PVGIS-ERA5&hstartyear=" + start_year + "&hendyear=" + end_year + "&trackingtype=0&hourlyangle=28&hourlyaspect=0"
  response = requests.get(request).json()

  return response["outputs"]["hourly"]