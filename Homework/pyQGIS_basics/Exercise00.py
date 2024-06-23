# Exercise 00
from pyqgis_scripting_ext.core import *

geomPath = r"C:\Users\Michele\Desktop\my-repo\data\02_exe0_geometries.csv"
with open (geomPath, "r") as file:
    lines = file.readlines()

mylines = []
mypolygons = []

for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    lineSplit = line.split(";")
    # print(lineSplit)
    
    shape = lineSplit[0]
    #print(shape)

    coordinates = lineSplit[1]
    # print(coordinates)
    
    # print(shape, ":", coordinates)
    if shape == "point":
        longitude = float(coordinates[0:4])
        latitude = float(coordinates[5:])
        point = HPoint(longitude,latitude)
        # print(point.asWkt())

    if shape == "line":
        lat_lon = coordinates.split(" ")
        for item in lat_lon:
            lat_lon1 = item.split(",")
            longitude = float(lat_lon1[0])
            latitude = float(lat_lon1[1])
            mylines.append([longitude,latitude])
             
        linea = HLineString.fromCoords(mylines) 
        # print(linea.asWkt())
        
    if shape == "polygon":
        lat_lon = coordinates.split(" ")
        pointList = []
        for item in lat_lon:
            split = item.split(",")
            longitude = float(split[0])
            latitude = float(split[1])
            pointList.append((longitude, latitude))
        polygon = HPolygon.fromCoords(pointList)
        mypolygons.append(polygon)
    
print(mypolygons)
    
canvas = HMapCanvas.new()
canvas.add_geometry(point, "green", 15)
canvas.add_geometry(linea, "red", 2)
for polygon in mypolygons:
    canvas.add_geometry(polygon, "orange", 2)
canvas.set_extent([0, 0 , 50 ,50]) #x, y bottom left and x,y upper side right
canvas.show()