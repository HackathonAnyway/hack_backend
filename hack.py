# filename: happy_birthday.py
"""A basic (single function) API written using hug"""
import hug
import connectDb

@hug.post('/happy_birthday')
def happy_birthday(name, age:hug.types.number=1):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())

VERSION = 1
@hug.post('/event/add', versions=VERSION)
def addEvent(eventName, location, starttime, period):
    pass

@hug.post('/event/delete', versions=VERSION)
def deleteEvent(userId, eventId):
    pass

@hug.get('/event/query', versions=VERSION)
def queryEvent(userId):
    cnx = connectDb.getConn()
    with cnx.cursor() as cursor:
        sql = 'show columns from TB_EVENT'
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


