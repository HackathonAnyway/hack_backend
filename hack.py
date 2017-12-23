# filename: happy_birthday.py
"""A basic (single function) API written using hug"""
import hug
import connectDb
import uuid

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
        print (result)
        cnx.commit()
    cnx.close()

@hug.post('/event/delete', versions=VERSION)
def deleteEvent(userId, eventId):
    pass

@hug.get('/event/query', versions=VERSION)
def queryEvent(userId):
    cnx = connectDb.getConn()
    with cnx.cursor() as cursor:
        sql = 'select * from TB_EVENT'
        cursor.execute(sql)
        result = cursor.fetchall()
        print (result)
        cnx.commit()

    cnx.close()
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
    pass

@hug.post('/event/modify', versions=VERSION)
def modifyEvent():
    pass


