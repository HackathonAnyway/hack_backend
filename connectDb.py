import pymysql.cursors

def getConn():
    cnx = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='TB_EVENT',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return cnx