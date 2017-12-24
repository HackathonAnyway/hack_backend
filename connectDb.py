import pymysql.cursors

def getConn():
<<<<<<< HEAD
    cnx = pymysql.connect(   host='172.20.10.3',
=======
    cnx = pymysql.connect(   host='172.21.0.2',
>>>>>>> bd0d90832dedbcdbfae053952b7ec74beb14166d
                             user='root',
                             password='123456',
                             db='hackforchristmas',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    return cnx