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



