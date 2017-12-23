import pymysql.cursors

def getConn():
    cnx = pymysql.connect(   host='mysql',
                             user='root',
                             password='123456',
                             db='hackforchristmas',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return cnx