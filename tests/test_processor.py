from src.processor import *

import pytest

@pytest.fixture(scope = "module")
def processor(request):
    
    pros = Processor()
    dbFile = os.getcwd() + os.path.sep+ 'tests'+os.path.sep+'camp_test.db'
    db = DB(dbFile,'')
    pros.db = db

    yield pros

    pros.kill()


def test_processor_registerCamps(processor):
    assert len(processor.registerCamps()) == 3

def test_processor_registerBunkhouses(processor):
    assert len(processor.registerBunkhouses()) == 6

def test_processor_registerTribes(processor):
    assert len(processor.registerTribes()) == 6

# def test_processor_registerCampers(processor):
#     assert len(processor.registerCampers(processor.camps[0]))>0

def test_processor_interacteDB(processor):
    res = processor.interacteDB('insert','camp',[{'id':'4','name':'c4','startDate':'2016-10-10','endDate':'2016-12-10','totalCapacity':'72'}])
    assert res['ok'] == True
    res = processor.interacteDB('insert','camp',[{'id':'4','name':'c4','startDate':'2016-10-10','endDate':'2016-12-10','totalCapacity':'72'}])
    assert res['ok'] == True
    res = processor.interacteDB('insert','camp',[{'campId':'4','name':'c4','startDate':'2016-10-10','endDate':'2016-12-10','totalCapacity':'72'}])
    assert res['result']['msg'] == 'error happend in db insert process'


    res = processor.interacteDB('select','camp','')
    assert res['ok'] == True
    assert len(res['result'])==4

    res = processor.interacteDB('update',"camp", {'newData':{'startDate':'2018-06-06'},'conditions':{'id':4}})
    assert res['ok'] == True
    assert processor.interacteDB('select',"camp","id = 4")['result'][0]['startDate'] == '2018-06-06'
    res = processor.interacteDB('update',"camp",{'newData':{'startDate':'2016-10-10'},'conditions':{'id':4}})
    assert res['ok'] == True
    assert processor.interacteDB('select',"camp","id = 4")['result'][0]['startDate'] == '2016-10-10'

    res = processor.interacteDB('delete',"camp",{'id':4})
    assert res['ok'] == True
    res = processor.interacteDB('delete',"camp",{'campId':4})
    assert res['ok'] == False
    res = processor.interacteDB('select',"camp",'')
    assert len(res['result']) == 3

def test_processor_addNewApplicant(processor):
    applicant = Applicant('Ming','asfdaf','16','M','12-01-2000','klasjdflk@lsakdf',\
    '198329','989287','918349','kjadsf','askjfdh','1232','akjdflsj','asfd','12312',True,'12-01-2016','12-01-2016',1,False,False,1,0,0)
    res = processor.addNewApplicant(applicant)
    assert res['ok'] == True

def test_processor_updateApplicant(processor):
    applicant = Applicant('MingSjks','asfdaf','16','M','12-01-2000','klasjdflk@lsakdf',\
    '198329','989287','918349','kjadsf','askjfdh','1232','akjdflsj','asfd','12312',True,'12-01-2016','12-01-2016',1,False,False,1,0,0)
    id = 47
    res = processor.updateApplicant(applicant,id)
    assert res['ok'] == True

def test_processor_checkSpaceAvilibility(processor):
    assert processor.checkSpaceAvilibility(1,"M")['availableSpace'] == 0
    assert processor.checkSpaceAvilibility(1,"F")['availableSpace'] == 1
    assert processor.checkSpaceAvilibility(2,"M")['availableSpace'] == 36
    assert processor.checkSpaceAvilibility(2,"F")['availableSpace'] == 36
    assert processor.checkSpaceAvilibility(3,"M")['availableSpace'] == 36
    assert processor.checkSpaceAvilibility(3,"F")['availableSpace'] == 36

def test_processor_validateApplicant(processor):
   assert processor.validateApplicant(1,'M',2)['msg'] == 'applicant need to be 9-18 years old'
   assert processor.validateApplicant(1,'M',12)['msg'] == 'there is no space in camp c1'
   assert processor.validateApplicant(1,'F',12)['msg'] == ''

def test_processor_generateLetterOfAcceptance(processor):
    
    assert processor.generateLetterOfAcceptance(1,processor.camps[0])[0:7] == 'Welcome'
    assert processor.generateLetterOfAcceptance(2,processor.camps[0])[0:7] == 'Welcome'
    assert processor.generateLetterOfAcceptance(3,processor.camps[0])[0:5] == 'Thank'
    assert processor.generateLetterOfAcceptance(4,processor.camps[0]) == 'Decision has not been made.'

def test_processor_generateCheckList(processor):
    assert processor.generateCheckList('form')[0:9] == '* medical'
    assert processor.generateCheckList('equipment')[0:8] == '* riding'

  