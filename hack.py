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
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            sql = 'INSERT INTO TB_EVENT VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\')'.format(str(uuid.uuid4()), eventName, starttime, location, period, flag)
            cursor.execute(sql)
            resResult = "success"
            cnx.commit()
    except Exception as err:
        resResult = "error occurred"
        print (err)
    finally:
        cnx.close()
        return resResult
    

@hug.post('/event/delete', versions=VERSION)
def deleteEvent(userId, eventId, response=None):
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            sqlSelect = 'SELECT * FROM TB_EVENT WHERE eventId=\'{0}\''.format(eventId)
            cursor.execute(sqlSelect)
            resResult = cursor.fetchall()
            if resResult:
                sqlDelete = 'DELETE FROM TB_EVENT WHERE eventId=\'{0}\''.format(eventId)
                cursor.execute(sqlDelete)
                result = "delete success"
                cnx.commit()
            else :
                response.status = HTTP_400
                result = "event not found"
    except Exception as err:
        result = "error occurred"
        print (err)
    finally:
        cnx.close()
        return result

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
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            if eventId == "DEFAULT":
                sql = 'SELECT * FROM TB_EVENT'
            else :
                sql = 'SELECT * FROM TB_EVENT WHERE eventId=\'{0}\''.format(eventId)
            cursor.execute(sql)
            resResult = cursor.fetchall()
            cnx.commit()
    except Exception as err:
        resResult = "error occurred"
        print (err)
    finally:
        cnx.close()
        return resResult

@hug.post('/event/modify', versions=VERSION)
def modifyEvent(eventId, eventName, eventStarttime, eventLocation, eventPeriod, eventFlag):
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            sql = 'UPDATE TB_EVENT SET eventName=\'{0}\', eventStarttime=\'{1}\', eventLocation=\'{2}\',\
                eventPeriod=\'{3}\', eventFlag=\'{4}\' WHERE eventId=\'{5}\'\
                '.format(eventName, eventStarttime, eventLocation, eventPeriod, eventFlag, eventId)
            cursor.execute(sql)
            resResult = cursor.fetchall()
            cnx.commit()           
    except Exception as err:
        resResult = "error occurred"
        print (err)
    finally:
        cnx.close()
        return resResult

@hug.post('/user/login', versions=VERSION)
def loginUser(userId, userPassword, response=None):
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            sql = 'SELECT userPassword FROM TB_USER WHERE userId ={0}'.format(userId)
            print (sql)
            cursor.execute(sql)
            resResult = cursor.fetchall()
            if (resResult[0]['userPassword'] == userPassword):
                result = 'success'
            else:
                response.status = HTTP_400
                result = 'auth error'
            cnx.commit()    
    except Exception as err:
        result = "auth error"
        response.status = HTTP_400
        print (err)
    finally:
        cnx.close()
        return result
        
@hug.post('/user/register', versions=VERSION)
def registerUser(userId, userPassword):
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            sql = 'INSERT INTO TB_USER VALUES({0}, {1})'.format(userId, userPassword)
            cursor.execute(sql)
            resResult = "success"
            cnx.commit()
    except Exception as err:
        resResult = "error occurred"
        print (err)
    finally:
        cnx.close()
        return resResult
