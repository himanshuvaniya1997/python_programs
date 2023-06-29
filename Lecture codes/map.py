def cube(x):
    return x*x*x

iterable = (1,2,3,4,5)

map_result = map(cube, iterable)
print(map_result)         #map fun return map object.
print(list(map_result))   #type casting = object to lits conversation. 