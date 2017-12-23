# filename: happy_birthday.py
"""A basic (single function) API written using hug"""
import hug
import connectDb
import uuid
from falcon import HTTP_400

@hug.post('/happy_birthday')
def happy_birthday(name, age:hug.types.number=1):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())


VERSION = 1
@hug.post('/event/add', versions=VERSION)
def addEvent(eventName, location, starttime, period, flag:hug.types.number=0):
    cnx = connectDb.getConn()
    with cnx.cursor() as cursor:
        sql = 'INSERT INTO TB_EVENT VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\')'.format(str(uuid.uuid4()), eventName, starttime, location, period, flag)
        print (sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        cnx.commit()
    cnx.close()
    return

@hug.post('/event/delete', versions=VERSION)
def deleteEvent(userId, eventId, response=None):
    cnx = connectDb.getConn()
    with cnx.cursor() as cursor:
        sqlSelect = 'SELECT * FROM TB_EVENT WHERE eventId=\'{0}\''.format(eventId)
        cursor.execute(sqlSelect)
        result = cursor.fetchall()
        if result:
            sqlDelete = 'DELETE FROM TB_EVENT WHERE eventId=\'{0}\''.format(eventId)
            cursor.execute(sqlDelete)
            cnx.commit()
        else :
            response.status = HTTP_400
            return "event not found"
    cnx.close()

@hug.get('/event/query', versions=VERSION)
def queryEvent(userId, eventId="DEFAULT"):
    """
    return 
    {
        userId: '',
        eventList: [
            {
                eventId: '',
                eventName: '',
                location: '',
                startTime: '',
                period: '',
                flag: '0 1 2'
            },
            {

            },
        ]
    }
    """
    cnx = connectDb.getConn()
    with cnx.cursor() as cursor:
        if eventId == "DEFAULT":
            sql = 'SELECT * FROM TB_EVENT'
        else :
            sql = 'SELECT * FROM TB_EVENT WHERE eventId=\'{0}\''.format(eventId)
        cursor.execute(sql)
        result = cursor.fetchall()
        cnx.commit()
    cnx.close()
    print(result)
    return result

@hug.post('/event/modify', versions=VERSION)
def modifyEvent(eventId, eventName, eventStarttime, eventLocation, eventPeriod, eventFlag):
    cnx = connectDb.getConn()
    with cnx.cursor() as cursor:
        sql = 'UPDATE TB_EVENT SET eventName=\'{0}\', eventStarttime=\'{1}\', eventLocation=\'{2}\',\
             eventPeriod=\'{3}\', eventFlag=\'{4}\' WHERE eventId=\'{5}\'\
            '.format(eventName, eventStarttime, eventLocation, eventPeriod, eventFlag, eventId)
        cursor.execute(sql)
        cnx.commit()
    cnx.close
    print(reversed)
    return


