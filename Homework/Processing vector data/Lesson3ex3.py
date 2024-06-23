from pyqgis_scripting_ext.core import *

folder = "C:/Users/Michele/OneDrive - Scientific Network South Tyrol/EMMA/Year 1/Advanced geomatics/"
geopackagePath = r"C:\Users\Michele\OneDrive - Scientific Network South Tyrol\EMMA\Year 1\Advanced geomatics\packages\natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
HMap.remove_layers_by_name(["OpenStreetMap"], ["centroids"])

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

schema = {
    "name": "string"
}

centroidsLayer = HVectorLayer.new("centroids", "Point", "EPSG:4326", schema)

countryLayer = HVectorLayer.open(geopackagePath, countriesName)

nonInCountryList = [] # Countries with centroids not inside the main polygon:
nameIndex = countryLayer.field_index("NAME")
for country in countryLayer.features():
    countryGeom = country.geometry
    name = country.attributes[nameIndex] 
    
    centroid = countryGeom.centroid()
    
    # we have geom and name and can create  a new feature. We can populate the centroid name

    centroidsLayer.add_feature(centroid, [name]) # We need a list so we create one and insert the name.

    if not centroid.intersects(countryGeom):
        nonInCountryList.append(name)

simpleStyle = HMarker("circle", 10) + HLabel("name") + HHalo()
centroidsLayer.set_style(simpleStyle)

HMap.add_layer(centroidsLayer)

print("Countries with centroids not inside the main polygon:")
for c in nonInCountryList:
    print(c)
    