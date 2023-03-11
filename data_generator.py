# import json
import requests
import csv

PARAMETER = "ALLSKY_SFC_SW_DWN"
DATA_START_YEAR = 2020
DATA_END_YEAR = 2021

latitude = input("Enter latitude: ")
longitude = input("\nEnter longitude: ")

date = input("\nEnter date for which data is required (DD/MM/YYYY): ")

# latitude = "77.6011776"
# longitude = "12.959744"

# date = "06/10/2022"

req_date = date[0:2]
req_month = date[3:5]
req_year = date[6:10]

api_request = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + PARAMETER + "&community=SB&longitude=" + longitude + "&latitude=" + latitude + "&start=" + str(DATA_START_YEAR) + "0101&end=" + str(DATA_END_YEAR) + "1231&format=JSON"
api_response = requests.get(api_request).json()

# sample_json_data = open('sample_data.json')
# api_response = json.load(sample_json_data)

hourly_data = api_response["properties"]["parameter"][PARAMETER]

req_data = []

def generate_hour_data(hour):
    sum_hour_data = 0

    for year in range(DATA_START_YEAR, DATA_END_YEAR + 1):
        data_key = str(year)+req_month+req_date+str(hour).zfill(2)
        sum_hour_data += hourly_data[data_key]

    avg_hour_data = sum_hour_data / (DATA_END_YEAR - DATA_START_YEAR)

    return round(avg_hour_data, 2)

for hour in range(0, 24):
    current_hour = [date, hour, generate_hour_data(hour)]
    req_data.append(current_hour)

header = ['Date', 'Hour', PARAMETER + ' Data']

with open('sample_data.csv', 'w', encoding='UTF8') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(header)

    for hour_data in req_data:
        csv_writer.writerow(hour_data)
