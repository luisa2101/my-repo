from pyqgis_scripting_ext.core import *

#g1
coords = [[0, 0], [0, 5], [5,5], [5,0], [0,0]]
g1 = HPolygon.fromCoords(coords) 
print(g1.asWkt())


#g2 
coords = [[7,0], [7,2], [5,2], [5,0], [7,0]]
g2 = HPolygon.fromCoords(coords)
print(g2.asWkt())

#g3
g3 = HPoint(4, 1)
print(g3.asWkt())

#g4
g4 = HPoint(5, 4)
print(g4.asWkt())

#g5
coords = [[1, 0], [1, 6]]
g5 = HLineString.fromCoords(coords) 
print(g5.asWkt())

#g6
coords = [[3,6], [6,6], [6,3], [3,3], [3,6]]
g6 = HPolygon.fromCoords(coords)
print(g6.asWkt())

#Bounding box
print("polygon boundingbox", g1.bbox())
print("-----------------------")
print("polygon length:", g1.length())
print("polygon area:", g1.area())
print("-----------------------")
print("line length:", g5.length())
print("line area:", g5.area()) 
print("-----------------------")
print("point length:", g3.length())
print("point area:", g3.area()) 
print("-----------------------")
#distance from the nearest point between two geometries 
print("distance between line and point:", g5.distance(g4))
print("-----------------------")
#PREDICATES -> functions returining true or false 
print("Intersects")
print(g1.intersects(g2)) # g2 is just touching, but it is considered anyways by the intersection
print(g1.intersects(g3))
print(g1.intersects(g4))
print(g1.intersects(g5))
print(g1.intersects(g6))
#All geometries intersect with g1
print("-----------------------")
print("Touches") 
# -> do not intersect their interior but have at least one point in common
print(g1.touches(g2))
print(g1.touches(g3))
print(g1.touches(g4))
print(g1.touches(g5))
print(g1.touches(g6)) 
print("-----------------------")
print("Contains")
print(g1.contains(g2))
print(g1.contains(g3)) 
print(g1.contains(g4)) 
print(g1.contains(g5)) 
print(g1.contains(g6))
print("-----------------------")
# FUNCTIONS - functions return an extra geometry
print("Intersection")
print(g1.intersection(g6))
print(g1.intersection(g2)) # touching polygons will give the line that they have in common
print(g1.intersection(g3)) # polygon and point will give the point itself
print(g1.intersection(g5)) # polygon and line -> line
newGeom = g1.intersection(g6)

print("symdifference")
print(g1.intersection(g6))
print(g1.intersection(g2)) 
print(g1.intersection(g3)) 
print(g1.intersection(g5)) 
newGeom = g1.symdifference(g6)

print("union")
print(g1.union(g6))
print(g1.union(g2)) 
print(g1.union(g3)) 
print(g1.union(g5)) 
newGeom = g1.union(g6)

print("difference") 
# - Mind the order when you use difference
print(g1.difference(g6)) 
newGeom = g1.difference(g6)

print(g6.difference(g1)) 
newGeom = g6.difference(g1)

print("buffers")
b1 = g3.buffer(1.0) # the buffer of a point
b2 = g3.buffer(1.0, 1) # the buffer of a point with few quandrant segments, because a buffer point is a series of segments, if we reduce the number of gragments we can se the segments. The default value should be 8.

b3 = g5.buffer(1.0) # line buffer
b4 = g5.buffer(1.0, 2) # line buffer with few points

# square end cap style (flat, square, round)
b5 = g5.buffer(1.0, -1, JOINSTYLE_ROUND, ENDCAPSTYLE_SQUARE)

# CONVEX HULL, with many geometries to know the bounding box. The "convex" will not mark the concavities of the shape, but creates a shape that covers all shapes, however a convex one.
collection = HGeometryCollection([g1, g2, g3, g4, g5, g6])
hull = collection.convex_hull()

canvas = HMapCanvas.new()
canvas.add_geometry(g1, "black", 2)
canvas.add_geometry(g2, "black", 2)
canvas.add_geometry(g3, "black", 2)
canvas.add_geometry(g4, "black", 2)
canvas.add_geometry(g5, "black", 2)
canvas.add_geometry(g6, "black", 2)
canvas.add_geometry(hull, "orange", 2)

canvas.set_extent(hull.bbox())

# canvas.add_geometry(g1, "black", 2)
# canvas.add_geometry(g2, "magenta", 2)
# canvas.add_geometry(g3, "blue", 5)
# canvas.add_geometry(g4, "red", 5)
# canvas.add_geometry(g5, "light green", 2)
# canvas.add_geometry(g6, "orange", 2)

# canvas.add_geometry(b1, "orange", 3)
# canvas.add_geometry(b2, "red", 3)
# canvas.add_geometry(b3, "green", 3)
# canvas.add_geometry(b4, "magenta", 3)
# canvas.add_geometry(b5, "cyan", 3)

# show the intercection geometry/the dfference between geometries
# canvas.add_geometry(newGeom, "magenta", 2)


canvas.set_extent([-1, -1 , 8 ,8]) #x, y bottom left and x,y upper side right
canvas.show()