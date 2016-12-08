from src.db import *

import pytest

@pytest.fixture(scope = "module")
def db(request):
    print('creating testing db connection')


    dbFile = os.getcwd() + os.path.sep+ 'tests'+os.path.sep+'camp_test.db'
    db = DB(dbFile,os.getcwd() + os.path.sep+ 'src' + os.path.sep + 'db' + os.path.sep + 'Camp_schema.sql')
    yield db
    print('disconnecting testing db connection')
    db.disconnect()
    


    

def test_db_insert(db):
    res = db.insert("camp",[{'id':'4','name':'c4','startDate':'2016-10-10','endDate':'2016-12-10','totalCapacity':'72'}])
    assert res['ok'] == True
    res = db.insert("camp",[{'id':'4','name':'c4','startDate':'2016-10-10','endDate':'2016-12-10','totalCapacity':'72'}])
    assert res['ok'] == True
    res = db.insert("camp",[{'campId':'4','name':'c4','startDate':'2016-10-10','endDate':'2016-12-10','totalCapacity':'72'}])
    assert res['result']['msg'] == 'error happend in db insert process.'

def test_db_select(db):
    res = db.select("camp",'')
    assert res['ok'] == True
    assert len(res['result']) == 4

def test_db_update(db):
    res = db.update("camp", {'newData':{'startDate':'2018-06-06'},'conditions':{'id':4}})
    assert res['ok'] == True
    assert db.select("camp","id = 4")['result'][0]['startDate'] == '2018-06-06'
    res = db.update("camp",{'newData':{'startDate':'2016-10-10'},'conditions':{'id':4}})
    assert res['ok'] == True
    assert db.select("camp","id = 4")['result'][0]['startDate'] == '2016-10-10'


def test_db_deleting(db):
    res = db.delete("camp",{'id':4})
    assert res['ok'] == True
    res = db.delete("camp",{'campId':4})
    assert res['ok'] == False
    res = db.select("camp",'')
    assert len(res['result']) == 3
    

