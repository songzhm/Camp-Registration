from camp import *
from person import *
from db import *
import time
import os



class Processor(object):
    def __init__(self):
        cwd = os.getcwd()
        self.db = DB(os.getcwd()+'../db/camp.db',os.getcwd()+'../db/Camp_schema.sql')
        self.__numberOfCamps = 3
        self.__numberOfGirlBunkhouses = 3
        self.__numberOfBoyBunkhouses = 3
        self.__totalGrilNumber = self.__numberOfGirlBunkhouses*6
        self.__totalBoyNumber = self.__numberOfBoyBunkhouses*6
        self.camps = self.registerCamps()
        

    def registerCamps():
        '''
        create Camp objects
        '''
        lookUpData= {}
        campData = self.interacteDB('select','camp',lookUpData)
        camps = []
        if campData['ok']:
            campData = campData['result']
            for i in range(len(campData)):
                c = campData[i]
                camps.append(Camp(c['id'],c['name'],c['startDate'],\
                    c['endDate'],c['totalCapacity']))
        else:
            print('error in retriving camp process')
        

        
        return camps

    def registerCampers():
        '''
        create Camp objects
        '''
        lookUpData = {}
        
        return True


    def interacteDB(self, operation, tableName, data):
        '''
        this function operate certain interactive database operations
        input:
            operation: select/insert/update/delete
            tableName: table name 
            data: dict()
        '''


        if operation == "select":
            res = self.db.select(tableName,data)
        elif operation == "insert":
            res = self.db.insert(tableName,data)
        elif operation == "update":
            res = self.db.update(tableName,data)
        elif operation == "delete":
            res = self.db.delete(,tableName,data)
        return res

    def checkSpaceAvilibility(self, campId):
        '''
        this function check the space availability from a given camp id
        '''
        avilibility = 0

        return avilibility
    
    # def makeAcceptanceDecision(self,applicantId):
    #     '''
    #     this function check if there is any availability in the camp and return
    #     the corresponding message 
    #     '''
    #     result = {'decision':'', msg:''}
    #     pass
    #     return result


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