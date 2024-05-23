#Exercise02
from pyqgis_scripting_ext.core import *

stationsPath = r"C:\Users\Michele\OneDrive - Scientific Network South Tyrol\EMMA\Year 1\Advanced geomatics\stations.txt"
with open (stationsPath, "r") as file:
    lines = file.readlines()

points = []
for line in lines[1:]:
    line = line.strip()
    lineSplit = line.split(",")
    if line.startswith("#") or len(line) == 0:
        continue
    # print(lineSplit)
    
    lat = lineSplit[3]
    lon = lineSplit[4]
    
    latSplit = lat.split(":")
    # print(latSplit)
    
    lat_deg = int(latSplit[0])
    lat_min = int(latSplit[1])/60
    lat_sec = int(latSplit[2])/3600
    
    newLat = float(lat_deg + lat_min + lat_sec)
    # print(newLat)
    
    lonSplit = lon.split(":")
    lon_deg = int(lonSplit[0])
    lon_min = int(lonSplit[1])/60
    lon_sec = int(lonSplit[2])/3600
    
    newLon = float(lon_deg + lon_min + lon_sec)
    # print(newLon)

    point = HPoint(newLon, newLat)
    points.append(point)
print(points[0])

crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)

Stations = []
for point in points:
    Point = crsHelper.transform(point)
    Stations.append(Point)

collection = HGeometryCollection(Stations)
hull = collection.convex_hull()

canvas = HMapCanvas.new()
for point in Stations: 
    canvas.add_geometry(point, "red", 2)

osm = HMap.get_osm_layer()
canvas.set_layers([osm])
canvas.set_extent(hull.bbox())
canvas.show()

# Dictionary to store the count of stations per country
stations_by_country = {}

with open(stationsPath, "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("#") or len(line) == 0:
            continue

        lineSplit = line.split(",")
        country = lineSplit[2].strip()
    
        stations_by_country[country] = stations_by_country.get(country, 0) + 1

for country, count in stations_by_country.items():
    print(f"{country}: {count}")