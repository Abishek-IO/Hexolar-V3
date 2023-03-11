import json
import requests
import csv

PARAMETERS = "ALLSKY_SFC_SW_DWN,T2M,WS10M"
DATA_START_YEAR = 2020
DATA_END_YEAR = 2021

latitude = "15.3173"
longitude = "75.7139"

date = "01/01/2022"

req_date = date[0:2]
req_month = date[3:5]
req_year = date[6:10]

api_request = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + PARAMETERS + "&community=SB&longitude=" + longitude + "&latitude=" + latitude + "&start=" + str(DATA_START_YEAR) + "0101&end=" + str(DATA_END_YEAR) + "1231&format=JSON"
api_response = requests.get(api_request).json()

# sample_json_data = open('sample_multiple_data.json')
# api_response = json.load(sample_json_data)

irradiance_data = api_response["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]
temperature_data = api_response["properties"]["parameter"]["T2M"]
wind_data = api_response["properties"]["parameter"]["WS10M"]

hourly_data = []

def generate_hour_data(hour):
    sum_irradiance_data = 0
    sum_temperature_data = 0
    sum_wind_data = 0
    invalid_keys = 0

    for year in range(DATA_START_YEAR, DATA_END_YEAR + 1):
        data_key = str(year)+req_month+req_date+str(hour).zfill(2)
        if data_key not in irradiance_data: 
            invalid_keys += 1
            continue

        sum_irradiance_data += irradiance_data[data_key]
        sum_temperature_data += temperature_data[data_key]
        sum_wind_data += wind_data[data_key]

    avg_irradiance_data = sum_irradiance_data / (DATA_END_YEAR - DATA_START_YEAR - invalid_keys + 1)
    avg_temperature_data = sum_temperature_data / (DATA_END_YEAR - DATA_START_YEAR - invalid_keys + 1)
    avg_wind_data = sum_wind_data / (DATA_END_YEAR - DATA_START_YEAR - invalid_keys + 1)

    return round(avg_irradiance_data, 2), round(avg_temperature_data, 2), round(avg_wind_data, 2)

for hour in range(0, 24):
    irradiance, temperature, wind = generate_hour_data(hour)

    if irradiance >= 100:
        hourly_data.append([date, hour, irradiance, temperature, wind])

total_sunshine_hours = len(hourly_data)

# CSV Writing
header = ["Date", "Hour", "Irradiance Data", "Temperature Data", "Wind Data"]

with open('integrated_data.csv', 'w', encoding='UTF8') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(header)

    for hour_data in hourly_data:
        csv_writer.writerow(hour_data)
