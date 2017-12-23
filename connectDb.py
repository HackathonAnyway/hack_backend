import pymysql.cursors

def getConn():
    cnx = pymysql.connect(   host='172.21.0.2',
                             user='root',
                             password='123456',
                             db='hackforchristmas',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return cnx