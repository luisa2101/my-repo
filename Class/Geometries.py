from pyqgis_scripting_ext.core import *

point = HPoint(30.0, 10.0)
print(point.asWkt())

# Create different types of geometry
# Longitude and latitude is the order to be kept always. 
coords = [[31, 11], [10, 30], [20,40], [40,40]]
line = HLineString.fromCoords(coords) 
print(line.asWkt())

#Polygon; coordinates should close on the same starting coordinates
coords = [[32,12], [10,20], [20,39], [40,39], [32,12]]
polygon = HPolygon.fromCoords(coords)
print(polygon.asWkt())

# Create a polygon with a hole inside
exteriorPoints = [[35,10],[10,20],[15,40],[45,45],[35,10]]
holePoints = [[20,30],[35,35],[30,20],[20,30]]
polygonWithHole = HPolygon.fromCoords(exteriorPoints)

holeRing = HLineString.fromCoords(holePoints)
polygonWithHole.add_interior_ring(holeRing)
print(polygonWithHole) # the result will show a list of coordinates separated by a comma

#Creating multi-geometries
coords = [[10, 40], [40, 30], [20, 20], [30, 10]]
multiPoints = HMultiPoint.fromCoords(coords)
print(multiPoints)

coords1 = [[10,10],[20,20],[10,40]]
coords2 = [[40,40],[30,30],[40,20],[30,10]]
multiLine = HMultiLineString.fromCoords([coords1, coords2])

# Multi-polygon
coords1 = [[30,20], [10,40], [45,40], [30,20]]
coords2 = [[15,5], [40,10], [10,20], [5,10], [15,5]]
multiPolygon = HMultiPolygon.fromCoords([coords1, coords2])

# Color the polygons with different colors
subGeometries = multiPolygon.geometries()
colorsList = ["red", "blue", "green"]

coordinates = polygon.coordinates()
for coord in coordinates:
    print(f"coord x = {coord[0]}/coord y = {coord[1]}")

# take a string and convert into geometry
wkt = "POINT (156 404)"
pointGeom = HGeometry.fromWkt(wkt)
print(pointGeom)

wkt = """
MULTIPOLYGON (((130 510, 140 450, 200 480, 210 570, 150 630, 130 560, 130 510)),
((430 770, 370 820, 210 860, 20 760, 35 631, 100 370, 108 363, 154 284, 230 380,
140 400, 150 440, 130 450, 104 585, 410 670, 440 590, 450 590, 430 770)))
"""
polygonGeom = HGeometry.fromWkt(wkt)


# canvas = HMapCanvas.new()
# for item in range(len(subGeometries)):
#     geom = subGeometries[item]
#     color = colorsList[item]
#     canvas.add_geometry(geom, color, 2)
    
    
#Visualize geometries
# canvas = HMapCanvas.new()
# canvas.add_geometry(point, "red", 2)# This does not show anything, we need to set it to an extent, which takes 4 coordinates --> canva set extent. The number represnets the thickness
# canvas.add_geometry(multiPolygon, "magenta", 5)
# canvas.add_geometry(multiLine, "blue", 5)
# canvas.add_geometry(multiPoints, "red", 15)
# canvas.add_geometry(line, "blue", 2)
# canvas.add_geometry(polygon, "green", 2)
# canvas.add_geometry(polygonWithHole, "magenta", 10)#
# canvas.set_extent([0, 0 , 50 ,50]) #x, y bottom left and x,y upper side right
# canvas.show()


