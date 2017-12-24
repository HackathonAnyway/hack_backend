# filename: happy_birthday.py
"""A basic (single function) API written using hug"""
import hug
import connectDb
import uuid
from falcon import HTTP_400
import time

@hug.post('/happy_birthday')
def happy_birthday(name, age:hug.types.number=1):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())


VERSION = 1
@hug.post('/event/add', versions=VERSION)
def addEvent(userId, eventName, location, period, flag:hug.types.number=0, startTime=int(time.time())):
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            sql = 'INSERT INTO TB_EVENT (eventId, eventName, eventStarttime, eventLocation, eventPeriod, eventFlag, userId ) VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\', \'{6}\')'.format(str(uuid.uuid4()), eventName, startTime, location, period, flag, userId)
            print (sql)
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
        eventList: [
            {
                eventId: '',
                eventName: '',
                eventStarttime: '',
                eventLocation: '',
                eventPeriod: '',
                eventFlag: '0 1 2'
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
                sql = 'SELECT * FROM TB_EVENT WHERE userId=\'{0}\''.format(userId)
            else :
                sql = 'SELECT * FROM TB_EVENT WHERE eventId=\'{0}\' AND userId=\'{1}\''.format(eventId, userId)
            cursor.execute(sql)
            resResult = cursor.fetchall()
            # print (resResult)
            cnx.commit()
    except Exception as err:
        resResult = "error occurred"
        print (err)
    finally:
        print (cnx)
        cnx.close()
        # print ('returning ..... >>>', resResult)
        return resResult

@hug.post('/event/modify', versions=VERSION)
def modifyEvent(userId, eventId, eventFlag):
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            sql = 'UPDATE TB_EVENT SET eventFlag=\'{0}\' WHERE eventId=\'{1}\' AND userId=\'{2}\'\
                '.format(eventFlag, eventId, userId)
            cursor.execute(sql)
            resResult = cursor.fetchall()
            if eventFlag == 1:
                sqlend = 'UPDATE TB_EVENT SET eventEndTime=\'{0}\' WHERE eventId=\'{1}\' AND userId=\'{2}\''.format(int(time.time()), eventId, userId)
                print (sqlend)
                cursor.execute(sqlend)
            print ('result............' ,resResult)
            cnx.commit()           
    except Exception as err:
        resResult = "error occurred"
        print (err)
    finally:
        cnx.close()
        return resResult

@hug.post('/user/login', versions=VERSION)
def loginUser(userId, userPassword, response=None):
    print (userId)
    print (userPassword)
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            sql = 'SELECT userPassword FROM TB_USER WHERE userId =\'{0}\''.format(userId)
            print (sql)
            cursor.execute(sql)
            resResult = cursor.fetchall()
            print (resResult)
            if (resResult[0]['userPassword'] == userPassword):
                print (111111111)
                result = 'success'
            else:
                response.status = HTTP_400
                print (2222222222)
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
    print (userId)
    print (type (userId))
    print (userPassword)
    print (type (userPassword))
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            sql = 'INSERT INTO TB_USER VALUES(\'{0}\', \'{1}\')'.format(userId, userPassword)
            print (sql)
            cursor.execute(sql)
            resResult = "success"
            cnx.commit()
    except Exception as err:
        resResult = "error occurred"
        print (err)
    finally:
        cnx.close()
        return resResult

@hug.post('/location/post', versions=VERSION)
def postLocation(location):
    print (location)
    # try:
    cnx = connectDb.getConn()
    with cnx.cursor() as cursor:
        sql = 'INSERT INTO TB_LOCATION VALUES(\'{0}\')'.format(location)
        print (sql)
        cursor.execute(sql)
        resResult = "success"
        cnx.commit()
        cnx.close()
    # except Exception as err:
        # resResult = "error occurred"
        # response.status = HTTP_400
        # print (err)
    # finally:
    #     cnx.close()
    #     return resResult

@hug.get('/location/get', versions=VERSION)
def postLocation():
    try:
        cnx = connectDb.getConn()
        with cnx.cursor() as cursor:
            sql = 'SELECT * FROM TB_LOCATION'.format(location)
            print (sql)
            cursor.execute(sql)
            resResult = cursor.fetchall()
            cnx.commit()
    except Exception as err:
        resResult = "error occurred"
        response.status = HTTP_400
        print (err)
    finally:
        cnx.close()
        return resResult