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
    
    assert ui.label.text()=='Gila Breath Camp'

    DialogAddNewApplicant = QtGui.QDialog()
    ui_AddNew = Ui_DialogAddNewApplicant()
    ui_AddNew.setupUi(DialogAddNewApplicant,pros)
    assert ui_AddNew.label_18.text() == "Applicant Basic Information:"
    qtbot.keyClicks(ui_AddNew.lineFirstName, "saldkjf")
    qtbot.keyClicks(ui_AddNew.lineLastName,"jhksjdh")
    qtbot.keyClicks(ui_AddNew.lineGender,"M")
    qtbot.keyClicks(ui_AddNew.dateEditDOB,"01/01/1988")
    qtbot.keyClicks(ui_AddNew.lineEmail,"laksjdlf@kalsjdf.com")
    qtbot.keyClicks(ui_AddNew.lineHomePhone,"192873198723")
    qtbot.keyClicks(ui_AddNew.lineCellPhone,"87697676576")
    qtbot.keyClicks(ui_AddNew.comboBoxCamp,"2")
    qtbot.keyClicks(ui_AddNew.lineLine1,"laskjd")
    qtbot.keyClicks(ui_AddNew.lineLine2,"jhkjhasdf")
    qtbot.keyClicks(ui_AddNew.lineCity,"upkajsf")
    qtbot.keyClicks(ui_AddNew.lineState,"cs")
    qtbot.keyClicks(ui_AddNew.lineEmergencyName,"aksdjfk")
    qtbot.keyClicks(ui_AddNew.lineEmergencyPhone,"0981749827")
    qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    assert ui_AddNew.labelWarningMsg.text() == "The fileds with * cannot be empty."
    qtbot.keyClicks(ui_AddNew.lineZipCode,"98731")
    qtbot.keyClicks(ui_AddNew.comboBoxAcceptanceDecision,"1")
    qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    assert ui_AddNew.labelWarningMsg.text() == "This application cannot be accepted due to applicant need to be 9-18 years old"
    qtbot.keyClicks(ui_AddNew.comboBoxCamp,"1")
    qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)





    




    qtbot.wait(10000)

    # sys.exit(app.exec_())
    pros.kill()

    

    
