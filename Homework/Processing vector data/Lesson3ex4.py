from pyqgis_scripting_ext.core import *

folder = "C:/Users/Michele/OneDrive - Scientific Network South Tyrol/EMMA/Year 1/Advanced geomatics/"
geopackagePath = r"C:\Users\Michele\OneDrive - Scientific Network South Tyrol\EMMA\Year 1\Advanced geomatics\packages\natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
HMap.remove_layers_by_name(["OpenStreetMap"])

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

ranges = [
    [80000000, float('inf')], # from 80 million to infinite, or you can place  a number with many zeros
    [1000000, 80000000],
    [float('-inf'), 1000000],
]

styles = [
    HFill("255, 0, 0, 70"), # we use the RGB way of styling because we eant to establish also transparency 
    HFill("0, 255, 0, 70"),
    HFill("0, 0, 255, 70"),
]

labelStyle = HLabel("POP_EST") + HHalo()
countriesLayer.set_graduated_style("POP_EST", ranges, styles, labelStyle) # POP EST = field

HMap.add_layer(countriesLayer)

