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
    assert len(processor.registerCamps()) ==3

