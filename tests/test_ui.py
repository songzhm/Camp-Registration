import pytest
from src.ui import *

def test_ui(qtbot):
    
    pros = Processor()
    dbFile = os.getcwd() + os.path.sep+ 'tests'+os.path.sep+'camp_test.db'
    db = DB(dbFile,'')
    pros.db = db
    
    
    MainWindow = QtGui.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow,pros)
    # qtbot.addWidget(MainWindow)  
    
    MainWindow.show()
    
    assert ui.label.text()=='Gila Breath Camp'

    qtbot.mouseClick(ui.pushButtonLogin,QtCore.Qt.LeftButton)
    assert ui.labelLogin.text()=='please select an user to login'
    ui.radioButtonDirector.setChecked(True)
    ui.lineEditAccessCode.setText('1')
    qtbot.mouseClick(ui.pushButtonLogin,QtCore.Qt.LeftButton)
    assert ui.labelLogin.text()=='wrong access code'
    ui.radioButtonRegClerk.setChecked(True)
    ui.lineEditAccessCode.setText('1')
    qtbot.mouseClick(ui.pushButtonLogin,QtCore.Qt.LeftButton)
    assert ui.labelLogin.text()=='wrong access code'
    ui.radioButtonDirector.setChecked(True)
    ui.lineEditAccessCode.setText('12345')
    qtbot.mouseClick(ui.pushButtonLogin,QtCore.Qt.LeftButton)
    assert ui.labelLogin.text()=='welcome'

    ui.actionAdd_New.trigger()

    assert ui.ui_addNew.label_18.text() == "Applicant Basic Information:"
    qtbot.keyClicks( ui.ui_addNew.lineFirstName, "saldkjf")
    qtbot.keyClicks( ui.ui_addNew.lineLastName,"jhksjdh")
    qtbot.keyClicks( ui.ui_addNew.lineGender,"M")
    # qtbot.keyClicks(ui_AddNew.dateEditDOB,"01/1/88")
    ui.ui_addNew.dateEditDOB.setDate(QtCore.QDate(1988,1,1))
    qtbot.keyClicks( ui.ui_addNew.lineEmail,"laksjdlf@kalsjdf.com")
    qtbot.keyClicks( ui.ui_addNew.lineHomePhone,"192873198723")
    qtbot.keyClicks( ui.ui_addNew.lineCellPhone,"87697676576")
    qtbot.keyClicks( ui.ui_addNew.lineLine1,"laskjd")
    qtbot.keyClicks( ui.ui_addNew.lineLine2,"jhkjhasdf")
    qtbot.keyClicks( ui.ui_addNew.lineCity,"upkajsf")
    qtbot.keyClicks( ui.ui_addNew.lineState,"cs")
    qtbot.keyClicks( ui.ui_addNew.lineEmergencyName,"aksdjfk")
    qtbot.keyClicks( ui.ui_addNew.lineEmergencyPhone,"0981749827")
    qtbot.mouseClick( ui.ui_addNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    ui.ui_addNew.comboBoxCamp.setCurrentIndex(1)
    assert ui.ui_addNew.labelWarningMsg.text() == "The fileds with * cannot be empty"
    qtbot.keyClicks(ui.ui_addNew.lineZipCode,"98731")
    qtbot.keyClicks(ui.ui_addNew.comboBoxAcceptanceDecision,"1")
    qtbot.mouseClick(ui.ui_addNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    ui.ui_addNew.comboBoxCamp.setCurrentIndex(2)
    # assert ui.ui_addNew.labelWarningMsg.text() == "This application cannot be accepted due to applicant need to be 9-18 years old"
    # ui_AddNew.dateEditDOB.setDate(QtCore.QDate(2006,1,1))
    # qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    # assert ui_AddNew.labelWarningMsg.text() == "This application cannot be accepted due to there is no space in camp c1"
    # ui_AddNew.comboBoxCamp.setCurrentIndex(2)
    # qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    # assert ui_AddNew.labelWarningMsg.text() == "This application cannot be accepted since the payment check has not been recieve"
    # qtbot.keyClicks(ui_AddNew.checkBoxPayment," ")
    # qtbot.mouseClick(ui_AddNew.pushButtonCheckList,QtCore.Qt.LeftButton)
    # qtbot.mouseClick(ui_AddNew.pushButtonGenerateLetter,QtCore.Qt.LeftButton)
    # qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    # assert ui_AddNew.labelWarningMsg.text()[0:7]=="Success"


    


    # DialogAddNewApplicant = QtGui.QDialog()
    # ui_AddNew = Ui_DialogAddNewApplicant()
    # ui_AddNew.setupUi(DialogAddNewApplicant,pros)
    # # DialogAddNewApplicant.show()
    # assert ui_AddNew.label_18.text() == "Applicant Basic Information:"
    # qtbot.keyClicks(ui_AddNew.lineFirstName, "saldkjf")
    # qtbot.keyClicks(ui_AddNew.lineLastName,"jhksjdh")
    # qtbot.keyClicks(ui_AddNew.lineGender,"M")
    # # qtbot.keyClicks(ui_AddNew.dateEditDOB,"01/1/88")
    # ui_AddNew.dateEditDOB.setDate(QtCore.QDate(1988,1,1))
    # qtbot.keyClicks(ui_AddNew.lineEmail,"laksjdlf@kalsjdf.com")
    # qtbot.keyClicks(ui_AddNew.lineHomePhone,"192873198723")
    # qtbot.keyClicks(ui_AddNew.lineCellPhone,"87697676576")
    # qtbot.keyClicks(ui_AddNew.comboBoxCamp,"2")
    # qtbot.keyClicks(ui_AddNew.lineLine1,"laskjd")
    # qtbot.keyClicks(ui_AddNew.lineLine2,"jhkjhasdf")
    # qtbot.keyClicks(ui_AddNew.lineCity,"upkajsf")
    # qtbot.keyClicks(ui_AddNew.lineState,"cs")
    # qtbot.keyClicks(ui_AddNew.lineEmergencyName,"aksdjfk")
    # qtbot.keyClicks(ui_AddNew.lineEmergencyPhone,"0981749827")
    # qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    # ui_AddNew.comboBoxCamp.setCurrentIndex(1)
    # assert ui_AddNew.labelWarningMsg.text() == "The fileds with * cannot be empty"
    # qtbot.keyClicks(ui_AddNew.lineZipCode,"98731")
    # qtbot.keyClicks(ui_AddNew.comboBoxAcceptanceDecision,"1")
    # qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    # assert ui_AddNew.labelWarningMsg.text() == "This application cannot be accepted due to applicant need to be 9-18 years old"
    # ui_AddNew.dateEditDOB.setDate(QtCore.QDate(2006,1,1))
    # qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    # assert ui_AddNew.labelWarningMsg.text() == "This application cannot be accepted due to there is no space in camp c1"
    # ui_AddNew.comboBoxCamp.setCurrentIndex(2)
    # qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    # assert ui_AddNew.labelWarningMsg.text() == "This application cannot be accepted since the payment check has not been recieve"
    # qtbot.keyClicks(ui_AddNew.checkBoxPayment," ")
    # qtbot.mouseClick(ui_AddNew.pushButtonCheckList,QtCore.Qt.LeftButton)
    # qtbot.mouseClick(ui_AddNew.pushButtonGenerateLetter,QtCore.Qt.LeftButton)
    # qtbot.mouseClick(ui_AddNew.pushButtonSubmit,QtCore.Qt.LeftButton)
    # assert ui_AddNew.labelWarningMsg.text()[0:7]=="Success"

    # DialogAddNewApplicant.accept()
    
    # DialogLookUpApplicant = QtGui.QDialog()
    # ui_LookUp = Ui_DialogLookUpApplicant()
    # ui_LookUp.setupUi(DialogLookUpApplicant,pros)
    
    # ui_LookUp.comboBoxCamp.setCurrentIndex(1)
    # qtbot.mouseClick(ui_LookUp.pushButtonLookUp,QtCore.Qt.LeftButton)

    # # DialogLookUpApplicant.show()

    # assert ui_LookUp.tableWidgetApplicantTable.item(0,0).text()=='1'
    
    # ui_LookUp.tableWidgetApplicantTable.selectRow(0)

    # qtbot.mouseClick(ui_LookUp.pushButtonUpdate,QtCore.Qt.LeftButton)

    # DialogUpdateApplicant = QtGui.QDialog()
    # ui_UpdateApplicant = Ui_DialogUpdateApplicant()
    # ui_UpdateApplicant.setupUi(DialogUpdateApplicant,pros)

    # qtbot.mouseClick(ui_UpdateApplicant.pushButtonCheckList,QtCore.Qt.LeftButton)

    qtbot.wait(5000)
    # sys.exit(app.exec_())


    


    
    pros.kill()

    

    
