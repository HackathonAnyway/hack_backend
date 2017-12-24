import hack
import numpy as np
import map

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