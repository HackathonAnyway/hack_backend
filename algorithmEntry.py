import hack
import numpy as np
import map
import requests
import json

def getUndone(userId):
    try:
        # 返回未完成的  events  
        url = 'http://localhost:8000/v1/event/query?userId={0}'.format(userId)
        r = requests.get(url)
        events = []
        # print(r.text)
        for i in range(0, len(json.loads(r.text))):
            if json.loads(r.text)[i]["eventFlag"] == 0:
                events.append(json.loads(r.text)[i])
        print(events)
    except Exception as err:
        print(err)
    return events

def getDone(userId):
    try:
        # 返回未完成的  events  
        url = 'http://localhost:8000/v1/event/query?userId={0}'.format(userId)
        r = requests.get(url)
        events = []
        # print(r.text)
        for i in range(0, len(json.loads(r.text))):
            if json.loads(r.text)[i]["eventFlag"] == 1:
                events.append(json.loads(r.text)[i])
        print(events)
    except Exception as err:
        print(err)
    return events

def getMatrix(userId, currentLocation):
    try:
        events = getUndone(userId)
        locations = []
        for event in events:
            locations.append(event["eventLocation"])
        locations.insert(0, currentLocation)
        print(locations)
        length = len(locations)
        # print("length : " + str(length))
        # a = np.matrix('1 2; 3 4')
        matrix = np.zeros(shape = (length, length))
        for i in range(0, length):
            for j in range(0, length):
                print(i, " ", j)
                matrix[i][j] = map.getCarTime(map.locatePoint(locations[i])[0], map.locatePoint(locations[i])[1], map.locatePoint(locations[j])[0], map.locatePoint(locations[j])[1])
        #         # print(str(i) + "," + str(j))
        # return matrix
    except Exception as err:
        print(err)
    return matrix
# getUndone("tric")

# r = requests.get('http://localhost:8000/v1/location/get')
# if len(json.loads(r.text)) > 0:
#     currentLocation = json.loads(r.text)[0]['curLocation']
#     print ('currentLocation', currentLocation)
#     print(getMatrix("tric", currentLocation))
print (getDone("tric"))
