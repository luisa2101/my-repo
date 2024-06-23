# --- CLASS 6 AND 7-----

from pyqgis_scripting_ext.core import *

folder = "C:/Users/Michele/OneDrive - Scientific Network South Tyrol/EMMA/Year 1/Advanced geomatics"

gpkgPATH = folder + r"\packages\natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"
riversName = "ne_10m_rivers_lake_centerlines_scale_rank"
tempfolder = r"C:\Users\Michele\OneDrive - Scientific Network South Tyrol\EMMA\Year 1\Advanced geomatics\tmp"

HMap.remove_layers_by_name(["OpenStreetMap", countriesName, citiesName, riversName, "rivers_italy"])

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

citiesLayer = HVectorLayer.open(gpkgPATH, citiesName)

citiesLayer.subset_filter("SOV0NAME='Italy'")   ## filtering in a layer

# STYLING:
# marker: (shape, size, rotation)
# fill: rgb code or directly the "color" + transparency
# stroke: (color, thickness)
pointStyle = HMarker("square",3,45) + \
                HFill("red") + HStroke("brown",0.5)

#labels
field = "NAME"
# pointStyle += HLabel(field,yoffset=-6) + HHalo("white",1)

field = "if(POP_MAX>1000000, concat(NAME, ' (', round(POP_MAX/1000000,1), ')'), NAME)"


labelProperties = {
    "font": "Arial",
    "color": "darkgreen",
    "size": 12,
    "field": field,
    "xoffset": 0,
    "yoffset": -6
}

pointStyle += HLabel(**labelProperties) + HHalo("white",1)


citiesLayer.set_style(pointStyle)

# Polygon layer
countriesLayer = HVectorLayer.open(gpkgPATH, countriesName)
countriesLayer.subset_filter("NAME='Italy'")
italyGEOM = countriesLayer.features()[0].geometry

polygonStyle = HFill("190,207,80,150") + HStroke("black",1)
countriesLayer.set_style(polygonStyle)

# New Layer
riversLayer = HVectorLayer.open(gpkgPATH, riversName)
riversLayerItaly = riversLayer.sub_layer(italyGEOM,"rivers_italy",['scalerank','name'])    # it creates a new layer: geom, namenewlayer, fieldstomaintain

ranges = [
    [0,0],
    [1,5],
    [6,7],
    [8,9],
    [10,11]
]

styles = [
    HStroke("blue",5),
    HStroke("blue",4),
    HStroke("blue",3),
    HStroke("blue",2),
    HStroke("blue",1)
]

labelStyle = HLabel (**labelProperties) + HHalo("white",1)

riversLayerItaly.set_graduated_style('scalerank', ranges, styles, labelStyle)

# lineStyle = HStroke("lightcyan",1)

# labelProperties = {
#     "font": "Arial",
#     "color": "darkblue",
#     "size": 14,
#     "field": 'name',
#     "along_line": True,      
#     "bold": True,
#     "italic": True
# }


# lineStyle += labelStyle
# riversLayerItaly.set_style(lineStyle + labelStyle)


HMap.add_layer(countriesLayer)
HMap.add_layer(riversLayerItaly)
HMap.add_layer(citiesLayer)

#PDF LAYOUT
# Change QGIS coordinates to EPSG:4326 to sjow map

printer = HPrinter(iface)
mapProperties = {
    "x": 5,
    "y": 25,
    "width": 285,
    "height": 180,
    "extent": [10,44,12,46],
    "frame":True
}

labelProperties = {
    "x": 120,
    "y": 10,
    "text": "River and cities map",
    "font_size": 28,
    "bold": True,
    "italic": False
    
}

legendProperties = {
    "x": 215, # mm
    "y": 30,
    "width": 150,
    "height": 100,
    "max_symbol_size": 3
}

scalebarProperties = {
    "x": 10,
    "y": 190,
    "units": "km",
    "segments": 4,
    "unit_per_segment": 10,
    "style": "Single Box",
    "font_size": 12
}


printer.add_map(**mapProperties)
printer.add_label(**labelProperties)
printer.add_legend(**legendProperties)
printer.add_scalebar(**scalebarProperties)


outputPdf = f"{tempfolder}/test.pdf"
printer.dump_to_pdf(outputPdf)

outputpng = f"{tempfolder}/test.png"
printer.dump_to_image(outputpng)