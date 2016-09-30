from camp import *
from person import *
from db import *
import time

class Processor(object):
    def __init__(self):
        self.db = DB('../db/camp.db','../db/Camp_schema.sql')

    def interacteDB(self, operation, tableName, data):
        '''
        this function operate certain interactive database operations
        input:
            operation: select/insert/update/delete
            tableName: table name 
            data: dict()
        '''
        ok = False
        result = {}

        if operation == "select":
            pass
        elif operation == "insert":
            pass
        elif operation == "update":
            pass
        elif operation == "delete":
            pass
        
        return {'ok': ok, 'result': result}

    def checkSpaceAvilibility(self, campId):
        '''
        this function check the space availability from a given camp id
        '''
        available = False
        pass
        return available
    
    def makeAcceptanceDecision(self,applicants):
        '''
        this function check if there is any availability in the camp and return
        the corresponding message 
        '''
        result = {'decision':'', msg:''}
        pass
        return result

    def assignBunkhouses(self, campers, requirements):
        result = {}
        pass
        return result

    def assignTribes(self, campers, requirements):
        result = {}
        pass
        return result

    def kill(self):
        self.db.disconnect()
        return 0

p = Processor()


# print("processor is running, counting for 5")
# for i in range(5):
#     print(i+1)
#     time.sleep(1)

# p.kill()
# print('processor is killed')