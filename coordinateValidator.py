from haversine import *
def coordiateValidator(coords1, coords2):
    data = {}
    for dict1 in coords1:
        for dict2 in coords2:
            maximumDistance = 100
            distance = haversineFormula((dict1['latitude'],dict1['longitude']),((dict2['latitude'],dict2['longitude'])))
            if distance<=maximumDistance:
                data[dict1['id']] = dict2['id']
    return data