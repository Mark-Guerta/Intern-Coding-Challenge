from math import sin, acos, cos,radians,pow
def haversineFormula(coord1, coord2):
    earthRadius = float(6.738*pow(10,6))
    latA, lonA = coord1
    latB, lonB = coord2
    latA, lonA = radians(latA), radians(lonA)
    latB, lonB = radians(latB), radians(lonB)
    distance = earthRadius * acos((sin(latA)*sin(latB)) + cos(latA)*cos(latB)*cos(lonA-lonB))
    return distance