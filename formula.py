import math
import numpy as np
import datetime
from datetime import date

tilt_angle = float(input("Enter PV module tilt angle\n"))
pv_azimuth = float(input("Enter PV module azimuth angle\n"))
#dhi = float(input("Enter Diffuse horizontal irradiance\n"))
ghi = float(input("Enter Global Horizontal irradiance\n"))
dni = float(input("Enter Direct normal irradiance\n"))
latitude = float(input("Enter latitude\n"))
longitude = float(input("Enter longitude\n"))
Date = input("Enter date in YYYYMMDD format\n")

year = Date[0:4]
year = int(year)
month = Date[4:6]
month = int(month)
day = Date[6:8]
day = int(day)
my_date = date(year, month, day)
days = float(my_date.strftime("%j"))

if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
    leap = float(366)
else :
    leap = float(365)

def sunpos(when, location, refraction):
    year, month, day, hour, minute, second, timezone = when
    latitude, longitude = location
    rad, deg = math.radians, math.degrees
    sin, cos, tan = math.sin, math.cos, math.tan
    asin, atan2 = math.asin, math.atan2
    rlat = rad(latitude)
    rlon = rad(longitude)
    greenwichtime = hour - timezone + minute / 60 + second / 3600
    daynum = (
        367 * year
        - 7 * (year + (month + 9) // 12) // 4
        + 275 * month // 9
        + day
        - 730531.5
        + greenwichtime / 24
    )
    mean_long = daynum * 0.01720279239 + 4.894967873
    mean_anom = daynum * 0.01720197034 + 6.240040768
    eclip_long = (
        mean_long
        + 0.03342305518 * sin(mean_anom)
        + 0.0003490658504 * sin(2 * mean_anom)
    )
    obliquity = 0.4090877234 - 0.000000006981317008 * daynum
    rasc = atan2(cos(obliquity) * sin(eclip_long), cos(eclip_long))
    decl = asin(sin(obliquity) * sin(eclip_long))
    sidereal = 4.894961213 + 6.300388099 * daynum + rlon
    hour_ang = sidereal - rasc
    elevation = asin(sin(decl) * sin(rlat) + cos(decl) * cos(rlat) * cos(hour_ang))
    azimuth = atan2(
        -cos(decl) * cos(rlat) * sin(hour_ang),
        sin(decl) - sin(rlat) * sin(elevation),
    )
    azimuth = into_range(deg(azimuth), 0, 360)
    elevation = into_range(deg(elevation), -180, 180)
    if refraction:
        targ = rad((elevation + (10.3 / (elevation + 5.11))))
        elevation += (1.02 / tan(targ)) / 60
    return (round(azimuth, 2), round(elevation, 2))
def into_range(x, range_min, range_max):
    shiftedx = x - range_min
    delta = range_max - range_min
    return (((shiftedx % delta) + delta) % delta) + range_min
if __name__ == "__main__":
    location = (latitude, longitude)
    when = (2010, 2, 1, 12, 18, 0, +5.5)
    azimuth, elevation = sunpos(when, location, True)
    print("Azimuth: ", azimuth)
    print("Elevation: ", elevation)
    elevation = 43.7 #change this accordingly
    azimuth = 168.42
    zenith = float(90 - elevation)
    #zenith = 69.06

dhi = ghi - (dni*np.cos(np.radians(zenith)))
print("DHI =",dhi)   

aoi = np.degrees(np.arccos((np.cos(np.radians(zenith))*np.cos(np.radians(tilt_angle)))+(np.sin(np.radians(zenith))*np.sin(np.radians(tilt_angle))*np.cos(np.radians(azimuth - pv_azimuth)))))
print ("AOI =",aoi)

a = np.cos(np.radians(aoi))
a = np.maximum(a, 0)
print("a =",a)

b = np.cos(np.radians(zenith))
b = np.maximum(b, np.cos(np.radians(85)))
print("b =",b)

kappa = 1.041 
z = np.radians(zenith)
e = ((dhi + dni) / dhi + kappa * (z ** 3)) / (1 + kappa * (z ** 3))
print("e =",e)

if (e>=1.000) and (e<=1.065):
    f11 = -0.0083
    f12 = 0.5877
    f13 = -0.0621
    f21 = -0.0596
    f22 = 0.0721
    f23 = -0.0220
elif (e>=1.065) and (e<=1.230):
    f11 = 0.1299
    f12 = 0.6826
    f13 = -0.1514
    f21 = -0.0189
    f22 = 0.0660
    f23 = -0.0289 
elif (e>=1.230) and (e<=1.500):
    f11 = 0.3297
    f12 = 0.4869
    f13 = -0.2211
    f21 = 0.0554
    f22 = -0.0640
    f23 = -0.0261
elif (e>=1.500) and (e<=1.950):
    f11 = 0.5682
    f12 = 0.1875
    f13 = -0.2951
    f21 = 0.1089
    f22 = -0.1519
    f23 = -0.0140
elif (e>=1.950) and (e<=2.800):
    f11 = 0.8730
    f12 = -0.3920
    f13 = -0.3616
    f21 = 0.2256
    f22 = -0.4620
    f23 = 0.0012
elif (e>=2.800) and (e<=4.500):
    f11 = 1.1326
    f12 = -1.2367
    f13 = -0.4118
    f21 = 0.2878
    f22 = -0.8230
    f23 = 0.0559 
elif (e>=4.500) and (e<=6.200):
    f11 = 1.0602
    f12 = -1.5999
    f13 = -0.3589
    f21 = 0.2642
    f22 = -1.1272
    f23 = 0.1311
else:
    f11 = 0.6777
    f12 = -0.3273
    f13 = -0.2504
    f21 = 0.1561
    f22 = -1.3765
    f23 = 0.2506                           


amo = 1/np.cos(np.radians(zenith))
print ("AMO =",amo)

B = (2*np.pi*days)/leap
print ("B =",B)

rav = (1.00011 + 0.034221 * np.cos(B) + 0.00128 * np.sin(B) + 0.000719 * np.cos(2 * B) + 7.7e-05 * np.sin(2 * B))
print("Rav =",rav)

ea = 1367*rav
print("ea =",ea)

delta = (dhi*amo)/ea
print("Delta =",delta)

F1 = (f11 + (f12 * delta) + (f13 * z))
F1 = np.maximum(F1, 0)
print("F1 =",F1)

F2 = (f21 + (f22 * delta) + (f23 * z))
print("F2 =",F2)

term1 = 0.5 * (1 - F1) * (1 + np.cos(np.radians(tilt_angle)))
term2 = F1 * (a / b)
term3 = F2 * np.sin(np.radians(tilt_angle))
sky_diffuse = np.maximum(dhi * (term1 + term2 + term3), 0)
print("perez DHI =",sky_diffuse)

trig_dhi = dhi*(np.sin(np.radians(elevation + tilt_angle)))
print("Trignometric DHI =",trig_dhi)

isotropic_dhi = dhi * (1 + np.cos(np.radians(tilt_angle))) * 0.5
print("Isotropic DHI =",isotropic_dhi)

tt1 = (0.012 * zenith) - 0.04
tt2 = (1 - np.cos(np.radians(tilt_angle)))
tt3 = tt1 * tt2 * 0.5
sandia_dhi = isotropic_dhi + (ghi * tt3)
print("sandia DHI =",sandia_dhi)

ai = dni/ea
rb = np.cos(np.radians(aoi))/np.cos(np.radians(zenith))
t1 = 1-ai
t2 = 0.5 * (1 + np.cos(np.radians(tilt_angle)))
hay_1 = dhi * t1 * t2
hay_2 = dhi * (ai * rb)
haydavies = hay_1 + hay_2
print("Hay Davies DHI =",haydavies)

ttt1 = 1-ai
ttt2 = 0.5 * (1 + np.cos(np.radians(tilt_angle)))
ttt2_1 = (dni * np.cos(np.radians(zenith)))/ghi
ttt3 = 1 + np.sqrt(ttt2_1) * (np.sin(np.radians(0.5 * tilt_angle))**3)
aii = ai * np.cos(np.radians(aoi))
rbb = (1 + np.cos(np.radians(tilt_angle))) * 0.5 
ttt4 = (aii + (ttt1 * rbb))
reindl = (dhi * (ttt4 * ttt3))
print("reindl DHI =",reindl)
