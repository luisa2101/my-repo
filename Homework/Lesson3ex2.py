from pyqgis_scripting_ext.core import *

geopackagePath = r"C:\Users\Michele\OneDrive - Scientific Network South Tyrol\EMMA\Year 1\Advanced geomatics\packages\natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

# print("Schema (first 4 fields):")
counter = 0
for name, type in countriesLayer.fields.items():
    counter += 1
    if counter < 5:
        print("\t", name,"of type", type)

# print("Attributes for France:")
nameIndex = countriesLayer.field_index("NAME") # This is case sensitive, if i write "name" this will show an error as -1
countriesFeatures = countriesLayer.features()

for feature in countriesFeatures: # Feature = geometric + attribute table part. 
    name = feature.attributes[nameIndex]
    if name == "France":
        geomFrance = feature.geometry
        # print("Geom:", geometry.asWkt()[:50] + "...")

# print(geometry)

crsHelper = HCrs()
crsHelper.from_srid(4326) # Lat lon coordinates
crsHelper.to_srid(3857)
geometry3857 = crsHelper.transform(geomFrance)

#####################################
citiesName = "ne_50m_populated_places"
citiesLayer = HVectorLayer.open(geopackagePath, citiesName)
        
nameIndex = citiesLayer.field_index("NAME") # This is case sensitive, if i write "name" this will show an error as -1
citiesFeatures = citiesLayer.features()

for feature in citiesFeatures: # Feature = geometric + attribute table part. 
    geometryCities = feature.geometry
    if geomFrance.contains(geometryCities):#these are all the cities
        print(geometryCities)
  
# define cities of france only and reproject those

canvas = HMapCanvas.new()
osm = HMap.get_osm_layer()
canvas.set_layers([osm])

crsHelper = HCrs()
crsHelper.from_srid(4326) # Lat lon coordinates
crsHelper.to_srid(3857)
geometryCities3857 = crsHelper.transform(geometryCities)

canvas.add_geometry(geometry3857)
canvas.add_geometry(geometryCities3857)
canvas.set_extent(geometry3857.bbox())
canvas.show()