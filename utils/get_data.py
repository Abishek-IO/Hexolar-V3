from API.nasa import get_hourly_nasa_data
from API.esa import get_hourly_esa_data
from utils.days import get_days_in_month, get_next_date
from datetime import datetime
import json

start_time = ""
end_time = ""

def get_data(latitude, longitude, date, month):
  global start_time
  global end_time
  start_time = datetime.now()

  nasa_api_parameters = "T2M,RH2M,WS10M"
  nasa_api_response = []
  nasa_api_response = get_hourly_nasa_data(latitude, longitude, nasa_api_parameters, "20091231", "20141231")
  esa_api_response = get_hourly_esa_data(latitude, longitude, "2009", "2014")

  modify_esa_time(esa_api_response)
  processed_data =  process_data(nasa_api_response, esa_api_response)

  predicted_data = get_predicted_date_data(processed_data, date, month)
  
  for hour in range(0, 24):
    print(str(hour).zfill(2) + ": ", end="")
    print(predicted_data[str(hour).zfill(2)])

  end_time = datetime.now()
  delta = end_time - start_time
  print("Total time taken is", delta.total_seconds())

def modify_esa_time(esa_data):
  for data_index in range(len(esa_data)):
    esa_data[data_index]["time"] = increase_6_hours(esa_data[data_index]["time"][:8], esa_data[data_index]["time"][9:])

def increase_6_hours(date, time):
  if(time.startswith("18")):
    new_date, new_month, new_year = get_next_date(int(date[6:]), int(date[4:6]), int(date[:4]))
    return str(new_year) + str(new_month) + str(new_date) + ":" + "0000"

  if(time.startswith("19")):
    new_date, new_month, new_year = get_next_date(int(date[6:]), int(date[4:6]), int(date[:4]))
    return str(new_year) + str(new_month) + str(new_date) + ":" + "0100"

  if(time.startswith("20")):
    new_date, new_month, new_year = get_next_date(int(date[6:]), int(date[4:6]), int(date[:4]))
    return str(new_year) + str(new_month) + str(new_date) + ":" + "0200"

  if(time.startswith("21")):
    new_date, new_month, new_year = get_next_date(int(date[6:]), int(date[4:6]), int(date[:4]))
    return str(new_year) + str(new_month) + str(new_date) + ":" + "0300"

  if(time.startswith("22")):
    new_date, new_month, new_year = get_next_date(int(date[6:]), int(date[4:6]), int(date[:4]))
    return str(new_year) + str(new_month) + str(new_date) + ":" + "0400"

  if(time.startswith("23")):
    new_date, new_month, new_year = get_next_date(int(date[6:]), int(date[4:6]), int(date[:4]))
    return str(new_year) + str(new_month) + str(new_date) + ":" + "0500"

  return date + ":" + str(int(time[:2]) + 6).zfill(2) + "00"

def process_data(nasa_data, esa_data):
  data = {}

  for year in range(2010, 2015):
    year_data = {}

    for month in range(1, 13):
      month_data = {}

      for date in range(1, get_days_in_month(month, year) + 1):
        date_data = {}

        for hour in range(0, 24):
          nasa_key = str(year) + str(month).zfill(2) + str(date).zfill(2) + str(hour).zfill(2)
          esa_key = str(year) + str(month).zfill(2) + str(date).zfill(2) + ":" + str(hour).zfill(2) + "00"

          temperature = nasa_data["T2M"][nasa_key]
          relative_humidity = nasa_data["RH2M"][nasa_key]
          wind_speed = nasa_data["WS10M"][nasa_key]

          date_data[str(hour).zfill(2)] = {
            "temperature": temperature,
            "relative_humidity": relative_humidity,
            "wind_speed": wind_speed,
            "tilted_radiation": find_tilted_radiation(esa_data, esa_key)
          }

        month_data[str(date).zfill(2)] = date_data

      year_data[str(month).zfill(2)] = month_data

    data[str(year)] = year_data

  return data

def find_tilted_radiation(data, key):
  for each_data in data:
    if (each_data["time"] == key):
      return each_data["G(i)"]

def get_predicted_date_data(processed_data, date, month):
  data = {}

  for hour in range(0, 24):
    temperature_sum = 0
    relative_humidity_sum = 0
    wind_speed_sum = 0
    tilted_radiation_sum = 0

    for year in range(2010, 2015):
      temperature_sum += processed_data[str(year)][str(month).zfill(2)][str(date).zfill(2)][str(hour).zfill(2)]["temperature"]
      relative_humidity_sum += processed_data[str(year)][str(month).zfill(2)][str(date).zfill(2)][str(hour).zfill(2)]["relative_humidity"]
      wind_speed_sum += processed_data[str(year)][str(month).zfill(2)][str(date).zfill(2)][str(hour).zfill(2)]["wind_speed"]
      tilted_radiation_sum += processed_data[str(year)][str(month).zfill(2)][str(date).zfill(2)][str(hour).zfill(2)]["tilted_radiation"]

    data[str(hour).zfill(2)] = {
      "temperature": round(temperature_sum / 5, 2),
      "relative_humidity": round(relative_humidity_sum / 5, 2),
      "wind_speed": round(wind_speed_sum / 5, 2),
      "tilted_radiation": round(tilted_radiation_sum / 5, 2)
    }

  return data