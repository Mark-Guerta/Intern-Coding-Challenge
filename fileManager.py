from csv import DictReader
from json import load, dump
def csvToDict(path):
    with open(path, mode='r') as file:
        csv_reader = DictReader(file)
        data = [row for row in csv_reader]
    return data

def jsonToDict(path):
    with open(path, mode='r') as file:
        data = load(file)
    return data

def storeAsJSON(data):
    fileName = 'output.json'
    with open(fileName, mode='w', newline='') as file:
        dump(data, file,indent=2)