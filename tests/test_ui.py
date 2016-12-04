import pytest
from src.ui import *

def test_ui(qtbot):
    
    pros = Processor()
    dbFile = os.getcwd() + os.path.sep+ 'tests'+os.path.sep+'camp_test.db'
    db = DB(dbFile,'')
    pros.db = db
    
    
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,pros)
    # qtbot.addWidget(MainWindow)  
    ui.actionAdd_New.trigger()
    
    assert ui.label.text()=='Gila Breath Camp'

    DialogAddNewApplicant = QtGui.QDialog()
    ui_AddNew = Ui_DialogAddNewApplicant()
    ui_AddNew.setupUi(DialogAddNewApplicant,pros)
    # DialogAddNewApplicant.show()
    assert ui_AddNew.label_18.text() == "Applicant Basic Information:"
    qtbot.keyClicks(ui_AddNew.lineFirstName, "saldkjf")
    qtbot.keyClicks(ui_AddNew.lineLastName,"jhksjdh")
    qtbot.keyClicks(ui_AddNew.lineGender,"M")
    # qtbot.keyClicks(ui_AddNew.dateEditDOB,"01/1/88")
    ui_AddNew.dateEditDOB.setDate(QtCore.QDate(1988,1,1))
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
    ui_AddNew.comboBoxCamp.setCurrentIndex(1)
    assert ui_AddNew.labelWarningMsg.text() == "The fileds with * cannot be empty"
    qtbot.keyClicks(ui_AddNew.lineZipCode,"98731")
    qtbot.keyClicks(ui_AddNew.comboBoxAcceptanceDecision,"1")
    qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    assert ui_AddNew.labelWarningMsg.text() == "This application cannot be accepted due to applicant need to be 9-18 years old"
    ui_AddNew.dateEditDOB.setDate(QtCore.QDate(2006,1,1))
    qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    assert ui_AddNew.labelWarningMsg.text() == "This application cannot be accepted due to there is no space in camp c1"
    ui_AddNew.comboBoxCamp.setCurrentIndex(2)
    qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    assert ui_AddNew.labelWarningMsg.text() == "This application cannot be accepted since the payment check has not been recieve"
    qtbot.keyClicks(ui_AddNew.checkBoxPayment," ")
    qtbot.mouseClick(ui_AddNew.pushButtonCheckList,QtCore.Qt.LeftButton)
    qtbot.mouseClick(ui_AddNew.pushButtonGenerateLetter,QtCore.Qt.LeftButton)
    qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    assert ui_AddNew.labelWarningMsg.text()[0:7]=="Success"

    DialogAddNewApplicant.accept()
    
    DialogLookUpApplicant = QtGui.QDialog()
    ui_LookUp = Ui_DialogLookUpApplicant()
    ui_LookUp.setupUi(DialogLookUpApplicant,pros)
    
    ui_LookUp.comboBoxCamp.setCurrentIndex(1)
    qtbot.mouseClick(ui_LookUp.pushButtonLookUp,QtCore.Qt.LeftButton)

    DialogLookUpApplicant.show()

    assert ui_LookUp.tableWidgetApplicantTable.item(0,0).text()=='1'
    
    ui_LookUp.tableWidgetApplicantTable.selectRow(0)

    qtbot.mouseClick(ui_LookUp.pushButtonUpdate,QtCore.Qt.LeftButton)

    DialogUpdateApplicant = QtGui.QDialog()
    ui_UpdateApplicant = Ui_DialogUpdateApplicant()
    ui_UpdateApplicant.setupUi(DialogUpdateApplicant,pros)

    DialogUpdateApplicant.show()

    # qtbot.wait(10000)
    # sys.exit(app.exec_())
    
    pros.kill()

    

    
