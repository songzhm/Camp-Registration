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

     ## ui_lookup test_new
    ui.actionLook_Up.trigger()
    qtbot.keyClicks( ui.ui_lookUP.lineFirstName, 'Ori')
    qtbot.keyClicks( ui.ui_lookUP.lineLastName, 'Alfreda')
    ui.ui_lookUP.comboBoxCamp.setCurrentIndex(1)
    ui.ui_lookUP.dateEditDOB.setDate(QtCore.QDate(1988,1,1))
    qtbot.mouseClick( ui.ui_lookUP.pushButtonLookUp, QtCore.Qt.LeftButton)
    qtbot.mouseClick( ui.ui_lookUP.pushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick( ui.ui_lookUP.pushButton_2, QtCore.Qt.LeftButton)
    ui.ui_lookUP.tableWidgetApplicantTable.selectRow(0)
    qtbot.mouseClick( ui.ui_lookUP.pushButtonUpdate, QtCore.Qt.LeftButton)
    assert ui.ui_lookUP.ui_update.label_18.text() == "Applicant Basic Information:"

    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineFirstName, 'Ori')
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineLastName, 'Alfreda')
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineGender,"F")
    ui.ui_lookUP.ui_update.dateEditDOB.setDate(QtCore.QDate(1988,1,1))
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineEmail,"laksjdlf@kalsjdf.com")
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineHomePhone,"192873198723")
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineCellPhone,"87697676576")
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineLine1,"laskjd")
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineLine2,"jhkjhasdf")
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineCity,"upkajsf")
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineState,"cs")
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineEmergencyName,"aksdjfk")
    qtbot.keyClicks( ui.ui_lookUP.ui_update.lineEmergencyPhone,"0981749827")

    qtbot.mouseClick( ui.ui_lookUP.ui_update.pushButtonPreference, QtCore.Qt.LeftButton)
    ui.ui_lookUP.ui_update.ui_preference.textEdit.setText('2')
    ui.ui_lookUP.ui_update.ui_preference.textEdit_2.setText('2')
    qtbot.mouseClick( ui.ui_lookUP.ui_update.ui_preference.pushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick( ui.ui_lookUP.ui_update.pushButtonPreference_2, QtCore.Qt.LeftButton)
    qtbot.mouseClick( ui.ui_lookUP.ui_update.pushButtonCancellation, QtCore.Qt.LeftButton)
    qtbot.mouseClick( ui.ui_lookUP.ui_update.pushButtonCheckList, QtCore.Qt.LeftButton)
    qtbot.mouseClick( ui.ui_lookUP.ui_update.pushButtonSubmit, QtCore.Qt.LeftButton)
    ui.ui_lookUP.ui_update.comboBoxCamp.setCurrentIndex(1)
    assert ui.ui_lookUP.ui_update.labelWarningMsg.text()[:3] == "Suc"
    ui.ui_lookUP.ui_update.checkBoxFormsCheck.setChecked(True)
    ui.ui_lookUP.ui_update.checkBoxEquipmentsCheck.setChecked(True)
    ui.ui_lookUP.ui_update.comboBoxBunkhouse.setCurrentIndex(0)
    ui.ui_lookUP.ui_update.comboBoxTribe.setCurrentIndex(0)

    qtbot.mouseClick( ui.ui_lookUP.pushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick( ui.ui_lookUP.pushButton_2, QtCore.Qt.LeftButton)

    
    # qtbot.wait(5000)
    # sys.exit(app.exec_())


    


    
    pros.kill()

    

    
