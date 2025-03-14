from fileManager import *
from coordinateValidator import *

def main():
    uav1 = csvToDict('SensorData1.csv')
    for dict in uav1:
        dict['latitude'] = float(dict['latitude'])
        dict['longitude'] = float(dict['longitude'])
    uav2 = jsonToDict('SensorData2.json')
    data = coordiateValidator(uav1,uav2)
    storeAsJSON(data)

if __name__ == "__main__":
    main()