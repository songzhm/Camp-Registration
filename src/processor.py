from camp import *
from person import *
from db import *
from arrivalInstraction import *
import time
import os



class Processor(object):
    def __init__(self):
        cwd = os.getcwd()
        print(os.getcwd()+'/db/camp.db')
        self.db = DB(os.getcwd()+'/db/camp.db',os.getcwd()+'/db/Camp_schema.sql')
        self.__numberOfCamps = 3
        self.__numberOfGirlBunkhouses = 3
        self.__numberOfBoyBunkhouses = 3
        self.__totalGrilNumber = self.__numberOfGirlBunkhouses*6
        self.__totalBoyNumber = self.__numberOfBoyBunkhouses*6
        self.camps = self.registerCamps()
        self.campers = self.registerCampers()
        

    def registerCamps(self):
        '''
        create Camp objects
        '''
        lookUpData= ''
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

    def registerCampers(camp):
        '''
        create Camp objects
        '''
        lookUpData= 'gender = \'M\' and campId = ' + str(camp.id)
        applicantData = self.interacteDB('select','applicant',lookUpData)
        campers = []
        if applicantData['ok']:
            applicantData = applicantData['result']
            for i in range(len(applicantData)):
                a = applicantData[i]
                campers.append(Applicant(a['firstName'], a['lastName'],\
                                            a['age'],a['gender'],a['dateOfBirth'],\
                                            a['email'], a['tshirtSize'], \
                                            a['homePhone'], a['cellPhone'],\
                                            a['emergencyPhone'], a['emergencyContact'], \
                                            a['line1'], a['line2'], a['city'], \
                                            a['state'], a['zipCode'], a['payment'],\
                                            a['applicationDate'], a['reviewDate'], \
                                            a['decisionId'], a['formsChecked'], \
                                            a['equipmentsChecked'], a['campId'], \
                                            a['bunkhouseId'], a['tribeId']))
        else:
            print('error in retriving applicant process')
        

        
        return applicants


    def interacteDB(self, operation, tableName, data):
        '''
        this function operate certain interactive database operations
        input:
            operation: select/insert/update/delete
            tableName: table name 
            data: depend on interaction type
        '''


        if operation == "select":
            res = self.db.select(tableName,data)
        elif operation == "insert":
            res = self.db.insert(tableName,data)
        elif operation == "update":
            res = self.db.update(tableName,data)
        elif operation == "delete":
            res = self.db.delete(tableName,data)
        return res

    def addNewApplicant(self, data):
        addressData = {}
        addressData['line1'] = data['line1']
        addressData['line2'] = data['line2']
        addressData['city'] = data['city']
        addressData['state'] = data['state']
        addressData['zipCode'] = data['zipCode']

        if not self.interacteDB('insert','applicant',addressData):
            print('insert new applicant failed')
        
        # lookUp Address id

        condition ='line1 = ' + '\'' + str(data['line1']) + '\'' + ' and line2 = ' + '\'' + str(data['line2'])+ '\'' +\
        ' and city = ' + '\'' + str(data['city']) +'\'' + ' and state = ' + '\'' +str(data['state']) +'\'' + \
        ' and zipCode = ' + '\'' + str(data['zipCode']) + '\''

        res = self.interacteDB('select','applicant',condition)

        if res['ok']:
            id = res['id']
        else:
            print('error in look up address id')


        applicantData = {}
        applicantData['firstName'] = data['firstName']
        applicantData['lastNmae'] = data['lastName']
        applicantData['gender'] = data['gender']
        applicantData['dateOfBirth'] = data['dateOfBirth']
        applicantData['addressId'] = str(id)
        applicantData['homePhone'] = data['homePhone']
        applicantData['cellPhone'] = data['cellPhone']
        applicantData['payment'] = data['payment']
        applicantData['applicationDate'] = data['applicationDate']
        applicantData['reviewDate'] = data['reviewDate']
        applicantData['decisionId'] = data['decisionId']
        applicantData['formsChecked'] = data['formsChecked']
        applicantData['equipmentsChecked'] = data['equipmentsChecked']
        applicantData['campId'] = data['campId']
        applicantData['emergencyContactId'] = data['emergencyContactId']
        applicantData['bunkhouseId'] = data['bunkhouseId']
        applicantData['tribeId'] = data['tribeId']

        res = self.interacteDB('insert','applicant',applicantData)

        return res

        

    def checkSpaceAvilibility(self, camp):
        '''
        this function check the space availability from a given camp id
        '''
        avilibility = 0

        return avilibility

    def generateLetterOfAcceptance(self, applicant, camp):
        letter = LetterOfAcceptance(applicant,camp)

        return letter.generateLetter()


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

p.registerCamps()
print(p.camps)
p.kill()

# print("processor is running, counting for 5")
# for i in range(5):
#     print(i+1)
#     time.sleep(1)

# p.kill()
# print('processor is killed')