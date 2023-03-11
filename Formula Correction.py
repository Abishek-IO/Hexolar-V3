import datetime
from datetime import date
import requests

parameters = "ALLSKY_SFC_SW_DWN"
latitude = input("Enter Latitude\n")
longitude = input("Enter Longitute\n")
Date = input("Enter date in YYYYMMDD format\n")
wattage = input("Enter Panel wattage in watts\n")

year = Date[0:4]
year = int(year)
month = Date[4:6]
month = int(month)
day = Date[6:8]
day = int(day)
my_date = date(year, month, day)
Previous_Date = my_date - datetime.timedelta(days=1)
Previous_Date = str(Previous_Date)
previous_year = Previous_Date[0:4]
previous_month = Previous_Date[5:7]
previous_day = Previous_Date[8:10]
date_before = previous_year+previous_month+previous_day
NextDay_Date = my_date + datetime.timedelta(days=1)
NextDay_Date = str(NextDay_Date)
next_year = NextDay_Date[0:4]
next_month = NextDay_Date[5:7]
next_day = NextDay_Date[8:10]
date_after = next_year+next_month+next_day

request_daily = "https://power.larc.nasa.gov/api/temporal/daily/point?parameters=" + parameters + "&community=RE&longitude=" + longitude + "&latitude=" + latitude + "&start=" + Date + "&end=" + Date + "&format=JSON"
response_daily = requests.get(request_daily).json()
api_response_daily = response_daily["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]
#print (api_response_daily)

insolation = api_response_daily[Date]
print ("Solar Insolation is " + str(insolation) + " KW-hr/m^2/day\n")
energy_produced = insolation*float(wattage)
print("Energy produced before temperature correction is " + str(energy_produced) + " Wh\n")

request_hourly = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + parameters + "&community=SB&longitude=" + longitude + "&latitude=" + latitude + "&start=" + Date + "&end=" + Date + "&format=JSON" 
response_hourly = requests.get(request_hourly).json()
api_response_hourly = response_hourly["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]

request_hourly_daybefore = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + parameters + "&community=SB&longitude=" + longitude + "&latitude=" + latitude + "&start=" + date_before + "&end=" + date_before + "&format=JSON"
response_hourly_daybefore = requests.get(request_hourly_daybefore).json()
api_response_hourly_daybefore = response_hourly_daybefore["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]
#print (api_response_hourly_daybefore)

irradiance_1am = api_response_hourly_daybefore[Date+"01"]
#print ("Solar irradiance at 1 AM is " + str(irradiance_1am) + " w/m^2")
irradiance_2am = api_response_hourly_daybefore[Date+"02"]
#print ("Solar irradiance at 2 AM is " + str(irradiance_2am) + " w/m^2")
irradiance_3am = api_response_hourly_daybefore[Date+"03"]
#print ("Solar irradiance at 3 AM is " + str(irradiance_3am) + " w/m^2")
irradiance_4am = api_response_hourly_daybefore[Date+"04"]
#print ("Solar irradiance at 4 AM is " + str(irradiance_4am) + " w/m^2")
irradiance_5am = api_response_hourly[Date+"05"]
#print ("Solar irradiance at 5 AM is " + str(irradiance_5am) + " w/m^2")
irradiance_6am = api_response_hourly[Date+"06"]
#print ("Solar irradiance at 6 AM is " + str(irradiance_6am) + " w/m^2")
irradiance_7am = api_response_hourly[Date+"07"]
#print ("Solar irradiance at 7 AM is " + str(irradiance_7am) + " w/m^2")
irradiance_8am = api_response_hourly[Date+"08"]
#print ("Solar irradiance at 8 AM is " + str(irradiance_8am) + " w/m^2")
irradiance_9am = api_response_hourly[Date+"09"]
#print ("Solar irradiance at 9 AM is " + str(irradiance_9am) + " w/m^2")
irradiance_10am = api_response_hourly[Date+"10"]
#print ("Solar irradiance at 10 AM is " + str(irradiance_10am) + " w/m^2")
irradiance_11am = api_response_hourly[Date+"11"]
#print ("Solar irradiance at 11 AM is " + str(irradiance_11am) + " w/m^2")
irradiance_12pm = api_response_hourly[Date+"12"]
#print ("Solar irradiance at 12 PM is " + str(irradiance_12pm) + " w/m^2")
irradiance_1pm = api_response_hourly[Date+"13"]
#print ("Solar irradiance at 1 PM is " + str(irradiance_1pm) + " w/m^2")
irradiance_2pm = api_response_hourly[Date+"14"]
#print ("Solar irradiance at 2 PM is " + str(irradiance_2pm) + " w/m^2")
irradiance_3pm = api_response_hourly[Date+"15"]
#print ("Solar irradiance at 3 PM is " + str(irradiance_3pm) + " w/m^2")
irradiance_4pm = api_response_hourly[Date+"16"]
#print ("Solar irradiance at 4 PM is " + str(irradiance_4pm) + " w/m^2")
irradiance_5pm = api_response_hourly[Date+"17"]
#print ("Solar irradiance at 5 PM is " + str(irradiance_5pm) + " w/m^2")
irradiance_6pm = api_response_hourly[Date+"18"]
#print ("Solar irradiance at 6 PM is " + str(irradiance_6pm) + " w/m^2")
irradiance_7pm = api_response_hourly[Date+"19"]
#print ("Solar irradiance at 7 PM is " + str(irradiance_7pm) + " w/m^2")
irradiance_8pm = api_response_hourly[Date+"20"]
#print ("Solar irradiance at 8 PM is " + str(irradiance_8pm) + " w/m^2")
irradiance_9pm = api_response_hourly[Date+"21"]
#print ("Solar irradiance at 9 PM is " + str(irradiance_9pm) + " w/m^2")
irradiance_10pm = api_response_hourly[Date+"22"]
#print ("Solar irradiance at 10 PM is " + str(irradiance_10pm) + " w/m^2")
irradiance_11pm = api_response_hourly[Date+"23"]
#print ("Solar irradiance at 11 PM is " + str(irradiance_11pm) + " w/m^2")
irradiance_12am = api_response_hourly[date_after+"00"]
#print ("Solar irradiance at 12 AM is " + str(irradiance_12am) + " w/m^2\n")

temperature_parameter = "T2M"
request_temperature_hourly = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + temperature_parameter + "&community=RE&longitude=" + longitude + "&latitude=" + latitude + "&start=" + Date + "&end=" + Date + "&format=JSON" 
response_hourly_temperature = requests.get(request_temperature_hourly).json()
api_response_temperature_hourly = response_hourly_temperature["properties"]["parameter"]["T2M"]
#print (api_response_temperature_hourly)

request_hourly_temperature_daybefore = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + temperature_parameter + "&community=RE&longitude=" + longitude + "&latitude=" + latitude + "&start=" + date_before + "&end=" + date_before + "&format=JSON"
response_hourly_temperature_daybefore = requests.get(request_hourly_temperature_daybefore).json()
api_response_hourly_temperature_daybefore = response_hourly_temperature_daybefore["properties"]["parameter"]["T2M"]

temperature_1am = api_response_hourly_temperature_daybefore[Date+"01"]
#print ("Temperature at 1 AM is " + str(temperature_1am) + " °C")
temperature_2am = api_response_hourly_temperature_daybefore[Date+"02"]
#print ("Temperature at 2 AM is " + str(temperature_2am) + " °C")
temperature_3am = api_response_hourly_temperature_daybefore[Date+"03"]
#print ("Temperature at 3 AM is " + str(temperature_3am) + " °C")
temperature_4am = api_response_hourly_temperature_daybefore[Date+"04"]
#print ("Temperature at 4 AM is " + str(temperature_4am) + " °C")
temperature_5am = api_response_temperature_hourly[Date+"05"]
#print ("Temperature at 5 AM is " + str(temperature_5am) + " °C")
temperature_6am = api_response_temperature_hourly[Date+"06"]
#print ("Temperature at 6 AM is " + str(temperature_6am) + " °C")
temperature_7am = api_response_temperature_hourly[Date+"07"]
#print ("Temperature at 7 AM is " + str(temperature_7am) + " °C")
temperature_8am = api_response_temperature_hourly[Date+"08"]
#print ("Temperature at 8 AM is " + str(temperature_8am) + " °C")
temperature_9am = api_response_temperature_hourly[Date+"09"]
#print ("Temperature at 9 AM is " + str(temperature_9am) + " °C")
temperature_10am = api_response_temperature_hourly[Date+"10"]
#print ("Temperature at 10 AM is " + str(temperature_10am) + " °C")
temperature_11am = api_response_temperature_hourly[Date+"11"]
#print ("Temperature at 11 AM is " + str(temperature_11am) + " °C")
temperature_12pm = api_response_temperature_hourly[Date+"12"]
#print ("Temperature at 12 PM is " + str(temperature_12pm) + " °C")
temperature_1pm = api_response_temperature_hourly[Date+"13"]
#print ("Temperature at 1 PM is " + str(temperature_1pm) + " °C")
temperature_2pm = api_response_temperature_hourly[Date+"14"]
#print ("Temperature at 2 PM is " + str(temperature_2pm) + " °C")
temperature_3pm = api_response_temperature_hourly[Date+"15"]
#print ("Temperature at 3 PM is " + str(temperature_3pm) + " °C")
temperature_4pm = api_response_temperature_hourly[Date+"16"]
#print ("Temperature at 4 PM is " + str(temperature_4pm) + " °C")
temperature_5pm = api_response_temperature_hourly[Date+"17"]
#print ("Temperature at 5 PM is " + str(temperature_5pm) + " °C")
temperature_6pm = api_response_temperature_hourly[Date+"18"]
#print ("Temperature at 6 PM is " + str(temperature_6pm) + " °C")
temperature_7pm = api_response_temperature_hourly[Date+"19"]
#print ("Temperature at 7 PM is " + str(temperature_7pm) + " °C")
temperature_8pm = api_response_temperature_hourly[Date+"20"]
#print ("Temperature at 8 PM is " + str(temperature_8pm) + " °C")
temperature_9pm = api_response_temperature_hourly[Date+"21"]
#print ("Temperature at 9 PM is " + str(temperature_9pm) + " °C")
temperature_10pm = api_response_temperature_hourly[Date+"22"]
#print ("Temperature at 10 PM is " + str(temperature_10pm) + " °C")
temperature_11pm = api_response_temperature_hourly[Date+"23"]
#print ("Temperature at 11 PM is " + str(temperature_11pm) + " °C")
temperature_12am = api_response_temperature_hourly[date_after+"00"]
#print ("Temperature at 12 AM is " + str(temperature_12am) + " °C")

wind_parameter = "WS10M"
request_wind_hourly = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + wind_parameter + "&community=RE&longitude=" + longitude + "&latitude=" + latitude + "&start=" + Date + "&end=" + Date + "&format=JSON"
response_hourly_wind = requests.get(request_wind_hourly).json()
api_response_wind_hourly = response_hourly_wind["properties"]["parameter"]["WS10M"]
#print (api_response_wind_hourly)

request_hourly_wind_daybefore = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + wind_parameter + "&community=RE&longitude=" + longitude + "&latitude=" + latitude + "&start=" + date_before + "&end=" + date_before + "&format=JSON"
response_hourly_wind_daybefore = requests.get(request_hourly_wind_daybefore).json()
api_response_hourly_wind_daybefore = response_hourly_wind_daybefore["properties"]["parameter"]["WS10M"]

wind_1am = api_response_hourly_wind_daybefore[Date+"01"]
#print ("Wind speed at 1 AM is " + str(wind_1am) + " m/s")
wind_2am = api_response_hourly_wind_daybefore[Date+"02"]
#print ("Wind speed at 2 AM is " + str(wind_2am) + " m/s")
wind_3am = api_response_hourly_wind_daybefore[Date+"03"]
#print ("Wind speed at 3 AM is " + str(wind_3am) + " m/s")
wind_4am = api_response_hourly_wind_daybefore[Date+"04"]
#print ("Wind speed at 4 AM is " + str(wind_4am) + " m/s")
wind_5am = api_response_wind_hourly[Date+"05"]
#print ("Wind speed at 5 AM is " + str(wind_5am) + " m/s")
wind_6am = api_response_wind_hourly[Date+"06"]
#print ("Wind speed at 6 AM is " + str(wind_6am) + " m/s")
wind_7am = api_response_wind_hourly[Date+"07"]
#print ("Wind speed at 7 AM is " + str(wind_7am) + " m/s")
wind_8am = api_response_wind_hourly[Date+"08"]
#print ("wind speed at 8 AM is " + str(wind_8am) + " m/s")
wind_9am = api_response_wind_hourly[Date+"09"]
#print ("Wind speed at 9 AM is " + str(wind_9am) + " m/s")
wind_10am = api_response_wind_hourly[Date+"10"]
#print ("Wind speed at 10 AM is " + str(wind_10am) + " m/s")
wind_11am = api_response_wind_hourly[Date+"11"]
#print ("Wind speed at 11 AM is " + str(wind_11am) + " m/s")
wind_12pm = api_response_wind_hourly[Date+"12"]
#print ("Wind speed at 12 PM is " + str(wind_12pm) + " m/s")
wind_1pm = api_response_wind_hourly[Date+"13"]
#print ("Wind speed at 1 PM is " + str(wind_1pm) + " m/s")
wind_2pm = api_response_wind_hourly[Date+"14"]
#print ("Wind speed at 2 PM is " + str(wind_2pm) + " m/s")
wind_3pm = api_response_wind_hourly[Date+"15"]
#print ("Wind speed at 3 PM is " + str(wind_3pm) + " m/s")
wind_4pm = api_response_wind_hourly[Date+"16"]
#print ("Wind speed at 4 PM is " + str(wind_4pm) + " m/s")
wind_5pm = api_response_wind_hourly[Date+"17"]
#print ("Wind speed at 5 PM is " + str(wind_5pm) + " m/s")
wind_6pm = api_response_wind_hourly[Date+"18"]
#print ("Wind speed at 6 PM is " + str(wind_6pm) + " m/s")
wind_7pm = api_response_wind_hourly[Date+"19"]
#print ("Wind speed at 7 PM is " + str(wind_7pm) + " m/s")
wind_8pm = api_response_wind_hourly[Date+"20"]
#print ("Wind speed at 8 PM is " + str(wind_8pm) + " m/s")
wind_9pm = api_response_wind_hourly[Date+"21"]
#print ("Wind speed at 9 PM is " + str(wind_9pm) + " m/s")
wind_10pm = api_response_wind_hourly[Date+"22"]
#print ("Wind speed at 10 PM is " + str(wind_10pm) + " m/s")
wind_11pm = api_response_wind_hourly[Date+"23"]
#print ("Wind speed at 11 PM is " + str(wind_11pm) + " m/s")
wind_12am = api_response_wind_hourly[date_after+"00"]
#print ("Wind speed at 12 AM is " + str(wind_12am) + " m/s")

humidity_parameter = "RH2M"
request_humidity_hourly = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + humidity_parameter + "&community=RE&longitude=" + longitude + "&latitude=" + latitude + "&start=" + Date + "&end=" + Date + "&format=JSON"
response_hourly_humidity = requests.get(request_humidity_hourly).json()
api_response_humidity_hourly = response_hourly_humidity["properties"]["parameter"]["RH2M"]

request_hourly_humidity_daybefore = "https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=" + humidity_parameter + "&community=RE&longitude=" + longitude + "&latitude=" + latitude + "&start=" + date_before + "&end=" + date_before + "&format=JSON"
response_hourly_humidity_daybefore = requests.get(request_hourly_humidity_daybefore).json()
api_response_hourly_humidity_daybefore = response_hourly_humidity_daybefore["properties"]["parameter"]["RH2M"]

humidity_1am = api_response_hourly_humidity_daybefore[Date+"01"]
#print ("Humidity at 1 AM is " + str(humidity_1am) + " %")
humidity_2am = api_response_hourly_humidity_daybefore[Date+"02"]
#print ("Humidity at 2 AM is " + str(humidity_2am) + " %")
humidity_3am = api_response_hourly_humidity_daybefore[Date+"03"]
#print ("Humidity at 3 AM is " + str(humidity_3am) + " %")
humidity_4am = api_response_hourly_humidity_daybefore[Date+"04"]
#print ("Humidity at 4 AM is " + str(humidity_4am) + " %")
humidity_5am = api_response_humidity_hourly[Date+"05"]
#print ("Humidity at 5 AM is " + str(humidity_5am) + " %")
humidity_6am = api_response_humidity_hourly[Date+"06"]
#print ("Humidity at 6 AM is " + str(humidity_6am) + " %")
humidity_7am = api_response_humidity_hourly[Date+"07"]
#print ("Humidity at 7 AM is " + str(humidity_7am) + " %")
humidity_8am = api_response_humidity_hourly[Date+"08"]
#print ("Humidity at 8 AM is " + str(humidity_8am) + " %")
humidity_9am = api_response_humidity_hourly[Date+"09"]
#print ("Humidity at 9 AM is " + str(humidity_9am) + " %")
humidity_10am = api_response_humidity_hourly[Date+"10"]
#print ("Humidity at 10 AM is " + str(humidity_10am) + " %")
humidity_11am = api_response_humidity_hourly[Date+"11"]
#print ("Humidity at 11 AM is " + str(humidity_11am) + " %")
humidity_12pm = api_response_humidity_hourly[Date+"12"]
#print ("Humidity at 12 PM is " + str(humidity_12pm) + " %")
humidity_1pm = api_response_humidity_hourly[Date+"13"]
#print ("Humidity at 1 PM is " + str(humidity_1pm) + " %")
humidity_2pm = api_response_humidity_hourly[Date+"14"]
#print ("Humidity at 2 PM is " + str(humidity_2pm) + " %")
humidity_3pm = api_response_humidity_hourly[Date+"15"]
#print ("Humidity at 3 PM is " + str(humidity_3pm) + " %")
humidity_4pm = api_response_humidity_hourly[Date+"16"]
#print ("Humidity at 4 PM is " + str(humidity_4pm) + " %")
humidity_5pm = api_response_humidity_hourly[Date+"17"]
#print ("Humidity at 5 PM is " + str(humidity_5pm) + " %")
humidity_6pm = api_response_humidity_hourly[Date+"18"]
#print ("Humidity at 6 PM is " + str(humidity_6pm) + " %")
humidity_7pm = api_response_humidity_hourly[Date+"19"]
#print ("Humidity at 7 PM is " + str(humidity_7pm) + " %")
humidity_8pm = api_response_humidity_hourly[Date+"20"]
#print ("Humidity at 8 PM is " + str(humidity_8pm) + " %")
humidity_9pm = api_response_humidity_hourly[Date+"21"]
#print ("Humidity at 9 PM is " + str(humidity_9pm) + " %")
humidity_10pm = api_response_humidity_hourly[Date+"22"]
#print ("Humidity at 10 PM is " + str(humidity_10pm) + " %")
humidity_11pm = api_response_humidity_hourly[Date+"23"]
#print ("Humidity at 11 PM is " + str(humidity_11pm) + " %")
humidity_12am = api_response_humidity_hourly[date_after+"00"]
#print ("Humidity at 12 AM is " + str(humidity_12am) + " %")

irradiance_dict = {1: irradiance_1am, 2: irradiance_2am, 3: irradiance_3am, 4: irradiance_4am, 5: irradiance_5am, 6: irradiance_6am, 7: irradiance_7am, 8: irradiance_8am, 9: irradiance_9am, 10: irradiance_10am, 11: irradiance_11am, 12: irradiance_12pm, 13: irradiance_1pm, 14: irradiance_2pm, 15: irradiance_3pm, 16: irradiance_4pm, 17: irradiance_5pm, 18: irradiance_6pm, 19: irradiance_7pm, 20: irradiance_8pm, 21: irradiance_9pm, 22: irradiance_10pm, 23: irradiance_11pm, 24: irradiance_12am}
#print(irradiance_dict)
#print("\n")
temperature_dict = {1: temperature_1am, 2: temperature_2am, 3: temperature_3am, 4: temperature_4am, 5: temperature_5am, 6: temperature_6am, 7: temperature_7am, 8: temperature_8am, 9: temperature_9am, 10: temperature_10am, 11: temperature_11am, 12: temperature_12pm, 13: temperature_1pm, 14: temperature_2pm, 15: temperature_3pm, 16: temperature_4pm, 17: temperature_5pm, 18: temperature_6pm, 19: temperature_7pm, 20: temperature_8pm, 21: temperature_9pm, 22: temperature_10pm, 23: temperature_11pm, 24: temperature_12am}
wind_dict = {1: wind_1am, 2: wind_2am, 3: wind_3am, 4: wind_4am, 5: wind_5am, 6: wind_6am, 7: wind_7am, 8: wind_8am, 9: wind_9am, 10: wind_10am, 11: wind_11am, 12: wind_12pm, 13: wind_1pm, 14: wind_2pm, 15: wind_3pm, 16: wind_4pm, 17: wind_5pm, 18: wind_6pm, 19: wind_7pm, 20: wind_8pm, 21: wind_9pm, 22: wind_10pm, 23: wind_11pm, 24: wind_12am}
humidity_dict = {1: humidity_1am, 2: humidity_2am, 3: humidity_3am, 4: humidity_4am, 5: humidity_5am, 6: humidity_6am, 7: humidity_7am, 8: humidity_8am, 9: humidity_9am, 10: humidity_10am, 11: humidity_11am, 12: humidity_12pm, 13: humidity_1pm, 14: humidity_2pm, 15: humidity_3pm, 16: humidity_4pm, 17: humidity_5pm, 18: humidity_6pm, 19: humidity_7pm, 20: humidity_8pm, 21: humidity_9pm, 22: humidity_10pm, 23: humidity_11pm, 24: humidity_12am}
for key, value in dict(irradiance_dict).items():
    if value == 0 and -999:
        del irradiance_dict[key]
        del temperature_dict[key]
        del wind_dict[key]
        del humidity_dict[key]
    elif value < 100.00:
        del irradiance_dict[key]
        del temperature_dict[key]
        del wind_dict[key] 
        del humidity_dict[key]           
#print (irradiance_dict)
#print("\n")
#print(temperature_dict) 
#print(wind_dict)
#print(humidity_dict)
irradiance_dict_original = irradiance_dict.copy()
irradiance_dict_original1 = irradiance_dict.copy()
temperature_dict_original = temperature_dict.copy()
temperature_dict_original1 = temperature_dict.copy()
wind_speed_original = wind_dict.copy()
total_sunshine = len(irradiance_dict)
print ("Total sunshine hours is " + str(total_sunshine) + " hrs\n")

noct = 47
half_formula = (noct - 20)/800
#print(half_formula)
for key in irradiance_dict:
    irradiance_dict[key] *= half_formula
#print (irradiance_dict) 
for key in temperature_dict:
    if key in irradiance_dict:
        temperature_dict[key] = temperature_dict[key] + irradiance_dict[key]
    else:
        pass
#print(temperature_dict)
tpo_dict = temperature_dict.copy()
#print(tpo_dict)
tpo_avg = sum(tpo_dict.values())/total_sunshine
#print (tpo_avg)
temperature_coefficient = 0.41
temperature_difference = tpo_avg - 25
rptc = temperature_difference * temperature_coefficient
print ("Reduction in power output after temperature is taken into consideration is " + str(rptc) + " %\n")
percentage_difference = 100-rptc
corrected_output = (energy_produced * percentage_difference)/100
print ("Energy produced after temperature correction is " + str(corrected_output) + " Wh\n")

for key in irradiance_dict_original:
    irradiance_dict_original[key] *= 0.293
#print (irradiance_dict_original)

for key in wind_dict:
    if key in irradiance_dict_original:
        irradiance_dict_original[key] = irradiance_dict_original[key] / (8.91 + (2.00 * wind_dict[key]))
    else:
        pass
#print(irradiance_dict_original)   

for key in temperature_dict_original:
    if key in irradiance_dict_original:
        temperature_dict_original[key] = temperature_dict_original[key] + irradiance_dict_original[key]
    else:
        pass    
#print(temperature_dict_original)        

tpo_wind_dict = temperature_dict_original.copy()
tpo_wind_avg = sum(tpo_wind_dict.values())/total_sunshine
#print (tpo_wind_avg)
temperature_difference_wind = tpo_wind_avg - 25
rptc_wind = temperature_difference_wind * temperature_coefficient
print ("Reduction in power output after temperature and wind speed are taken into consideration is " + str(rptc_wind) + " %\n")
percentage_difference_wind = 100-rptc_wind
corrected_output_wind = (energy_produced * percentage_difference_wind)/100
print ("Energy produced after temperature correction and wind speed is " + str(corrected_output_wind) + " Wh\n")

for key in irradiance_dict_original1:
    if key in temperature_dict_original1:
        if key in wind_speed_original:
            if key in humidity_dict:
                temperature_dict_original1[key] = 26.97 + (0.77 * temperature_dict_original1[key]) + 0.023 * (irradiance_dict_original1[key]) - (0.206 * humidity_dict[key]) - (0.137 * wind_speed_original[key])
            else:
                pass    
tpo_humidity_dict = temperature_dict_original1.copy()
tpo_humidity_avg = sum(tpo_humidity_dict.values())/total_sunshine
#print(tpo_humidity_avg)

temperature_difference_humidity = tpo_humidity_avg - 25
rptc_humidity = temperature_difference_humidity * temperature_coefficient
print ("Reduction in power output after temperature, wind speed and relative humidity are taken into consideration is " + str(rptc_humidity) + " %\n")
percentage_difference_humidity = 100-rptc_humidity
corrected_output_humidity = (energy_produced * percentage_difference_humidity)/100
print ("Energy produced after temperature correction, wind speed and relative humidity is " + str(corrected_output_wind) + " Wh\n")


