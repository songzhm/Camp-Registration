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
    
    def generateCheckList(self,type):
        
        return self.cl.generageCheckList(type)


    def switch(self, final_list, clist, elist):
        switch_list = []
        e_temp_id = 0
        for x in clist:
            # read data
            temp_bunklist = []
            temp_id_1 = x[0]
            temp_id_2 = x[1]
            temp_b_1 = final_list[temp_id_1][2]
            temp_a_1 = final_list[temp_id_1][0]
            temp_b_2 = final_list[temp_id_2][2]
            temp_a_2 = final_list[temp_id_2][0]
            # if they are in the same bunkhouse, no swith
            if temp_b_1 == temp_b_2: break
            # if not, read all members in the bunkhouse number == id_2

            temp_fianl_list = final_list[1]
            for y in final_list:
                if y[2] == temp_b_2 and y[1] != temp_id_2: temp_bunklist.append(y)

            # if id_1 is on someone's elist in bunkhouse_2, can't switch id_1 to temp_b_2
            for x in elist:
                if temp_id_1 == x[0]:
                    # found the id that reject id_1
                    e_temp_id = x[1]
            # see if the id reject id_1 in the list of temp_bunklist, true => break
            if final_list[e_temp_id][2] == temp_b_2:
                break

            res = [abs(x[0] - temp_a_1) for x in temp_bunklist]
            id_final = temp_bunklist[res.index(min(res))][1]
            switch_list.append([temp_id_1, id_final])

        for x in elist:
            # read data
            temp_bunklist = []
            temp_id_1 = x[0]
            temp_id_2 = x[1]
            temp_b_1 = final_list[temp_id_1][2]
            temp_a_1 = final_list[temp_id_1][0]
            temp_g_1 = final_list[temp_id_1][3]
            temp_b_2 = final_list[temp_id_2][2]
            temp_a_2 = final_list[temp_id_2][0]
            # if they are not in the same bunkhouse, no swith
            if temp_b_1 == temp_b_2:
                # if yes, read all members in the bunkhouse number == id_2

                temp_fianl_list = final_list[1]
                for y in final_list:
                    if y[2] != temp_b_2 and y[1] != temp_id_2 and y[1] != temp_id_1 and temp_g_1 == y[
                        3]: temp_bunklist.append(y)

                res = [abs(x[0] - temp_a_1) for x in temp_bunklist]
                id_final = temp_bunklist[res.index(min(res))][1]
                switch_list.append([temp_id_1, id_final])

        return switch_list


    def assignBunkhouses(self,campId):
        camp = self.camps[campId - 1]
        bunkhousenumber = camp.numberOfBoyBunkhouses+camp.numberOfGirlBunkhouses
        male='M'
        female='F'
        res = self.interacteDB('select','applicant','campId={} and decisionId=1'.format(str(campId)))['result']
        alist = [datetime.datetime.strptime(x['applicationDate'],'%Y-%m-%d').year - datetime.datetime.strptime(x['dateOfBirth'],'%Y-%m-%d').year for x in res]
        
        ilist = [x['id'] for x in res]
        blist=[]
        glist = [x['gender'] for x in res]

        for x in range(0, len(ilist)):
            if glist[x] == male: blist.append(x % int(bunkhousenumber / 2) + 1)

        for x in range(0, len(ilist)):
            if glist[x] == female: blist.append(x % int(bunkhousenumber / 2) + int(bunkhousenumber / 2) + 1)

        age_sorted = sorted(zip(alist, ilist, blist, glist))
        age_sorted = sorted(age_sorted, key = lambda x:x[1])

        res = self.interacteDB('select','bkpreference','campId='+str(campId))['result']
        clist = []
        elist = []
        for x in res:
            if x['stay']=='':
                elist.append((x['applicantId'],x['reject']))
            elif x['reject']=='':
                clist.append((x['applicantId'],x['stay']))

        switch_list = self.switch(age_sorted,clist,elist)

        final_list = []
        for x in age_sorted:
            final_list.append(list(x))
        for x in switch_list:
            id_1 = x[0]
            id_2 = x[1]
            temp = final_list[id_1][2]
            final_list[id_1][2] = final_list[id_2][2]
            final_list[id_2][2] = temp
        
        for x in final_list:
            bkId = x[2]
            aId = x[1]
            self.interacteDB('update','applicant',{'newData':{'bunkhouseId':bkId},'conditions':{'id':aId}})
            
            

        




    def assignTribes(self,campId):
        camp = self.camps[campId - 1]
        tribenumber = camp.numberOfTribes
        male='M'
        female='F'
        res = self.interacteDB('select','applicant','campId={} and decisionId=1'.format(str(campId)))['result']
        alist = [datetime.datetime.strptime(x['applicationDate'],'%Y-%m-%d').year - datetime.datetime.strptime(x['dateOfBirth'],'%Y-%m-%d').year for x in res]
        ilist = [x['id'] for x in res]
        tlist=[]
        glist = [x['gender'] for x in res]

        for x in range(0, len(ilist)):
            if glist[x] == male: tlist.append(x % tribenumber + 1)

        for x in range(0, len(ilist)):
            if glist[x] == female: tlist.append(x % tribenumber  + 1)

        age_sorted = sorted(zip(alist, ilist, tlist, glist))
        age_sorted = sorted(age_sorted, key = lambda x:x[1])

        res = self.interacteDB('select','tribepreference','campId='+str(campId))['result']
        clist = []
        elist = []
        for x in res:
            if x['stay']=='':
                elist.append((x['applicantId'],x['reject']))
            elif x['reject']=='':
                clist.append((x['applicantId'],x['stay']))

        switch_list = self.switch(age_sorted,clist,elist)

        final_list = []
        for x in age_sorted:
            final_list.append(list(x))
        for x in switch_list:
            id_1 = x[0]
            id_2 = x[1]
            temp = final_list[id_1][2]
            final_list[id_1][2] = final_list[id_2][2]
            final_list[id_2][2] = temp
        
        for x in final_list:
            tId = x[2]
            aId = x[1]
            self.interacteDB('update','applicant',{'newData':{'tribeId':tId},'conditions':{'id':aId}})
            
            


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