import pytest
from src.ui import *

def test_ui(qtbot):
    
    pros = Processor()
    dbFile = os.getcwd() + os.path.sep+ 'tests'+os.path.sep+'camp_test.db'
    db = DB(dbFile,'')
    pros.db = db
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,pros)
    qtbot.addWidget(MainWindow)  
    MainWindow.show()
    assert ui.label.text()=='Gila Breath Camp'

    ui.actionAdd_New.trigger()


    qtbot.wait(2000)

    # sys.exit(app.exec_())
    pros.kill()

    

    
