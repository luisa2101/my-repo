from pyqgis_scripting_ext.core import *

# Necessary functions
def fromLatString(latString):
    sign = latString[0]
    latDegrees = float(latString[1:3]) # 3 excluded
    latMinutes = float(latString[4:6])
    latSeconds = float(latString[7:9])
    lat = latDegrees + latMinutes/60 + latSeconds/3600
    if sign == "-":
        lat = lat *-1
    return lat
    
def fromLonString(lonString):
    sign = lonString[0]
    lonDegrees = float(lonString[1:4])
    lonMinutes = float(lonString[5:7])
    lonSeconds = float(lonString[8:10])
    lon = lonDegrees + lonMinutes/60 + lonSeconds/3600
    if sign == "-":
        lon = lon *-1
    return lon

# Script start
lon = 11.34999
lat = 46.49809

stationsPath = r"C:\Users\Michele\Desktop\my-repo\data\stations.txt"
centrePoint = HPoint(lon, lat)

with open (stationsPath, "r") as file:
    lines = file.readlines()

minDistance = 9999
nearestStationName = "none"
nearestDistancePoint = None

for line in lines[1:10]: #Skip the first line because are not numbers so it will give error for float
    line = line.strip()
    
    lineSplit = line.split(",")
    name = lineSplit[1].strip()
    latString = lineSplit[3]
    lonString = lineSplit[4]
    
    latDec = fromLatString(latString)
    lonDec = fromLonString(lonString)
    # print(name, latDec, lonDec)
    point = HPoint(lonDec, latDec)
    
    distance = point.distance(centrePoint)
    if distance < minDistance:
        minDistance = distance
        nearestStationName = name
        nearestDistancePoint = point

print(nearestStationName, "->", nearestDistancePoint)
    