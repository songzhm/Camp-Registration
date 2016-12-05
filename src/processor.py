from src.camp import *
from src.person import *
from src.db import *
from src.arrivalInstraction import *
import time
import os



class Processor(object):
    def __init__(self):
        cwd = os.getcwd()
        print(cwd + os.path.sep + 'src' + os.path.sep + 'db' + os.path.sep + 'camp.db')
        self.db = DB(cwd + os.path.sep + 'src' + os.path.sep + 'db' + os.path.sep + 'camp.db',cwd + os.path.sep + 'src' + os.path.sep + 'db' + os.path.sep + 'Camp_schema.sql')
        self.__numberOfCamps = 3
        self.camps = self.registerCamps()
        self.bunkhouses = self.registerBunkhouses()
        self.tribes = self.registerTribes()
        self.cl = CheckList()
        # self.campers = self.registerCampers()
        

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

    def registerBunkhouses(self):
        '''
        create Bunkhouses objects
        '''
        lookUpData= ''
        bunkhouseData = self.interacteDB('select','bunkhouse',lookUpData)
        bunkhouses = []
        if bunkhouseData['ok']:
            bunkhouseData = bunkhouseData['result']
            for i in range(len(bunkhouseData)):
                b = bunkhouseData[i]
                bunkhouses.append(Bunkhouse(b['id'],b['name'],b['gender']))
        else:
            print('error in retriving bunkhouse` process')
        

        
        return bunkhouses

    def registerTribes(self):
        '''
        create Tribes objects
        '''
        lookUpData= ''
        tribeData = self.interacteDB('select','tribe',lookUpData)
        tribes = []
        if tribeData['ok']:
            tribeData = tribeData['result']
            for i in range(len(tribeData)):
                t = tribeData[i]
                tribes.append(Tribe(t['id'],t['name']))
        else:
            print('error in retriving tribe` process')
        

        
        return tribes

    # def registerCampers(camp):
    #     '''
    #     create Camp objects
    #     '''
    #     lookUpData= 'gender = \'M\' and campId = ' + str(camp.id)
    #     applicantData = self.interacteDB('select','applicant',lookUpData)
    #     campers = []
    #     if applicantData['ok']:
    #         applicantData = applicantData['result']
    #         for i in range(len(applicantData)):
    #             a = applicantData[i]
    #             campers.append(Applicant(a['firstName'], a['lastName'],\
    #                                         a['age'],a['gender'],a['dateOfBirth'],\
    #                                         a['email'], a['tshirtSize'], \
    #                                         a['homePhone'], a['cellPhone'],\
    #                                         a['emergencyPhone'], a['emergencyContact'], \
    #                                         a['line1'], a['line2'], a['city'], \
    #                                         a['state'], a['zipCode'], a['payment'],\
    #                                         a['applicationDate'], a['reviewDate'], \
    #                                         a['decisionId'], a['formsChecked'], \
    #                                         a['equipmentsChecked'], a['campId'], \
    #                                         a['bunkhouseId'], a['tribeId']))
    #     else:
    #         print('error in retriving applicant process')
        

        
    #     return campers


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

    def addNewApplicant(self, applicant):
        addressData = {}
        addressData['line1'] = applicant.address.line1
        addressData['line2'] = applicant.address.line2
        addressData['city'] = applicant.address.city
        addressData['state'] = applicant.address.state
        addressData['zipCode'] = applicant.address.zipCode

        self.interacteDB('insert','address',[addressData])

        
        # lookUp Address id

        condition ='line1 = ' + '\'' + str(applicant.address.line1) + '\'' + ' and line2 = ' + '\'' + str(applicant.address.line2)+ '\'' +\
        ' and city = ' + '\'' + str(applicant.address.city) +'\'' + ' and state = ' + '\'' +str(applicant.address.state) +'\'' + \
        ' and zipCode = ' + '\'' + str(applicant.address.zipCode) + '\''

        res = self.interacteDB('select','address',condition)

        if res['ok']:
            address_id = res['result'][0]['id']
        else:
            print('error in look up address id')


        emergencyContactData = {}
        emergencyContactData['name'] = applicant.emergencyContactName
        emergencyContactData['phone'] = applicant.emergencyContactPhone


        if emergencyContactData['name']=='':
            
            self.interacteDB('insert','emergencyContact',[emergencyContactData])
            
            # lookUp emergencyContact id

            condition ='name = \'' + str(applicant.emergencyContactName) + '\'' +\
            'and phone = \'' + str(applicant.emergencyContactPhone) + '\'' 

            res = self.interacteDB('select','emergencyContact',condition)
            if res['ok']:
                emergencyContact_id = res['result'][0]['id']
            else:
                print('error in look up emergency id')
        else:
            emergencyContact_id = ''





        applicantData = {}
        applicantData['firstName'] = applicant.firstName
        applicantData['lastName'] = applicant.lastName
        applicantData['gender'] = applicant.gender
        applicantData['dateOfBirth'] = applicant.dateOfBirth
        applicantData['addressId'] = str(address_id)
        applicantData['email'] = applicant.email
        applicantData['homePhone'] = applicant.homePhone
        applicantData['cellPhone'] = applicant.cellPhone
        applicantData['payment'] = applicant.payment
        applicantData['applicationDate'] = applicant.applicationDate
        applicantData['reviewDate'] = applicant.reviewDate
        applicantData['decisionId'] = applicant.decisionId
        applicantData['formsChecked'] = applicant.formsChecked
        applicantData['equipmentsChecked'] = applicant.equipmentsChecked
        applicantData['campId'] = applicant.campId
        applicantData['emergencyContactId'] = str(emergencyContact_id)
        applicantData['bunkhouseId'] = applicant.bunkhouseId
        applicantData['tribeId'] = applicant.tribeId

        res = self.interacteDB('insert','applicant',[applicantData])

        return res


    def updateApplicant(self, applicant,id):
        addressData = {}
        addressData['line1'] = applicant.address.line1
        addressData['line2'] = applicant.address.line2
        addressData['city'] = applicant.address.city
        addressData['state'] = applicant.address.state
        addressData['zipCode'] = applicant.address.zipCode

        lookUpRes = self.interacteDB('select','applicant','id = \''+str(id)+'\'')

        addressId = lookUpRes['result'][0]['addressId']

        if addressId == "":
            self.interacteDB('insert','address',[addressData])
        else:
            self.interacteDB('update','address',{'newData':addressData,'conditions':{'id':str(addressId)}})

        emergencyContactData = {}
        emergencyContactData['name'] = applicant.emergencyContactName
        emergencyContactData['phone'] = applicant.emergencyContactPhone
        
        emergencyContactId = lookUpRes['result'][0]['emergencyContactId']
        print(emergencyContactId)
        if emergencyContactId=="":
            self.interacteDB('insert','emergencyContact',[emergencyContactData])
        else:
            self.interacteDB('update','emergencyContact',{'newData':emergencyContactData,'conditions':{'id':str(emergencyContactId)}})

        applicantData = {}
        applicantData['firstName'] = applicant.firstName
        applicantData['lastName'] = applicant.lastName
        applicantData['gender'] = applicant.gender
        applicantData['dateOfBirth'] = applicant.dateOfBirth
        applicantData['addressId'] = str(addressId)
        applicantData['email'] = applicant.email
        applicantData['homePhone'] = applicant.homePhone
        applicantData['cellPhone'] = applicant.cellPhone
        applicantData['payment'] = applicant.payment
        applicantData['applicationDate'] = applicant.applicationDate
        applicantData['reviewDate'] = applicant.reviewDate
        applicantData['decisionId'] = applicant.decisionId
        applicantData['formsChecked'] = applicant.formsChecked
        applicantData['equipmentsChecked'] = applicant.equipmentsChecked
        applicantData['campId'] = applicant.campId
        applicantData['emergencyContactId'] = str(emergencyContactId)
        applicantData['bunkhouseId'] = applicant.bunkhouseId
        applicantData['tribeId'] = applicant.tribeId

        res = self.interacteDB('update','applicant',{'newData':applicantData,'conditions':{'id':id}})


        

        return res

        


        

    def checkSpaceAvilibility(self, campId,gender):
        '''
        this function check the space availability from a given camp id and gender
        '''

        occupiedSpace = self.interacteDB('select','applicant','campId = \''+str(campId)+\
        '\' and gender = \''+gender+ '\' and decisionId != \'3\' ')
        
        if occupiedSpace['ok']:
            occupiedSpace=len(occupiedSpace['result'])

            if gender == 'M':
                if self.camps[campId-1].totalBoyNumber > occupiedSpace:
                    return {'ok':True,'availableSpace':self.camps[campId-1].totalBoyNumber - occupiedSpace}
                else:
                    return {'ok':False,'availableSpace':0}
            elif gender == 'F':
                if self.camps[campId-1].totalGrilNumber > occupiedSpace:
                    return {'ok':True,'availableSpace':self.camps[campId-1].totalGrilNumber - occupiedSpace}
                else:
                    return {'ok':False,'availableSpace':0}
                
            
        else:
            print('error happend at checkSpaceAvilibility')

    def validateApplicant(self, campId, gender, age):
        '''
        this function check the space and the age constraints 
        '''
        if 9<=age<=18:
            res = self.checkSpaceAvilibility(campId,gender)
            if res['ok']:
                return {'ok':True,'msg':'','availableSpace':res['availableSpace']}
            else:
                return {'ok':False,'msg':'there is no space in camp '+self.camps[campId-1].name,'availableSpace':res['availableSpace']}
            
        else:
            return {'ok':False,'msg':'applicant need to be 9-18 years old'  }

    def generateLetterOfAcceptance(self, decisionId, camp):
        letter = LetterOfAcceptance(decisionId,camp)

        return letter.generateLetter()
    
    def generateCheckList(self):
        
        return self.cl.generageCheckList()



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






# p = Processor()

# p.registerCamps()
# print(p.camps)
# p.kill()

# print("processor is running, counting for 5")
# for i in range(5):
#     print(i+1)
#     time.sleep(1)

# p.kill()
# print('processor is killed')