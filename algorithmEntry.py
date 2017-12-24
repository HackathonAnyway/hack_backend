import hack
import numpy as np
import map
<<<<<<< HEAD
import requests
import json

def getUndone(userId):
    try:
        # 返回未完成的  events  
        url = 'http://172.20.10.3:8000/v1/event/query?userId={0}'.format(userId)
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
print(getMatrix("tric", "江苏省南京市新街口"))
=======

def getUndone(userId):
    # 返回未完成的  events  
    events = hack.queryEvent(userId)
    result = []
    for event in events:
        if event["eventFlag"] == 1:
            result.append(event)
    # print(result)
    # 返回 objects
    return result


def getMatrix(userId, currentLocation):
    events = getUndone(userId)
    locations = []
    for event in events:
        locations.append(event["eventLocation"])
    locations.insert(0, currentLocation)
    print(locations)
    length = len(locations)
    # print("length : " + str(length))
    # a = np.matrix('1 2; 3 4')
    matrix = np.zeros(shape = (length + 1, length + 1))
    for i in range(0, length):
        for j in range(0, length):
            print(i, " ", j)
            #matrix[i][j] = map.getCarTime(map.locatePoint(i)[0], map.locatePoint(i)[1], map.locatePoint(j)[0], map.locatePoint(j)[1])
    #         # print(str(i) + "," + str(j))
    # return matrix
    print(matrix)
getMatrix("tric", "南京市南京信息工程大学")
>>>>>>> bd0d90832dedbcdbfae053952b7ec74beb14166d
