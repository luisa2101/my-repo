from pyqgis_scripting_ext.core import *
filePath = r"C:\Users\Michele\OneDrive - Scientific Network South Tyrol\EMMA\Year 1\Advanced geomatics\stations.txt"

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

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
    
fields = {
    "Id": "Integer",
    "Name": "String",
    "Country": "String",
    "Height": "Integer"
}

stationsLayer = HVectorLayer.new("test", "Point", "EPSG:4326", fields)    

with open(filePath,"r")as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()#remove spaces

    if line.startswith("#") or len(line) == 0:
        continue
    
    lineSplit = line.split(",")
    
    latString = lineSplit[3]
    lonString = lineSplit[4]
    
    latDec = fromLatString(latString)
    lonDec = fromLonString(lonString)
    
    
    stationsLayer.add_feature(HPoint(lonDec, latDec), [lineSplit[0].strip(), lineSplit[1].strip(), lineSplit[2].strip(), lineSplit[5].strip()])

folder = "C:/Users/Michele/OneDrive - Scientific Network South Tyrol/EMMA/Year 1/Advanced geomatics/"
path = folder + "Stations.gpkg"
error = stationsLayer.dump_to_gpkg(path, overwrite=True)
if(error):
    print(error)