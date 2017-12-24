import requests
import json
import re
def locatePoint(location):
    #input location  , return lng lat
    try:
        url = "http://api.map.baidu.com/geocoder/v2/?address={0}&ret_coordtype=gcj02ll&city=南京市&output=json&ak=WkaSDu7nrqKQBIeOFyKeUT6wQpLGQ5te".format(location)
        # print(url)
        r = requests.get(url)
        lng = json.loads(r.text)['result']['location']['lng']
        lat = json.loads(r.text)['result']['location']['lat']
        # print(location+"的经纬度")
        # print(lng)
        # print(lat)
    except Exception as err:
        print(err)
        lng = -1
        lat = -1
    return lng, lat

def getCarTime(origin_lng, origin_lat, destination_lng, destination_lat, tactics="13", vehicle="driving"):
    try:
        #http://api.map.baidu.com/routematrix/v2/driving?output=json&
        # origins=40.45,116.34|40.54,116.35&destinations=40.34,116.45|40.35,116.46&ak=您的ak
        url = "http://api.map.baidu.com/routematrix/v2/{0}?tactics={1}&coord_type=gcj02&output=json&origins={2},{3}&destinations={4},{5}&ak=WkaSDu7nrqKQBIeOFyKeUT6wQpLGQ5te".format(vehicle, tactics, origin_lat, origin_lng, destination_lat, destination_lng)
        # print(url)
        r = requests.get(url)
        # print(r.text)
        time = json.loads(r.text)['result'][0]['duration']['text']
        # print("获取到的time 的 str : "+time)
        # 单位 小时 or 分钟
        nuit = ''.join(re.findall('[\u4e00-\u9fa5]+', time))
        # float类型 数据
        timeNumber = float(time[0:(len(time)-2)])
        if nuit == '小时':
            minutes = timeNumber * 60
        else:
            minutes = timeNumber
        # print(int(minutes))
        # print(type(minutes))
    except Exception as err:
        minutes = -1
        print(err)
    return minutes

minutes1=getCarTime(locatePoint("江苏省南京市江宁区南京航空航天大学")[0], locatePoint("江苏省南京市江宁区南京航空航天大学")[1], locatePoint("东南大学")[0], locatePoint("东南大学")[1])
minutes2=getCarTime(locatePoint("江苏省南京市江宁区南京航空航天大学")[0], locatePoint("江苏省南京市江宁区南京航空航天大学")[1], locatePoint("江苏省南京市浦口区南京信息工程大学")[0], locatePoint("江苏省南京市浦口区南京信息工程大学")[1])
print(minutes1)
print(minutes2)
