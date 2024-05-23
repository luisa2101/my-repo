# Exercise 01
extent = 6

polygons = []

for lon in range(-180, 180, extent):
    minX = lon
    maxX = lon + extent
    minY = -84
    maxY = 84
    
    coords = [[minX, minY], [minX, maxY], [maxX, maxY], [maxX, minY], [minX, minY]]
    polygon = HPolygon.fromCoords(coords)
    polygons.append(polygon)

canvas = HMapCanvas.new()

# osm = HMap.get_osm_layer()
# canvas.set_layers([osm]) 
# #The problem is that the pojections are different from my drawing and the imported map. So we need to do a transformation.

for polygon in polygons:
    canvas.add_geometry(polygon)
    
canvas.set_extent([-180, -84, 180, 84])
canvas.show()