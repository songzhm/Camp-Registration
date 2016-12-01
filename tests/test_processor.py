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


