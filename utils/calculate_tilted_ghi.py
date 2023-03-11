import numpy as np
import csv
from datetime import datetime, timedelta
from utils.days import get_day_no_in_year, get_days_in_month
from API.nasa import get_hourly_nasa_data

LOCAL_STANDARD_MERIDIAN_TIME = 82.5

def write_to_csv(csv_header, csv_rows):
  with open('data/tilted-ghi.csv', 'w+', encoding='UTF8') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(csv_header)

    for row in csv_rows:
      csv_writer.writerow(row)
    
def calculate_tilted_ghi(latitude, longitude, month, year, slope, albedo):
  csv_header = ["Date", "Time", "Tilted GHI"]
  csv_rows = []

  days_in_month = get_days_in_month(month, year)

  api_parameters = "ALLSKY_SFC_SW_DIFF,ALLSKY_SFC_SW_DWN"
  api_response = get_hourly_nasa_data(month, year, latitude, longitude, api_parameters)

  dhi_data = api_response["ALLSKY_SFC_SW_DIFF"]
  ghi_data = api_response["ALLSKY_SFC_SW_DWN"]

  for date in range(1, days_in_month + 1):
    day_number = get_day_no_in_year(date, month, year)

    solar_declination = 23.45 * np.sin(np.radians(360 * (day_number + 284) / 365))

    equation_of_timeX = 360 * (day_number - 1) / 365.242
    equation_of_time = 0.258 * np.cos(np.radians(equation_of_timeX)) - 7.416 * np.sin(np.radians(equation_of_timeX)) - 3.648 * np.cos(np.radians(2 * equation_of_timeX)) - 9.228 * np.sin(np.radians(2 * equation_of_timeX))

    for hour in range(24):
      currentHour = datetime(year, month, date, hour, 0, 0, 0)
      solar_time_difference = 4 * (longitude - LOCAL_STANDARD_MERIDIAN_TIME) + equation_of_time
      local_solar_time_with_seconds = currentHour + timedelta(minutes=solar_time_difference)
      local_solar_time = datetime(year, month, date, local_solar_time_with_seconds.hour, local_solar_time_with_seconds.minute)

      difference_lst_noon_in_seconds = (local_solar_time - datetime(year, month, date, 12, 0, 0, 0)).total_seconds()
      difference_lst_noon_in_minutes = difference_lst_noon_in_seconds / 60
      hour_angle = difference_lst_noon_in_minutes * 15 / 60

      cosine_zenith_angle = np.sin(np.radians(latitude)) * np.sin(np.radians(solar_declination)) + np.cos(np.radians(solar_declination)) * np.cos(np.radians(latitude)) * np.cos(np.radians(hour_angle))

      angle_of_incidence_of_radiation_on_surface = np.sin(np.radians(latitude - slope)) * np.sin(np.radians(solar_declination)) + np.cos(np.radians(latitude - slope)) * np.cos(np.radians(solar_declination)) * np.cos(np.radians(hour_angle))

      tilt_factor_for_direct_irradiance = angle_of_incidence_of_radiation_on_surface / cosine_zenith_angle

      tilt_factor_for_diffuse_irradiance = (1 + np.cos(np.radians(slope))) / 2

      tilt_factor_for_reflected_irradiance = albedo * (1 - np.cos(np.radians(slope))) / 2

      data_key = str(year) + str(month).zfill(2) + str(date).zfill(2) + str(hour).zfill(2)
      [ghi, dhi] =  [ghi_data[data_key], dhi_data[data_key]]

      tilted_ghi = (ghi - dhi) * tilt_factor_for_direct_irradiance + dhi * tilt_factor_for_diffuse_irradiance + ghi * tilt_factor_for_reflected_irradiance

      csv_rows.append([data_key[:-2], data_key[-2:], tilted_ghi])

  write_to_csv(csv_header, csv_rows)

  return 0
