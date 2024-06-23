# ----------------- COVID CASES ------------------

from pyqgis_scripting_ext.core import *

# ----------------- FOLDERS ----------------------

# folder = "/Users/rominalavarello/Downloads"
folder = "C:/Users/Michele/OneDrive - Scientific Network South Tyrol/EMMA/Year 1/Advanced geomatics"
geopackagePath = folder + "/packages/natural_earth_vector.gpkg"
provincesName = "ne_10m_admin_1_states_provinces"

# data = "/Users/rominalavarello/Desktop/Group4"
# data = r"C:\Users\Michele\OneDrive - Scientific Network South Tyrol\EMMA\Year 1\Advanced geomatics"
# dataPath = folder + "/Covid_data/dpc-covid19-ita-regioni.csv"
dataPath = folder + "/dpc-covid19-ita-regioni.csv"

outputFolder = f"{folder}/tmp/output"
# -----------------------------------------------
HMap.remove_layers_by_name(["ne_10m_admin_1_states_provinces"])

provincesLayer = HVectorLayer.open(geopackagePath, provincesName)
provincesLayer.subset_filter("iso_a2='IT'")

HMap.add_layer(provincesLayer)

# create a dictionary containing the region name and its geometry
regionName2GeometryMap = {}
regionIndex = provincesLayer.field_index("region")
for provinceFeature in provincesLayer.features():
    geometry = provinceFeature.geometry
    regionName = provinceFeature.attributes[regionIndex]
    
    regionGeometry = regionName2GeometryMap.get(regionName)
    if regionGeometry:
        regionGeometry = regionGeometry.union(geometry)
    else:
        regionGeometry = geometry
    
    regionName2GeometryMap[regionName] = regionGeometry

for name, geom in regionName2GeometryMap.items():
    print(name)

# get the data out of csv and match to the region data
with open(dataPath, 'r') as file:
    lines = file.readlines()

day2featuresMap = {} #key: day, value: list for each region of values region name, total cases  
for index, line in enumerate(lines): #returns item and index
    line = line.strip()

    if index < 5000:
        lineSplit = line.split(",")
        # 0 -> date
        # 3 -> region
        # 17 -> total cases
        # 4, 5 -> lat, lon
        
        dayAndTime = lineSplit[0]
        dayAndTimeSplit = dayAndTime.split("T")
        day = dayAndTime[0]
        
        if day.endswith("01"): # 1st of the month for every region
            region = lineSplit[3]
            totalCases = int(lineSplit[17])
            
            lat = float(lineSplit[4])
            lon = float(lineSplit[5])
            dataPoint = HPoint(lon, lat)
            
            for regionName, regionGeometry in regionName2GeometryMap.items():
                if regionGeometry.intersects(dataPoint): 
                    featuresList = day2featuresMap.get(day)
                    if featuresList: #if different than none so it exist, create a list
                        featuresList.append((regionGeometry, [day, region, totalCases]))
                    else: 
                        featuresList = [(regionGeometry, [day, region, totalCases])]
                    day2featuresMap[day] = featuresList
        
imagePathList = []
for day, featuresList in day2featuresMap.items():
    # if day != "2020-04-01":
    #     continue
    
    print("Generating day", day)
    newLayerName = "covid_italy"
    HMap.remove_layer_by_name(newLayerName)
    
    schema = {
        "day":"string",
        "region":"string",
        "totcases":"int"
    }
    covidLayer = HVectorLayer.new(newLayerName, "MultiPolygon", "EPSG:4326", schema)
    
    for geometry, attributes in featuresList:
        covidLayer.add_feature(geometry, attributes)
        
    # style = HFill('yellow') + HStroke('black', 0.5)
    # covidLayer.set_style(style)
    
    ranges = [
        [float('-inf'), 1000],
        [1001, 3000],
        [3001, 10000],
        [10001, 40000],
        [40001, 100000],
        [100001, float('inf')]
    ]
    styles = [
        HFill('yellow') + HStroke('white', 0.5),
        HFill('green') + HStroke('white', 0.5),
        HFill('blue') + HStroke('white', 0.5),
        HFill('orange') + HStroke('white', 0.5),
        HFill('red') + HStroke('white', 0.5),
        HFill('black') + HStroke('white', 0.5),
    ]
    
    labelStyle = HLabel('totcases', size = 8, color = 'black'), + HHalo()
    covidLayer.set_graduated_style("totcases", ranges, styles, labelStyle)
    
    HMap.add_layer(covidLayer)
    
    printer = HPrinter(iface)
    mapProperties = {
        "x": 5, 
        "y": 25,
        "width": 285,
        "height": 180,
        "frame": True,
        "extent": provincesLayer.bbox()
    }
    printer.add_map(**mapProperties)
        
    legendProp = {
        "x": 210,
        "y": 30,
        "width": 150,
        "height": 100,
        "frame": True
    }
    printer.add_legend(**legendProp)
    
    labelProperties = {
        "x": 120, 
        "y": 10,
        "text": "COVID Italy, Total Cases",
        "bold": True
    }
    printer.add_label(**labelProperties)
    
    labelProperties = {
        "x": 120, 
        "y": 10,
        "text": day,
        "size": 28,
        "bold": True
    }
    printer.add_label(**labelProperties)
        
    imageName = f"{day}_covid.png" #png performs better than jpg in this case
    imagePath = f"{outputFolder}/{imageName}"
    printer.dump_to_image(imagePath)
    imagePathsList.append(imagePath)
        
        # printer.dump_to_image(imagePath)
        # imagePathList.append(imagePath)
        # disable data to create animation. Get hold of all images further at the top imagePathList
        
#generate final animation
# generate animation
import pip 
pip.main(['install','pillow'])

from PIL import Image

imagesList = []
for path in imagePathList:
    img = Image.open(path)
    imagesList.append(img)

animationPath = f"{outputFolder}/covid_animation.gif"

imagesList[0].save(animationPath, save_all=True, append_images = imagesList[1:], duration=500, loop=2)

for path in imagePathList:
    os.remove(path)