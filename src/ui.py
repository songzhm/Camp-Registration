# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'campReg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import datetime
from src.processor import *



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)





class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow,p):
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.resize(993, 651)
        self.centralwidget = QtGui.QWidget(LoginWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 90, 471, 151))
        self.label.setStyleSheet(_fromUtf8("font: 75 20pt \"Kristen ITC\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBoxList = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxList.setGeometry(QtCore.QRect(220, 270, 501, 301))
        self.groupBoxList.setTitle(_fromUtf8(""))
        self.groupBoxList.setObjectName(_fromUtf8("groupBoxList"))
        self.radioButtonDirector = QtGui.QRadioButton(self.groupBoxList)
        self.radioButtonDirector.setGeometry(QtCore.QRect(140, 50, 211, 41))
        self.radioButtonDirector.setObjectName(_fromUtf8("radioButtonDirector"))
        self.radioButtonRegClerk = QtGui.QRadioButton(self.groupBoxList)
        self.radioButtonRegClerk.setGeometry(QtCore.QRect(140, 90, 211, 41))
        self.radioButtonRegClerk.setObjectName(_fromUtf8("radioButtonRegClerk"))
        self.lineEditAccessCode = QtGui.QLineEdit(self.groupBoxList)
        self.lineEditAccessCode.setGeometry(QtCore.QRect(140, 180, 221, 21))
        self.lineEditAccessCode.setObjectName(_fromUtf8("lineEditAccessCode"))
        self.labelAccessCode = QtGui.QLabel(self.groupBoxList)
        self.labelAccessCode.setGeometry(QtCore.QRect(140, 140, 221, 16))
        self.labelAccessCode.setObjectName(_fromUtf8("labelAccessCode"))
        self.pushButtonLogin = QtGui.QPushButton(self.groupBoxList)
        self.pushButtonLogin.setGeometry(QtCore.QRect(200, 250, 101, 23))
        self.pushButtonLogin.setObjectName(_fromUtf8("pushButtonLogin"))
        self.labelLogin = QtGui.QLabel(self.groupBoxList)
        self.labelLogin.setGeometry(QtCore.QRect(120, 210, 281, 23))
        self.labelLogin.setText(_fromUtf8(""))
        self.labelLogin.setObjectName(_fromUtf8("labelLogin"))

        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(290, 240, 351, 211))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateEditCamp2Start = QtGui.QDateEdit(self.frame)
        self.dateEditCamp2Start.setObjectName(_fromUtf8("dateEditCamp2Start"))
        self.dateEditCamp2Start.setDisplayFormat('yyyy/MM/dd')
        self.gridLayout.addWidget(self.dateEditCamp2Start, 3, 1, 1, 1)
        self.dateEditCampStart = QtGui.QDateEdit(self.frame)
        self.dateEditCampStart.setObjectName(_fromUtf8("dateEditCampStart"))
        self.dateEditCampStart.setDisplayFormat('yyyy/MM/dd')
        self.gridLayout.addWidget(self.dateEditCampStart, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.dateEditCamp3End = QtGui.QDateEdit(self.frame)
        self.dateEditCamp3End.setObjectName(_fromUtf8("dateEditCamp3End"))
        self.dateEditCamp3End.setDisplayFormat('yyyy/MM/dd')
        self.gridLayout.addWidget(self.dateEditCamp3End, 4, 2, 1, 1)
        self.dateEditCamp2End = QtGui.QDateEdit(self.frame)
        self.dateEditCamp2End.setObjectName(_fromUtf8("dateEditCamp2End"))
        self.dateEditCamp2End.setDisplayFormat('yyyy/MM/dd')
        self.gridLayout.addWidget(self.dateEditCamp2End, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.dateEditCamp3Start = QtGui.QDateEdit(self.frame)
        self.dateEditCamp3Start.setObjectName(_fromUtf8("dateEditCamp3Start"))
        self.dateEditCamp3Start.setDisplayFormat('yyyy/MM/dd')
        self.gridLayout.addWidget(self.dateEditCamp3Start, 4, 1, 1, 1)
        self.dateEditCamp1End = QtGui.QDateEdit(self.frame)
        self.dateEditCamp1End.setObjectName(_fromUtf8("dateEditCamp1End"))
        self.dateEditCamp1End.setDisplayFormat('yyyy/MM/dd')
        self.gridLayout.addWidget(self.dateEditCamp1End, 1, 2, 1, 1)
        self.pushButtonCampDates = QtGui.QPushButton(self.frame)
        self.pushButtonCampDates.setObjectName(_fromUtf8("pushButtonCampDates"))
        self.gridLayout.addWidget(self.pushButtonCampDates, 5, 1, 1, 1)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(LoginWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LoginWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(LoginWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 993, 36))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuApplicant = QtGui.QMenu(self.menuBar)
        self.menuApplicant.setObjectName(_fromUtf8("menuApplicant"))
        self.menuSetting = QtGui.QMenu(self.menuBar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        LoginWindow.setMenuBar(self.menuBar)
        self.actionAdd_New = QtGui.QAction(LoginWindow)
        self.actionAdd_New.setObjectName(_fromUtf8("actionAdd_New"))
        self.actionLook_Up = QtGui.QAction(LoginWindow)
        self.actionLook_Up.setObjectName(_fromUtf8("actionLook_Up"))
        self.actionChange_Camp_Dates = QtGui.QAction(LoginWindow)
        self.actionChange_Camp_Dates.setObjectName(_fromUtf8("actionChange_Camp_Dates"))

        self.menuApplicant.addAction(self.actionAdd_New)
        self.menuApplicant.addAction(self.actionLook_Up)
        self.menuSetting.addAction(self.actionChange_Camp_Dates)
        self.menuBar.addAction(self.menuApplicant.menuAction())
        self.menuBar.addAction(self.menuSetting.menuAction())

        self.p = p
        self.director_pw = '12345'
        self.regClerk_pw = '54321'
        self.menuBar.hide()
        self.frame.hide()
        self.pushButtonLogin.clicked.connect(lambda:self.login())
        self.actionAdd_New.triggered.connect(lambda:self.showNewApplicantDialog())
        self.actionLook_Up.triggered.connect(lambda:self.showLookUpApplicant())
        self.actionChange_Camp_Dates.triggered.connect(lambda:self.showChangeCampDate())
        self.pushButtonCampDates.clicked.connect(lambda:self.changeCampDate())

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    
    def login(self):
        if self.radioButtonDirector.isChecked() and not self.radioButtonRegClerk.isChecked():
            if self.lineEditAccessCode.text()!=self.director_pw:
                    self.labelLogin.setText("wrong access code")
            else:
                self.labelLogin.setText("welcome")
                self.menuBar.show()
                self.groupBoxList.hide()

        elif not self.radioButtonDirector.isChecked() and self.radioButtonRegClerk.isChecked():
            if self.lineEditAccessCode.text()!=self.regClerk_pw:
                self.labelLogin.setText("wrong access code")
            else:
                self.groupBoxList.hide()
                self.labelLogin.setText("welcome")
                self.menuSetting.menuAction().setVisible(False)
                self.menuBar.show()
                
        elif not self.radioButtonDirector.isChecked() and not self.radioButtonRegClerk.isChecked():
            self.labelLogin.setText('please select an user to login')

    def showNewApplicantDialog(self):
        self.DialogAddNewApplicant = QtGui.QDialog()
        self.ui_addNew = Ui_DialogAddNewApplicant()
        self.ui_addNew.setupUi(self.DialogAddNewApplicant,self.p)
        self.DialogAddNewApplicant.show()
    
    def showLookUpApplicant(self):
        self.DialogLookUpApplicant = QtGui.QDialog()
        self.ui_lookUP = Ui_DialogLookUpApplicant()
        self.ui_lookUP.setupUi(self.DialogLookUpApplicant,self.p)
        self.DialogLookUpApplicant.show()

    def showChangeCampDate(self):
        self.groupBoxList.hide()
        self.frame.show()
        camps = self.p.camps
        startDate = datetime.datetime.strptime(camps[0].startDate,'%Y-%m-%d')
        self.dateEditCampStart.setDate(QtCore.QDate(startDate.year,startDate.month,startDate.day))
        endDate = datetime.datetime.strptime(camps[0].endDate,'%Y-%m-%d')
        self.dateEditCamp1End.setDate(QtCore.QDate(endDate.year,endDate.month,endDate.day))
        
        startDate = datetime.datetime.strptime(camps[1].startDate,'%Y-%m-%d')
        self.dateEditCamp2Start.setDate(QtCore.QDate(startDate.year,startDate.month,startDate.day))
        endDate = datetime.datetime.strptime(camps[1].endDate,'%Y-%m-%d')
        self.dateEditCamp2End.setDate(QtCore.QDate(endDate.year,endDate.month,endDate.day))

        startDate = datetime.datetime.strptime(camps[2].startDate,'%Y-%m-%d')
        self.dateEditCamp3Start.setDate(QtCore.QDate(startDate.year,startDate.month,startDate.day))
        endDate = datetime.datetime.strptime(camps[2].endDate,'%Y-%m-%d')
        self.dateEditCamp3End.setDate(QtCore.QDate(endDate.year,endDate.month,endDate.day))

    def changeCampDate(self):
        startDate = self.dateEditCampStart.date().toPyDate()
        endDate = self.dateEditCamp1End.date().toPyDate()
        self.p.interacteDB('update','camp',{'newData':{'startDate':startDate,'endDate':endDate},'conditions':{'id':1}})
        startDate = self.dateEditCamp2Start.date().toPyDate()
        endDate = self.dateEditCamp2End.date().toPyDate()
        self.p.interacteDB('update','camp',{'newData':{'startDate':startDate,'endDate':endDate},'conditions':{'id':2}})
        startDate = self.dateEditCamp3Start.date().toPyDate()
        endDate = self.dateEditCamp3End.date().toPyDate()
        self.p.interacteDB('update','camp',{'newData':{'startDate':startDate,'endDate':endDate},'conditions':{'id':3}})
        self.p.camps = self.p.registerCamps()
        self.frame.hide()



        
            

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login", None))
        self.label.setText(_translate("LoginWindow", "Gila Breath Camp", None))
        self.radioButtonDirector.setText(_translate("LoginWindow", "Director", None))
        self.radioButtonRegClerk.setText(_translate("LoginWindow", "Registration Clerk", None))
        self.labelAccessCode.setText(_translate("LoginWindow", "Access Code:", None))
        self.pushButtonLogin.setText(_translate("LoginWindow", "Login", None))
        self.label_4.setText(_translate("LoginWindow", "Camp 1", None))
        self.label_3.setText(_translate("LoginWindow", "Camp 1", None))
        self.label_2.setText(_translate("LoginWindow", "Camp 1", None))
        self.label_6.setText(_translate("LoginWindow", "End Date", None))
        self.label_5.setText(_translate("LoginWindow", "Start Date", None))
        self.pushButtonCampDates.setText(_translate("LoginWindow", "Submit", None))
        self.menuApplicant.setTitle(_translate("LoginWindow", "Applicant", None))
        self.menuSetting.setTitle(_translate("LoginWindow", "Setting", None))
        self.actionAdd_New.setText(_translate("LoginWindow", "Add New Applicant", None))
        self.actionLook_Up.setText(_translate("LoginWindow", "Look Up", None))
        self.actionChange_Camp_Dates.setText(_translate("LoginWindow", "Change Camp Dates", None))













class Ui_DialogAddNewApplicant(object):
    def setupUi(self, DialogAddNewApplicant, p):
        DialogAddNewApplicant.setObjectName(_fromUtf8("DialogAddNewApplicant"))
        DialogAddNewApplicant.resize(1389, 1010)
        DialogAddNewApplicant.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        DialogAddNewApplicant.setAutoFillBackground(False)
        DialogAddNewApplicant.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(DialogAddNewApplicant)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(DialogAddNewApplicant)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelCamp = QtGui.QLabel(self.frame)
        self.labelCamp.setObjectName(_fromUtf8("labelCamp"))
        self.horizontalLayout.addWidget(self.labelCamp)
        self.comboBoxCamp = QtGui.QComboBox(self.frame)
        self.comboBoxCamp.setObjectName(_fromUtf8("comboBoxCamp"))
        self.horizontalLayout.addWidget(self.comboBoxCamp)
        self.labelCampAvilability = QtGui.QLabel(self.frame)
        self.labelCampAvilability.setObjectName(_fromUtf8("labelCampAvilability"))
        self.horizontalLayout.addWidget(self.labelCampAvilability)
        self.gridLayout.addWidget(self.frame, 6, 3, 1, 2)
        self.label_14 = QtGui.QLabel(DialogAddNewApplicant)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 13, 1, 1, 4)
        self.comboBoxTribe = QtGui.QComboBox(DialogAddNewApplicant)
        self.comboBoxTribe.setObjectName(_fromUtf8("comboBoxTribe"))
        self.gridLayout.addWidget(self.comboBoxTribe, 21, 4, 1, 1)
        self.labelFirstName = QtGui.QLabel(DialogAddNewApplicant)
        self.labelFirstName.setObjectName(_fromUtf8("labelFirstName"))
        self.gridLayout.addWidget(self.labelFirstName, 1, 1, 1, 1)
        self.lineFirstName = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineFirstName.setObjectName(_fromUtf8("lineFirstName"))
        self.gridLayout.addWidget(self.lineFirstName, 1, 2, 1, 1)
        self.comboBoxBunkhouse = QtGui.QComboBox(DialogAddNewApplicant)
        self.comboBoxBunkhouse.setObjectName(_fromUtf8("comboBoxBunkhouse"))
        self.gridLayout.addWidget(self.comboBoxBunkhouse, 21, 2, 1, 1)
        self.dateApplicationDate = QtGui.QDateEdit(DialogAddNewApplicant)
        self.dateApplicationDate.setDisplayFormat('yyyy/MM/dd')
        self.dateApplicationDate.setObjectName(_fromUtf8("dateApplicationDate"))
        self.gridLayout.addWidget(self.dateApplicationDate, 17, 2, 1, 1)
        self.labelPayment = QtGui.QLabel(DialogAddNewApplicant)
        self.labelPayment.setObjectName(_fromUtf8("labelPayment"))
        self.gridLayout.addWidget(self.labelPayment, 18, 1, 1, 1)
        self.checkBoxPayment = QtGui.QCheckBox(DialogAddNewApplicant)
        self.checkBoxPayment.setObjectName(_fromUtf8("checkBoxPayment"))
        self.gridLayout.addWidget(self.checkBoxPayment, 18, 2, 1, 1)
        self.labelLine2 = QtGui.QLabel(DialogAddNewApplicant)
        self.labelLine2.setObjectName(_fromUtf8("labelLine2"))
        self.gridLayout.addWidget(self.labelLine2, 9, 3, 1, 1)
        self.labelDOB = QtGui.QLabel(DialogAddNewApplicant)
        self.labelDOB.setObjectName(_fromUtf8("labelDOB"))
        self.gridLayout.addWidget(self.labelDOB, 2, 3, 1, 1)
        self.labelAcceptanceDecision = QtGui.QLabel(DialogAddNewApplicant)
        self.labelAcceptanceDecision.setObjectName(_fromUtf8("labelAcceptanceDecision"))
        self.gridLayout.addWidget(self.labelAcceptanceDecision, 18, 3, 1, 1)
        self.line = QtGui.QFrame(DialogAddNewApplicant)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 7, 1, 1, 4)
        self.labelEmergencyName = QtGui.QLabel(DialogAddNewApplicant)
        self.labelEmergencyName.setObjectName(_fromUtf8("labelEmergencyName"))
        self.gridLayout.addWidget(self.labelEmergencyName, 14, 1, 1, 1)
        self.dateReviewDate = QtGui.QDateEdit(DialogAddNewApplicant)
        self.dateReviewDate.setDisplayFormat('yyyy/MM/dd')
        self.dateReviewDate.setObjectName(_fromUtf8("dateReviewDate"))
        self.gridLayout.addWidget(self.dateReviewDate, 17, 4, 1, 1)
        self.labelReviewDate = QtGui.QLabel(DialogAddNewApplicant)
        self.labelReviewDate.setObjectName(_fromUtf8("labelReviewDate"))
        self.gridLayout.addWidget(self.labelReviewDate, 17, 3, 1, 1)
        self.labelBunkhouse = QtGui.QLabel(DialogAddNewApplicant)
        self.labelBunkhouse.setObjectName(_fromUtf8("labelBunkhouse"))
        self.gridLayout.addWidget(self.labelBunkhouse, 21, 1, 1, 1)
        self.labelApplicationDate = QtGui.QLabel(DialogAddNewApplicant)
        self.labelApplicationDate.setObjectName(_fromUtf8("labelApplicationDate"))
        self.gridLayout.addWidget(self.labelApplicationDate, 17, 1, 1, 1)
        self.lineEmergencyPhone = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineEmergencyPhone.setObjectName(_fromUtf8("lineEmergencyPhone"))
        self.gridLayout.addWidget(self.lineEmergencyPhone, 14, 4, 1, 1)
        self.labelLine1 = QtGui.QLabel(DialogAddNewApplicant)
        self.labelLine1.setObjectName(_fromUtf8("labelLine1"))
        self.gridLayout.addWidget(self.labelLine1, 9, 1, 1, 1)
        self.labelEquipmentsCheck = QtGui.QLabel(DialogAddNewApplicant)
        self.labelEquipmentsCheck.setObjectName(_fromUtf8("labelEquipmentsCheck"))
        self.gridLayout.addWidget(self.labelEquipmentsCheck, 19, 3, 1, 1)
        self.lineCity = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineCity.setObjectName(_fromUtf8("lineCity"))
        self.gridLayout.addWidget(self.lineCity, 10, 2, 1, 1)
        self.labelEmergencyPhone = QtGui.QLabel(DialogAddNewApplicant)
        self.labelEmergencyPhone.setObjectName(_fromUtf8("labelEmergencyPhone"))
        self.gridLayout.addWidget(self.labelEmergencyPhone, 14, 3, 1, 1)
        self.lineState = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineState.setObjectName(_fromUtf8("lineState"))
        self.gridLayout.addWidget(self.lineState, 10, 4, 1, 1)
        self.lineEmergencyName = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineEmergencyName.setObjectName(_fromUtf8("lineEmergencyName"))
        self.gridLayout.addWidget(self.lineEmergencyName, 14, 2, 1, 1)
        self.lineLine2 = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineLine2.setObjectName(_fromUtf8("lineLine2"))
        self.gridLayout.addWidget(self.lineLine2, 9, 4, 1, 1)
        self.checkBoxFormsCheck = QtGui.QCheckBox(DialogAddNewApplicant)
        self.checkBoxFormsCheck.setObjectName(_fromUtf8("checkBoxFormsCheck"))
        self.gridLayout.addWidget(self.checkBoxFormsCheck, 19, 2, 1, 1)
        self.labelZipCode = QtGui.QLabel(DialogAddNewApplicant)
        self.labelZipCode.setObjectName(_fromUtf8("labelZipCode"))
        self.gridLayout.addWidget(self.labelZipCode, 11, 1, 1, 1)
        self.lineLine1 = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineLine1.setObjectName(_fromUtf8("lineLine1"))
        self.gridLayout.addWidget(self.lineLine1, 9, 2, 1, 1)
        self.checkBoxEquipmentsCheck = QtGui.QCheckBox(DialogAddNewApplicant)
        self.checkBoxEquipmentsCheck.setObjectName(_fromUtf8("checkBoxEquipmentsCheck"))
        self.gridLayout.addWidget(self.checkBoxEquipmentsCheck, 19, 4, 1, 1)
        self.labelFormsCheck = QtGui.QLabel(DialogAddNewApplicant)
        self.labelFormsCheck.setObjectName(_fromUtf8("labelFormsCheck"))
        self.gridLayout.addWidget(self.labelFormsCheck, 19, 1, 1, 1)
        self.label_17 = QtGui.QLabel(DialogAddNewApplicant)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 16, 1, 1, 1)
        self.comboBoxAcceptanceDecision = QtGui.QComboBox(DialogAddNewApplicant)
        self.comboBoxAcceptanceDecision.setObjectName(_fromUtf8("comboBoxAcceptanceDecision"))
        self.gridLayout.addWidget(self.comboBoxAcceptanceDecision, 18, 4, 1, 1)
        self.labelHomePhone = QtGui.QLabel(DialogAddNewApplicant)
        self.labelHomePhone.setObjectName(_fromUtf8("labelHomePhone"))
        self.gridLayout.addWidget(self.labelHomePhone, 5, 3, 1, 1)
        self.labelTribe = QtGui.QLabel(DialogAddNewApplicant)
        self.labelTribe.setObjectName(_fromUtf8("labelTribe"))
        self.gridLayout.addWidget(self.labelTribe, 21, 3, 1, 1)
        self.lineCellPhone = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineCellPhone.setObjectName(_fromUtf8("lineCellPhone"))
        self.gridLayout.addWidget(self.lineCellPhone, 6, 2, 1, 1)
        self.lineZipCode = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineZipCode.setObjectName(_fromUtf8("lineZipCode"))
        self.gridLayout.addWidget(self.lineZipCode, 11, 2, 1, 1)
        self.dateEditDOB = QtGui.QDateEdit(DialogAddNewApplicant)
        self.dateEditDOB.setObjectName(_fromUtf8("dateEditDOB"))
        self.dateEditDOB.setDisplayFormat('yyyy/MM/dd')
        self.gridLayout.addWidget(self.dateEditDOB, 2, 4, 1, 1)
        self.line_3 = QtGui.QFrame(DialogAddNewApplicant)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 15, 1, 1, 4)
        self.labelEmail = QtGui.QLabel(DialogAddNewApplicant)
        self.labelEmail.setObjectName(_fromUtf8("labelEmail"))
        self.gridLayout.addWidget(self.labelEmail, 5, 1, 1, 1)
        self.labelLastName = QtGui.QLabel(DialogAddNewApplicant)
        self.labelLastName.setObjectName(_fromUtf8("labelLastName"))
        self.gridLayout.addWidget(self.labelLastName, 1, 3, 1, 1)
        self.lineHomePhone = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineHomePhone.setObjectName(_fromUtf8("lineHomePhone"))
        self.gridLayout.addWidget(self.lineHomePhone, 5, 4, 1, 1)
        self.labelGender = QtGui.QLabel(DialogAddNewApplicant)
        self.labelGender.setObjectName(_fromUtf8("labelGender"))
        self.gridLayout.addWidget(self.labelGender, 2, 1, 1, 1)
        self.lineGender = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineGender.setObjectName(_fromUtf8("lineGender"))
        self.gridLayout.addWidget(self.lineGender, 2, 2, 1, 1)
        self.lineLastName = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineLastName.setObjectName(_fromUtf8("lineLastName"))
        self.gridLayout.addWidget(self.lineLastName, 1, 4, 1, 1)
        self.lineEmail = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineEmail.setObjectName(_fromUtf8("lineEmail"))
        self.gridLayout.addWidget(self.lineEmail, 5, 2, 1, 1)
        self.labelCity = QtGui.QLabel(DialogAddNewApplicant)
        self.labelCity.setObjectName(_fromUtf8("labelCity"))
        self.gridLayout.addWidget(self.labelCity, 10, 1, 1, 1)
        self.line_2 = QtGui.QFrame(DialogAddNewApplicant)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 12, 1, 1, 4)
        self.labelState = QtGui.QLabel(DialogAddNewApplicant)
        self.labelState.setObjectName(_fromUtf8("labelState"))
        self.gridLayout.addWidget(self.labelState, 10, 3, 1, 1)
        self.labelCellPhone = QtGui.QLabel(DialogAddNewApplicant)
        self.labelCellPhone.setObjectName(_fromUtf8("labelCellPhone"))
        self.gridLayout.addWidget(self.labelCellPhone, 6, 1, 1, 1)
        self.label_5 = QtGui.QLabel(DialogAddNewApplicant)
        self.label_5.setMinimumSize(QtCore.QSize(90, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 8, 1, 1, 1)
        self.label_18 = QtGui.QLabel(DialogAddNewApplicant)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 0, 1, 1, 2)
        
        
        self.labelWarningMsg = QtGui.QLabel(DialogAddNewApplicant)
        self.labelWarningMsg.setObjectName(_fromUtf8("labelWarningMsg"))
        self.labelWarningMsg.setStyleSheet("color:red")
        self.gridLayout.addWidget(self.labelWarningMsg, 0, 3, 1, 2)
        


        self.widget = QtGui.QWidget(DialogAddNewApplicant)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 8, 2, 1, 2)
        self.frame_2 = QtGui.QFrame(DialogAddNewApplicant)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButtonGenerateLetter = QtGui.QPushButton(self.frame_2)
        self.pushButtonGenerateLetter.setGeometry(QtCore.QRect(740, 30, 291, 40))
        self.pushButtonGenerateLetter.setObjectName(_fromUtf8("pushButtonGenerateLetter"))
        self.pushButtonSubmit = QtGui.QPushButton(self.frame_2)
        self.pushButtonSubmit.setGeometry(QtCore.QRect(1050, 30, 281, 40))
        self.pushButtonSubmit.setObjectName(_fromUtf8("pushButtonSubmit"))
        self.pushButtonCheckList = QtGui.QPushButton(self.frame_2)
        self.pushButtonCheckList.setGeometry(QtCore.QRect(510, 30, 211, 40))
        self.pushButtonCheckList.setObjectName(_fromUtf8("pushButtonCheckList"))
        self.gridLayout.addWidget(self.frame_2, 22, 1, 1, 4)
        # click submit button
        self.pushButtonSubmit.clicked.connect(lambda:self.submitDataToDB(DialogAddNewApplicant))
        self.pushButtonGenerateLetter.clicked.connect(lambda:self.generateLetter(DialogAddNewApplicant))
        self.pushButtonCheckList.clicked.connect(lambda:self.generateCheckList(DialogAddNewApplicant))
        # value changes
        self.comboBoxCamp.currentIndexChanged.connect(lambda:self.showCampAvilability())

        self.dateEditDOB = QtGui.QDateEdit(DialogAddNewApplicant)
        self.dateEditDOB.setObjectName(_fromUtf8("dateEditDOB"))
        self.dateEditDOB.setDate(QtCore.QDate(1800,1,1))
        self.dateEditDOB.setDisplayFormat('yyyy/MM/dd')
        self.gridLayout.addWidget(self.dateEditDOB, 2, 4, 1, 1)

        self.retranslateUi(DialogAddNewApplicant)
        QtCore.QMetaObject.connectSlotsByName(DialogAddNewApplicant)
        DialogAddNewApplicant.setTabOrder(self.lineFirstName, self.lineLastName)
        DialogAddNewApplicant.setTabOrder(self.lineLastName, self.lineGender)
        DialogAddNewApplicant.setTabOrder(self.lineGender, self.dateEditDOB)
        DialogAddNewApplicant.setTabOrder(self.dateEditDOB, self.lineEmail)
        DialogAddNewApplicant.setTabOrder(self.lineEmail, self.lineHomePhone)
        DialogAddNewApplicant.setTabOrder(self.lineHomePhone, self.lineCellPhone)
        DialogAddNewApplicant.setTabOrder(self.lineCellPhone, self.comboBoxCamp)
        DialogAddNewApplicant.setTabOrder(self.comboBoxCamp, self.lineLine1)
        DialogAddNewApplicant.setTabOrder(self.lineLine1, self.lineLine2)
        DialogAddNewApplicant.setTabOrder(self.lineLine2, self.lineCity)
        DialogAddNewApplicant.setTabOrder(self.lineCity, self.lineState)
        DialogAddNewApplicant.setTabOrder(self.lineState, self.lineZipCode)
        DialogAddNewApplicant.setTabOrder(self.lineZipCode, self.lineEmergencyName)
        DialogAddNewApplicant.setTabOrder(self.lineEmergencyName, self.lineEmergencyPhone)
        DialogAddNewApplicant.setTabOrder(self.lineEmergencyPhone, self.dateApplicationDate)
        DialogAddNewApplicant.setTabOrder(self.dateApplicationDate, self.dateReviewDate)
        DialogAddNewApplicant.setTabOrder(self.dateReviewDate, self.checkBoxPayment)
        DialogAddNewApplicant.setTabOrder(self.checkBoxPayment, self.comboBoxAcceptanceDecision)
        DialogAddNewApplicant.setTabOrder(self.comboBoxAcceptanceDecision, self.checkBoxFormsCheck)
        DialogAddNewApplicant.setTabOrder(self.checkBoxFormsCheck, self.checkBoxEquipmentsCheck)
        DialogAddNewApplicant.setTabOrder(self.checkBoxEquipmentsCheck, self.comboBoxBunkhouse)
        DialogAddNewApplicant.setTabOrder(self.comboBoxBunkhouse, self.comboBoxTribe)
        DialogAddNewApplicant.setTabOrder(self.comboBoxTribe, self.pushButtonCheckList)
        DialogAddNewApplicant.setTabOrder(self.pushButtonCheckList, self.pushButtonGenerateLetter)
        DialogAddNewApplicant.setTabOrder(self.pushButtonGenerateLetter, self.pushButtonSubmit)
        self.p = p
        self.comboBoxCamp.addItem('')
        self.comboBoxBunkhouse.addItem('')
        self.comboBoxTribe.addItem('')
        self.comboBoxAcceptanceDecision.addItem('')
        self.comboBoxCamp.addItems([str(x.name) for x in self.p.camps])
        self.comboBoxBunkhouse.addItems([str(x.name) for x in self.p.bunkhouses])
        self.comboBoxTribe.addItems([str(x.name) for x in self.p.tribes])
        self.comboBoxAcceptanceDecision.addItems(['1-Accept','2-Conditional Accept', '3-Denial', '4-Canceled'])

        # list = [firstName, lastName,..]
    def showCampAvilability(self):
        campId = self.comboBoxCamp.currentIndex()
        if campId ==0:
            return
        else:
            boys = self.p.interacteDB('select','applicant','campId = \''+str(campId)+\
        '\' and gender = \''+'M'+ '\' and decisionId != \'3\' ')
            girls = self.p.interacteDB('select','applicant','campId = \''+str(campId)+\
        '\' and gender = \''+'F'+ '\' and decisionId != \'3\' ')
        self.labelCampAvilability.setText('M: ' + str(self.p.camps[campId-1].totalBoyNumber - len(boys['result']))+', F:'+str(self.p.camps[campId-1].totalGrilNumber -len(girls['result'])))
        

    def checkBlankCells(self):
        if self.lineFirstName.text()=='' or self.lineGender.text()==''\
        or self.lineLastName.text()=='' or self.dateEditDOB.date().toPyDate()==datetime.date(1800,1,1)\
        or self.lineEmail.text()=='' or self.lineHomePhone.text()=='' or self.lineCellPhone.text()==''\
        or self.comboBoxCamp.currentIndex==0 or self.lineLine1.text()=='' or self.lineCity.text()==''\
        or self.lineState.text()=='' or self.lineZipCode.text()=='':
            return True
        else:
            return False
        
    def generateLetter(self,DialogAddNewApplicant):
        letter = self.p.generateLetterOfAcceptance(self.comboBoxAcceptanceDecision.currentIndex(),\
        self.p.camps[self.comboBoxCamp.currentIndex()-1])

        self.DialogLetterOfAcceptance = QtGui.QDialog()
        self.ui_acceptanceLetter = Ui_DialogLetterOfAcceptance()
        self.ui_acceptanceLetter.setupUi(self.DialogLetterOfAcceptance)
        self.ui_acceptanceLetter.writeLetter(letter)
        
        self.DialogLetterOfAcceptance.show()

        # QtGui.QMessageBox.warning(DialogAddNewApplicant,"Letter Of Acceptance",
        # letter, QtGui.QMessageBox.Cancel,
        # QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
        # QtGui.QMessageBox.about(DialogAddNewApplicant,'Letter Of Acceptance',letter)
    def generateCheckList(self,DialogAddNewApplicant):
        cl_form = self.p.generateCheckList('form')
        cl_equipment = self.p.generateCheckList('equipment')
        cl = 'Forms:\n'+cl_form + '\n'+'Equipments:\n'+cl_equipment

        self.DialogLetterOfAcceptance = QtGui.QDialog()
        self.ui_acceptanceLetter = Ui_DialogLetterOfAcceptance()
        self.ui_acceptanceLetter.setupUi(self.DialogLetterOfAcceptance)
        self.ui_acceptanceLetter.writeLetter(cl)
        
        self.DialogLetterOfAcceptance.show()
        
    def submitDataToDB(self,DialogAddNewApplicant):
        firstName = self.lineFirstName.text()
        lastName = self.lineLastName.text()
        gender = self.lineGender.text()
        dateOfBirth =self.dateEditDOB.date().toPyDate()
        
        email = self.lineEmail.text()
        homePhone = self.lineHomePhone.text()
        cellPhone = self.lineCellPhone.text()
        campId = self.comboBoxCamp.currentIndex()
        line1 = self.lineLine1.text()
        line2 = self.lineLine2.text()
        city = self.lineCity.text()
        state = self.lineState.text()
        zipCode = self.lineZipCode.text()
        emergencyContactName = self.lineEmergencyName.text()
        emergencyContactPhone = self.lineEmergencyPhone.text()
        applicationDate = self.dateApplicationDate.date().toPyDate()
        age =applicationDate.year - dateOfBirth.year
        reviewDate = self.dateReviewDate.date().toPyDate()
        payment = 1 if self.checkBoxPayment.isChecked() else 0
        decisionId = self.comboBoxAcceptanceDecision.currentIndex()
        formsChecked = 1 if self.checkBoxFormsCheck.isChecked() else 0
        equipmentsChecked = 1 if self.checkBoxEquipmentsCheck.isChecked() else 0
        bunkhouseId = self.comboBoxBunkhouse.currentIndex()
        tribeId = self.comboBoxTribe.currentIndex()

        a = Applicant(firstName = firstName,lastName = lastName,age = age,gender = gender,\
        dateOfBirth = dateOfBirth,email = email, homePhone = homePhone, cellPhone = cellPhone,\
        emergencyContactPhone = emergencyContactPhone,emergencyContactName = emergencyContactName,\
        line1 = line1,line2 = line2,city = city,state = state,zipCode = zipCode,payment = payment,
        applicationDate = applicationDate,
        reviewDate = reviewDate,decisionId = decisionId,formsChecked = formsChecked,\
        equipmentsChecked = equipmentsChecked,campId = campId,bunkhouseId = bunkhouseId,\
        tribeId = tribeId)
        validationRes = self.p.validateApplicant(campId,gender,age)

        if self.checkBlankCells():
            
            # QtGui.QMessageBox.warning(DialogAddNewApplicant,"Invalid Inputs",
            # "The fileds with * cannot be empty.", QtGui.QMessageBox.Cancel,
            # QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
            self.labelWarningMsg.clear()
            self.labelWarningMsg.setText("The fileds with * cannot be empty")
            
        elif self.comboBoxAcceptanceDecision.currentIndex() == 1 and not validationRes['ok']:
            
            # QtGui.QMessageBox.warning(DialogAddNewApplicant,"Application cannot be accepted",
            # "This application cannot be accepted due to {}".format(validationRes['msg']), QtGui.QMessageBox.Cancel,
            # QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
            self.labelWarningMsg.clear()
            self.labelWarningMsg.setText("This application cannot be accepted due to {}".format(validationRes['msg']))
        
        elif self.comboBoxAcceptanceDecision.currentIndex() == 1 and not self.checkBoxPayment.isChecked():
            # QtGui.QMessageBox.warning(DialogAddNewApplicant,"Application cannot be accepted",
            # "This application cannot be accepted since the payment check has not been recieve", QtGui.QMessageBox.Cancel,
            # QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
            self.labelWarningMsg.clear()
            self.labelWarningMsg.setText("This application cannot be accepted since the payment check has not been recieve")

        else:
            res = self.p.addNewApplicant(a)
            # QtGui.QMessageBox.warning(DialogAddNewApplicant,"Success",
            # res['result']['msg'], QtGui.QMessageBox.Ok,
            # QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
            self.labelWarningMsg.clear()
            self.labelWarningMsg.setText("Success! {}".format(validationRes['msg']))
        
            DialogAddNewApplicant.accept()

            

            # popup window
        

    def retranslateUi(self, DialogAddNewApplicant):
        DialogAddNewApplicant.setWindowTitle(_translate("DialogAddNewApplicant", "Add New Applicant", None))
        self.labelCamp.setText(_translate("DialogAddNewApplicant", "Camp Interested*", None))
        self.labelCampAvilability.setText(_translate("DialogAddNewApplicant", "-", None))
        self.label_14.setText(_translate("DialogAddNewApplicant", "Emergency Contact:", None))
        self.labelFirstName.setText(_translate("DialogAddNewApplicant", "First Name*", None))
        self.labelPayment.setText(_translate("DialogAddNewApplicant", "Payment", None))
        self.checkBoxPayment.setText(_translate("DialogAddNewApplicant", "Check Recieved?", None))
        self.labelLine2.setText(_translate("DialogAddNewApplicant", "Line 2", None))
        self.labelDOB.setText(_translate("DialogAddNewApplicant", "Date of Birth*", None))
        self.labelAcceptanceDecision.setText(_translate("DialogAddNewApplicant", "Accepted?", None))
        self.labelEmergencyName.setText(_translate("DialogAddNewApplicant", "Name", None))
        self.labelReviewDate.setText(_translate("DialogAddNewApplicant", "Review Date", None))
        self.labelBunkhouse.setText(_translate("DialogAddNewApplicant", "Bunkhouse", None))
        self.labelApplicationDate.setText(_translate("DialogAddNewApplicant", "Application Date", None))
        self.labelLine1.setText(_translate("DialogAddNewApplicant", "Line 1*", None))
        self.labelEquipmentsCheck.setText(_translate("DialogAddNewApplicant", "Equipments", None))
        self.labelEmergencyPhone.setText(_translate("DialogAddNewApplicant", "Phone", None))
        self.checkBoxFormsCheck.setText(_translate("DialogAddNewApplicant", "Camper has all required forms?", None))
        self.labelZipCode.setText(_translate("DialogAddNewApplicant", "ZipCode*", None))
        self.checkBoxEquipmentsCheck.setText(_translate("DialogAddNewApplicant", "Camper has all required equipments?", None))
        self.labelFormsCheck.setText(_translate("DialogAddNewApplicant", "Forms", None))
        self.label_17.setText(_translate("DialogAddNewApplicant", "Admin:", None))
        self.labelHomePhone.setText(_translate("DialogAddNewApplicant", "Home Phone*", None))
        self.labelTribe.setText(_translate("DialogAddNewApplicant", "Tribe", None))
        self.labelEmail.setText(_translate("DialogAddNewApplicant", "Email*", None))
        self.labelLastName.setText(_translate("DialogAddNewApplicant", "Last Name*", None))
        self.labelGender.setText(_translate("DialogAddNewApplicant", "Gender*", None))
        self.labelCity.setText(_translate("DialogAddNewApplicant", "City*", None))
        self.labelState.setText(_translate("DialogAddNewApplicant", "State*", None))
        self.labelCellPhone.setText(_translate("DialogAddNewApplicant", "Cell Phone*", None))
        self.label_5.setText(_translate("DialogAddNewApplicant", "Address:", None))
        self.label_18.setText(_translate("DialogAddNewApplicant", "Applicant Basic Information:", None))
        self.pushButtonGenerateLetter.setText(_translate("DialogAddNewApplicant", "Generate Acceptance Letter", None))
        self.pushButtonSubmit.setText(_translate("DialogAddNewApplicant", "Submit", None))
        self.pushButtonCheckList.setText(_translate("DialogAddNewApplicant", "Checkin Checklist", None))


class Ui_DialogLookUpApplicant(object):
    def setupUi(self, DialogLookUpApplicant,p):
        DialogLookUpApplicant.setObjectName(_fromUtf8("DialogLookUpApplicant"))
        DialogLookUpApplicant.resize(1229, 784)
        self.gridLayout = QtGui.QGridLayout(DialogLookUpApplicant)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelLastName = QtGui.QLabel(DialogLookUpApplicant)
        self.labelLastName.setObjectName(_fromUtf8("labelLastName"))
        self.gridLayout.addWidget(self.labelLastName, 0, 2, 1, 1)
        self.labelFirstName = QtGui.QLabel(DialogLookUpApplicant)
        self.labelFirstName.setObjectName(_fromUtf8("labelFirstName"))
        self.gridLayout.addWidget(self.labelFirstName, 0, 0, 1, 1)
        self.lineFirstName = QtGui.QLineEdit(DialogLookUpApplicant)
        self.lineFirstName.setObjectName(_fromUtf8("lineFirstName"))
        self.gridLayout.addWidget(self.lineFirstName, 0, 1, 1, 1)
        self.lineLastName = QtGui.QLineEdit(DialogLookUpApplicant)
        self.lineLastName.setObjectName(_fromUtf8("lineLastName"))
        self.gridLayout.addWidget(self.lineLastName, 0, 3, 1, 1)
        self.pushButtonUpdate = QtGui.QPushButton(DialogLookUpApplicant)
        self.pushButtonUpdate.setObjectName(_fromUtf8("pushButtonUpdate"))
        self.gridLayout.addWidget(self.pushButtonUpdate, 4, 5, 1, 1)
        self.line = QtGui.QFrame(DialogLookUpApplicant)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 6)
        self.tableWidgetApplicantTable = QtGui.QTableWidget(DialogLookUpApplicant)
        self.tableWidgetApplicantTable.setObjectName(_fromUtf8("tableWidgetApplicantTable"))
        self.tableWidgetApplicantTable.setColumnCount(24)
        self.tableWidgetApplicantTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(20, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(21, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(22, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetApplicantTable.setHorizontalHeaderItem(23, item)
        self.gridLayout.addWidget(self.tableWidgetApplicantTable, 3, 0, 1, 6)
        self.labelCamp = QtGui.QLabel(DialogLookUpApplicant)
        self.labelCamp.setObjectName(_fromUtf8("labelCamp"))
        self.gridLayout.addWidget(self.labelCamp, 1, 0, 1, 1)
        self.labelDOB = QtGui.QLabel(DialogLookUpApplicant)
        self.labelDOB.setObjectName(_fromUtf8("labelDOB"))
        self.gridLayout.addWidget(self.labelDOB, 1, 2, 1, 1)
        self.dateEditDOB = QtGui.QDateEdit(DialogLookUpApplicant)
        self.dateEditDOB.setDisplayFormat('yyyy/MM/dd')
        self.dateEditDOB.setObjectName(_fromUtf8("dateEditDOB"))
        self.gridLayout.addWidget(self.dateEditDOB, 1, 3, 1, 1)
        self.pushButtonLookUp = QtGui.QPushButton(DialogLookUpApplicant)
        self.pushButtonLookUp.setObjectName(_fromUtf8("pushButtonLookUp"))
        self.gridLayout.addWidget(self.pushButtonLookUp, 0, 5, 2, 1)
        self.comboBoxCamp = QtGui.QComboBox(DialogLookUpApplicant)
        self.comboBoxCamp.setObjectName(_fromUtf8("comboBoxCamp"))
        self.gridLayout.addWidget(self.comboBoxCamp, 1, 1, 1, 1)
        self.frame = QtGui.QFrame(DialogLookUpApplicant)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 0, 131, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 0, 131, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.frame, 4, 3, 1, 1)

        self.retranslateUi(DialogLookUpApplicant)
        QtCore.QMetaObject.connectSlotsByName(DialogLookUpApplicant)
        DialogLookUpApplicant.setTabOrder(self.lineFirstName, self.lineLastName)
        DialogLookUpApplicant.setTabOrder(self.lineLastName, self.comboBoxCamp)
        DialogLookUpApplicant.setTabOrder(self.comboBoxCamp, self.dateEditDOB)
        DialogLookUpApplicant.setTabOrder(self.dateEditDOB, self.pushButtonLookUp)
        DialogLookUpApplicant.setTabOrder(self.pushButtonLookUp, self.tableWidgetApplicantTable)
        DialogLookUpApplicant.setTabOrder(self.tableWidgetApplicantTable, self.pushButtonUpdate)

        self.p = p
        self.comboBoxCamp.addItem('')
        self.comboBoxCamp.addItems([str(x.name) for x in self.p.camps])
        self.pushButtonLookUp.clicked.connect(lambda: self.lookUpApplicant())
        self.pushButtonUpdate.clicked.connect(lambda: self.display())
        self.pushButton.clicked.connect(lambda:self.p.assignBunkhouses(self.comboBoxCamp.currentIndex()))
        self.pushButton_2.clicked.connect(lambda:self.p.assignTribes(self.comboBoxCamp.currentIndex()))

    def lookUpApplicant(self):
        firstName = self.lineFirstName.text()
        lastName = self.lineLastName.text()
        dob = self.dateEditDOB.date().toPyDate()
        campId = self.comboBoxCamp.currentIndex()
        if firstName=='' and lastName == '' and dob < datetime.date(2001,1,1) and campId ==0:
            condition = ''
        else:
            cols = ['firstName', 'lastName','dateOfBirth','campId']
            values = [firstName,lastName,dob,campId]
            tests = [firstName!='',lastName!='',dob > datetime.date(2001,1,1),campId!=0]
            cons = [cols[i] + '=' +'\''+str(values[i])+'\'' for i in range(len(cols)) if tests[i]]
            condition = ' and '.join(cons)
        res = self.p.interacteDB('select','applicant',condition) 
        applicants = res['result']
        
        self.tableWidgetApplicantTable.clear()
        cols = ['Id','First Name', 'Last Name','Gender','Date Of Birth','Line 1',\
            'Line 2','City','State','Zip Code','Email','Home Phone','Cell Phone',\
            'Payment','Application Date','Review Date','Decision Id','Forms Checked',\
            'Equipments Checked', 'Camp Id', 'Emergency Contact Name', \
            'Emergency Contact Phone','Bunkhouse Id','Tribe Id']
        if len(applicants)>0:
            self.tableWidgetApplicantTable.setRowCount(len(applicants))
            self.tableWidgetApplicantTable.setColumnCount(len(cols))

            
            for i in range(24):
                self.tableWidgetApplicantTable.setHorizontalHeaderItem(i, QtGui.QTableWidgetItem(cols[i]))
            
            
            
            applicants_list = []
            # print(applicants)
            for a in applicants:
                address = self.p.interacteDB('select','address','id = \''+str(a['addressId'])+'\'')['result'][0]
                if a['emergencyContactId'] == '':
                    emergencyContact = {'name':'','phone':''}
                else:
                    emergencyContact = self.p.interacteDB('select','emergencyContact','id = \''+str(a['emergencyContactId'])+'\'')['result'][0]
                l = [a['id'],a['firstName'],a['lastName'],a['gender'],\
                a['dateOfBirth'],address['line1'],address['line2'],address['city'],address['state'],\
                address['zipCode'],a['email'],a['homePhone'],a['cellPhone'],a['payment'],\
                a['applicationDate'],a['reviewDate'],a['decisionId'],a['formsChecked'],\
                a['equipmentsChecked'], a['campId'],emergencyContact['name'],\
                emergencyContact['phone'],a['bunkhouseId'],a['tribeId']]
                applicants_list.append(l)

            for i, a in enumerate(applicants_list):
                for j,item in enumerate(a):
                    self.tableWidgetApplicantTable.setItem(i,j,QtGui.QTableWidgetItem(str(item)))
   
    def display(self):
        self.DialogUpdateApplicant = QtGui.QDialog()
        self.ui_update = Ui_DialogUpdateApplicant()
        self.ui_update.setupUi(self.DialogUpdateApplicant,self.p)
        selected = self.tableWidgetApplicantTable.selectedItems()
        cols = ['Id','First Name', 'Last Name','Gender','Date Of Birth','Line 1',\
            'Line 2','City','State','Zip Code','Email','Home Phone','Cell Phone',\
            'Payment','Application Date','Review Date','Decision Id','Forms Checked',\
            'Equipments Checked', 'Camp Id', 'Emergency Contact Name', \
            'Emergency Contact Phone','Bunkhouse Id','Tribe Id']
        self.ui_update.labelId.setText(selected[0].text())
        self.ui_update.lineFirstName.setText(selected[1].text())
        self.ui_update.lineLastName.setText(selected[2].text())
        self.ui_update.lineGender.setText(selected[3].text())
        dob_str = selected[4].text().split('-')
        self.ui_update.dateEditDOB.setDate(QtCore.QDate(int(dob_str[0]),int(dob_str[1]),int(dob_str[2])))
        self.ui_update.lineLine1.setText(selected[5].text())
        self.ui_update.lineLine2.setText(selected[6].text())
        self.ui_update.lineCity.setText(selected[7].text())
        self.ui_update.lineState.setText(selected[8].text())
        self.ui_update.lineZipCode.setText(selected[9].text())
        self.ui_update.lineEmail.setText(selected[10].text())
        self.ui_update.lineHomePhone.setText(selected[11].text())
        self.ui_update.lineCellPhone.setText(selected[12].text())
        
        if selected[13].text()=='1':
            self.ui_update.checkBoxPayment.setChecked(True)
        applicationDate = selected[14].text().split('-')
        self.ui_update.dateApplicationDate.setDate(QtCore.QDate(int(applicationDate[0]),int(applicationDate[1]),int(applicationDate[2])))
        reviewDate = selected[15].text().split('-')
        self.ui_update.dateReviewDate.setDate(QtCore.QDate(int(reviewDate[0]),int(reviewDate[1]),int(reviewDate[2])))
        self.ui_update.comboBoxAcceptanceDecision.setCurrentIndex(int(selected[16].text()))
        if selected[17].text()=='1':
            self.ui_update.checkBoxFormsCheck.setChecked(True)
        if selected[18].text()=='1':
            self.ui_update.checkBoxEquipmentsCheck.setChecked(True)
        if selected[19].text()!='':
            self.ui_update.comboBoxCamp.setCurrentIndex(int(selected[19].text()))
        self.ui_update.lineEmergencyName.setText(selected[20].text())
        self.ui_update.lineEmergencyPhone.setText(selected[21].text())
        if selected[22].text()!='':
            self.ui_update.comboBoxBunkhouse.setCurrentIndex(int(selected[22].text()))
        if selected[23].text()!='':
            self.ui_update.comboBoxTribe.setCurrentIndex(int(selected[23].text()))

        

        

        
        
        
        selectedRow = self.tableWidgetApplicantTable.selectedIndexes




        self.DialogUpdateApplicant.show()

    def retranslateUi(self, DialogLookUpApplicant):
        DialogLookUpApplicant.setWindowTitle(_translate("DialogLookUpApplicant", "Look Up Applicant", None))
        self.labelLastName.setText(_translate("DialogLookUpApplicant", "Last Name", None))
        self.labelFirstName.setText(_translate("DialogLookUpApplicant", "First Name", None))
        self.pushButtonUpdate.setText(_translate("DialogLookUpApplicant", "Update", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(0)
        item.setText(_translate("DialogLookUpApplicant", "Id", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(1)
        item.setText(_translate("DialogLookUpApplicant", "First Name", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(2)
        item.setText(_translate("DialogLookUpApplicant", "Last Name", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(3)
        item.setText(_translate("DialogLookUpApplicant", "Gender", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(4)
        item.setText(_translate("DialogLookUpApplicant", "Date Of Birth", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(5)
        item.setText(_translate("DialogLookUpApplicant", "Line 1", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(6)
        item.setText(_translate("DialogLookUpApplicant", "Line 2", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(7)
        item.setText(_translate("DialogLookUpApplicant", "City", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(8)
        item.setText(_translate("DialogLookUpApplicant", "State", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(9)
        item.setText(_translate("DialogLookUpApplicant", "Zip Code", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(10)
        item.setText(_translate("DialogLookUpApplicant", "Email", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(11)
        item.setText(_translate("DialogLookUpApplicant", "Home Phone", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(12)
        item.setText(_translate("DialogLookUpApplicant", "Cell Phone", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(13)
        item.setText(_translate("DialogLookUpApplicant", "Payment", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(14)
        item.setText(_translate("DialogLookUpApplicant", "Application Date", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(15)
        item.setText(_translate("DialogLookUpApplicant", "Review Date", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(16)
        item.setText(_translate("DialogLookUpApplicant", "Decision Id", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(17)
        item.setText(_translate("DialogLookUpApplicant", "Forms Checked", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(18)
        item.setText(_translate("DialogLookUpApplicant", "Equipments Checked", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(19)
        item.setText(_translate("DialogLookUpApplicant", "Camp Id", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(20)
        item.setText(_translate("DialogLookUpApplicant", "Emergency Contact Name", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(21)
        item.setText(_translate("DialogLookUpApplicant", "Emergency Contact Phone Number", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(22)
        item.setText(_translate("DialogLookUpApplicant", "Bunkhouse Id", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(23)
        item.setText(_translate("DialogLookUpApplicant", "Tribe Id", None))
        self.labelCamp.setText(_translate("DialogLookUpApplicant", "Camp", None))
        self.labelDOB.setText(_translate("DialogLookUpApplicant", "Date of Birth", None))
        self.pushButtonLookUp.setText(_translate("DialogLookUpApplicant", "Look Up", None))
        self.pushButton.setText(_translate("DialogLookUpApplicant", "Assign BK", None))
        self.pushButton_2.setText(_translate("DialogLookUpApplicant", "Assign Tribes", None))










class Ui_DialogLetterOfAcceptance(object):
    def setupUi(self, DialogLetterOfAcceptance):
        DialogLetterOfAcceptance.setObjectName(_fromUtf8("DialogLetterOfAcceptance"))
        DialogLetterOfAcceptance.resize(443, 348)
        self.textBrowserLetterOfAcceptance = QtGui.QTextBrowser(DialogLetterOfAcceptance)
        self.textBrowserLetterOfAcceptance.setGeometry(QtCore.QRect(40, 20, 371, 271))
        self.textBrowserLetterOfAcceptance.setObjectName(_fromUtf8("textBrowserLetterOfAcceptance"))
        self.pushButtonOkay = QtGui.QPushButton(DialogLetterOfAcceptance)
        self.pushButtonOkay.setGeometry(QtCore.QRect(190, 310, 75, 23))
        self.pushButtonOkay.setObjectName(_fromUtf8("pushButtonOkay"))

        self.retranslateUi(DialogLetterOfAcceptance)
        QtCore.QMetaObject.connectSlotsByName(DialogLetterOfAcceptance)

    def writeLetter(self, letter):
        self.textBrowserLetterOfAcceptance.setText(letter)

    def retranslateUi(self, DialogLetterOfAcceptance):
        DialogLetterOfAcceptance.setWindowTitle(_translate("DialogLetterOfAcceptance", "Notice", None))
        self.pushButtonOkay.setText(_translate("DialogLetterOfAcceptance", "Okay", None))


class Ui_DialogUpdateApplicant(object):
    def setupUi(self, DialogUpdateApplicant,p):
        DialogUpdateApplicant.setObjectName(_fromUtf8("DialogUpdateApplicant"))
        DialogUpdateApplicant.resize(1389, 1010)
        DialogUpdateApplicant.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        DialogUpdateApplicant.setAutoFillBackground(False)
        DialogUpdateApplicant.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(DialogUpdateApplicant)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(DialogUpdateApplicant)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelCamp = QtGui.QLabel(self.frame)
        self.labelCamp.setObjectName(_fromUtf8("labelCamp"))
        self.horizontalLayout.addWidget(self.labelCamp)
        self.comboBoxCamp = QtGui.QComboBox(self.frame)
        self.comboBoxCamp.setObjectName(_fromUtf8("comboBoxCamp"))
        self.horizontalLayout.addWidget(self.comboBoxCamp)
        self.labelCampAvilability = QtGui.QLabel(self.frame)
        self.labelCampAvilability.setObjectName(_fromUtf8("labelCampAvilability"))
        self.horizontalLayout.addWidget(self.labelCampAvilability)
        self.gridLayout.addWidget(self.frame, 6, 3, 1, 2)
        self.label_14 = QtGui.QLabel(DialogUpdateApplicant)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 13, 1, 1, 4)
        self.comboBoxTribe = QtGui.QComboBox(DialogUpdateApplicant)
        self.comboBoxTribe.setObjectName(_fromUtf8("comboBoxTribe"))
        self.gridLayout.addWidget(self.comboBoxTribe, 21, 4, 1, 1)
        self.labelFirstName = QtGui.QLabel(DialogUpdateApplicant)
        self.labelFirstName.setObjectName(_fromUtf8("labelFirstName"))
        self.gridLayout.addWidget(self.labelFirstName, 1, 1, 1, 1)
        self.lineFirstName = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineFirstName.setObjectName(_fromUtf8("lineFirstName"))
        self.gridLayout.addWidget(self.lineFirstName, 1, 2, 1, 1)
        self.comboBoxBunkhouse = QtGui.QComboBox(DialogUpdateApplicant)
        self.comboBoxBunkhouse.setObjectName(_fromUtf8("comboBoxBunkhouse"))
        self.gridLayout.addWidget(self.comboBoxBunkhouse, 21, 2, 1, 1)
        self.dateApplicationDate = QtGui.QDateEdit(DialogUpdateApplicant)
        self.dateApplicationDate.setDisplayFormat('yyyy/MM/dd')
        self.dateApplicationDate.setObjectName(_fromUtf8("dateApplicationDate"))
        self.gridLayout.addWidget(self.dateApplicationDate, 17, 2, 1, 1)
        self.labelPayment = QtGui.QLabel(DialogUpdateApplicant)
        self.labelPayment.setObjectName(_fromUtf8("labelPayment"))
        self.gridLayout.addWidget(self.labelPayment, 18, 1, 1, 1)
        self.checkBoxPayment = QtGui.QCheckBox(DialogUpdateApplicant)
        self.checkBoxPayment.setObjectName(_fromUtf8("checkBoxPayment"))
        self.gridLayout.addWidget(self.checkBoxPayment, 18, 2, 1, 1)
        self.labelLine2 = QtGui.QLabel(DialogUpdateApplicant)
        self.labelLine2.setObjectName(_fromUtf8("labelLine2"))
        self.gridLayout.addWidget(self.labelLine2, 9, 3, 1, 1)
        self.labelDOB = QtGui.QLabel(DialogUpdateApplicant)
        self.labelDOB.setObjectName(_fromUtf8("labelDOB"))
        self.gridLayout.addWidget(self.labelDOB, 2, 3, 1, 1)
        self.labelAcceptanceDecision = QtGui.QLabel(DialogUpdateApplicant)
        self.labelAcceptanceDecision.setObjectName(_fromUtf8("labelAcceptanceDecision"))
        self.gridLayout.addWidget(self.labelAcceptanceDecision, 18, 3, 1, 1)
        self.line = QtGui.QFrame(DialogUpdateApplicant)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 7, 1, 1, 4)
        self.labelEmergencyName = QtGui.QLabel(DialogUpdateApplicant)
        self.labelEmergencyName.setObjectName(_fromUtf8("labelEmergencyName"))
        self.gridLayout.addWidget(self.labelEmergencyName, 14, 1, 1, 1)
        self.dateReviewDate = QtGui.QDateEdit(DialogUpdateApplicant)
        self.dateReviewDate.setDisplayFormat('yyyy/MM/dd')
        self.dateReviewDate.setObjectName(_fromUtf8("dateReviewDate"))
        self.gridLayout.addWidget(self.dateReviewDate, 17, 4, 1, 1)
        self.labelReviewDate = QtGui.QLabel(DialogUpdateApplicant)
        self.labelReviewDate.setObjectName(_fromUtf8("labelReviewDate"))
        self.gridLayout.addWidget(self.labelReviewDate, 17, 3, 1, 1)
        self.labelBunkhouse = QtGui.QLabel(DialogUpdateApplicant)
        self.labelBunkhouse.setObjectName(_fromUtf8("labelBunkhouse"))
        self.gridLayout.addWidget(self.labelBunkhouse, 21, 1, 1, 1)
        self.labelApplicationDate = QtGui.QLabel(DialogUpdateApplicant)
        self.labelApplicationDate.setObjectName(_fromUtf8("labelApplicationDate"))
        self.gridLayout.addWidget(self.labelApplicationDate, 17, 1, 1, 1)
        self.lineEmergencyPhone = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineEmergencyPhone.setObjectName(_fromUtf8("lineEmergencyPhone"))
        self.gridLayout.addWidget(self.lineEmergencyPhone, 14, 4, 1, 1)
        self.labelLine1 = QtGui.QLabel(DialogUpdateApplicant)
        self.labelLine1.setObjectName(_fromUtf8("labelLine1"))
        self.gridLayout.addWidget(self.labelLine1, 9, 1, 1, 1)
        self.labelEquipmentsCheck = QtGui.QLabel(DialogUpdateApplicant)
        self.labelEquipmentsCheck.setObjectName(_fromUtf8("labelEquipmentsCheck"))
        self.gridLayout.addWidget(self.labelEquipmentsCheck, 19, 3, 1, 1)
        self.lineCity = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineCity.setObjectName(_fromUtf8("lineCity"))
        self.gridLayout.addWidget(self.lineCity, 10, 2, 1, 1)
        self.labelEmergencyPhone = QtGui.QLabel(DialogUpdateApplicant)
        self.labelEmergencyPhone.setObjectName(_fromUtf8("labelEmergencyPhone"))
        self.gridLayout.addWidget(self.labelEmergencyPhone, 14, 3, 1, 1)
        self.lineState = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineState.setObjectName(_fromUtf8("lineState"))
        self.gridLayout.addWidget(self.lineState, 10, 4, 1, 1)
        self.lineEmergencyName = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineEmergencyName.setObjectName(_fromUtf8("lineEmergencyName"))
        self.gridLayout.addWidget(self.lineEmergencyName, 14, 2, 1, 1)
        self.lineLine2 = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineLine2.setObjectName(_fromUtf8("lineLine2"))
        self.gridLayout.addWidget(self.lineLine2, 9, 4, 1, 1)
        self.checkBoxFormsCheck = QtGui.QCheckBox(DialogUpdateApplicant)
        self.checkBoxFormsCheck.setObjectName(_fromUtf8("checkBoxFormsCheck"))
        self.gridLayout.addWidget(self.checkBoxFormsCheck, 19, 2, 1, 1)
        self.labelZipCode = QtGui.QLabel(DialogUpdateApplicant)
        self.labelZipCode.setObjectName(_fromUtf8("labelZipCode"))
        self.gridLayout.addWidget(self.labelZipCode, 11, 1, 1, 1)
        self.lineLine1 = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineLine1.setObjectName(_fromUtf8("lineLine1"))
        self.gridLayout.addWidget(self.lineLine1, 9, 2, 1, 1)
        self.checkBoxEquipmentsCheck = QtGui.QCheckBox(DialogUpdateApplicant)
        self.checkBoxEquipmentsCheck.setObjectName(_fromUtf8("checkBoxEquipmentsCheck"))
        self.gridLayout.addWidget(self.checkBoxEquipmentsCheck, 19, 4, 1, 1)
        self.labelFormsCheck = QtGui.QLabel(DialogUpdateApplicant)
        self.labelFormsCheck.setObjectName(_fromUtf8("labelFormsCheck"))
        self.gridLayout.addWidget(self.labelFormsCheck, 19, 1, 1, 1)
        self.label_17 = QtGui.QLabel(DialogUpdateApplicant)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 16, 1, 1, 1)
        self.comboBoxAcceptanceDecision = QtGui.QComboBox(DialogUpdateApplicant)
        self.comboBoxAcceptanceDecision.setObjectName(_fromUtf8("comboBoxAcceptanceDecision"))
        self.gridLayout.addWidget(self.comboBoxAcceptanceDecision, 18, 4, 1, 1)
        self.labelHomePhone = QtGui.QLabel(DialogUpdateApplicant)
        self.labelHomePhone.setObjectName(_fromUtf8("labelHomePhone"))
        self.gridLayout.addWidget(self.labelHomePhone, 5, 3, 1, 1)
        self.labelTribe = QtGui.QLabel(DialogUpdateApplicant)
        self.labelTribe.setObjectName(_fromUtf8("labelTribe"))
        self.gridLayout.addWidget(self.labelTribe, 21, 3, 1, 1)
        self.lineCellPhone = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineCellPhone.setObjectName(_fromUtf8("lineCellPhone"))
        self.gridLayout.addWidget(self.lineCellPhone, 6, 2, 1, 1)
        self.lineZipCode = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineZipCode.setObjectName(_fromUtf8("lineZipCode"))
        self.gridLayout.addWidget(self.lineZipCode, 11, 2, 1, 1)
        self.dateEditDOB = QtGui.QDateEdit(DialogUpdateApplicant)
        self.dateEditDOB.setObjectName(_fromUtf8("dateEditDOB"))
        self.dateEditDOB.setDisplayFormat('yyyy/MM/dd')
        self.gridLayout.addWidget(self.dateEditDOB, 2, 4, 1, 1)
        self.line_3 = QtGui.QFrame(DialogUpdateApplicant)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 15, 1, 1, 4)
        self.labelEmail = QtGui.QLabel(DialogUpdateApplicant)
        self.labelEmail.setObjectName(_fromUtf8("labelEmail"))
        self.gridLayout.addWidget(self.labelEmail, 5, 1, 1, 1)
        self.labelLastName = QtGui.QLabel(DialogUpdateApplicant)
        self.labelLastName.setObjectName(_fromUtf8("labelLastName"))
        self.gridLayout.addWidget(self.labelLastName, 1, 3, 1, 1)
        self.lineHomePhone = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineHomePhone.setObjectName(_fromUtf8("lineHomePhone"))
        self.gridLayout.addWidget(self.lineHomePhone, 5, 4, 1, 1)
        self.labelGender = QtGui.QLabel(DialogUpdateApplicant)
        self.labelGender.setObjectName(_fromUtf8("labelGender"))
        self.gridLayout.addWidget(self.labelGender, 2, 1, 1, 1)
        self.lineGender = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineGender.setObjectName(_fromUtf8("lineGender"))
        self.gridLayout.addWidget(self.lineGender, 2, 2, 1, 1)
        self.lineLastName = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineLastName.setObjectName(_fromUtf8("lineLastName"))
        self.gridLayout.addWidget(self.lineLastName, 1, 4, 1, 1)
        self.lineEmail = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineEmail.setObjectName(_fromUtf8("lineEmail"))
        self.gridLayout.addWidget(self.lineEmail, 5, 2, 1, 1)
        self.labelCity = QtGui.QLabel(DialogUpdateApplicant)
        self.labelCity.setObjectName(_fromUtf8("labelCity"))
        self.gridLayout.addWidget(self.labelCity, 10, 1, 1, 1)
        self.line_2 = QtGui.QFrame(DialogUpdateApplicant)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 12, 1, 1, 4)
        self.labelState = QtGui.QLabel(DialogUpdateApplicant)
        self.labelState.setObjectName(_fromUtf8("labelState"))
        self.gridLayout.addWidget(self.labelState, 10, 3, 1, 1)
        self.labelCellPhone = QtGui.QLabel(DialogUpdateApplicant)
        self.labelCellPhone.setObjectName(_fromUtf8("labelCellPhone"))
        self.gridLayout.addWidget(self.labelCellPhone, 6, 1, 1, 1)
        self.label_5 = QtGui.QLabel(DialogUpdateApplicant)
        self.label_5.setMinimumSize(QtCore.QSize(90, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 8, 1, 1, 1)
        self.widget = QtGui.QWidget(DialogUpdateApplicant)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 8, 2, 1, 2)
        self.frame_2 = QtGui.QFrame(DialogUpdateApplicant)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButtonSubmit = QtGui.QPushButton(self.frame_2)
        self.pushButtonSubmit.setGeometry(QtCore.QRect(1050, 30, 281, 40))
        self.pushButtonSubmit.setObjectName(_fromUtf8("pushButtonSubmit"))
        self.pushButtonCheckList = QtGui.QPushButton(self.frame_2)
        self.pushButtonCheckList.setGeometry(QtCore.QRect(820, 30, 211, 40))
        self.pushButtonCheckList.setObjectName(_fromUtf8("pushButtonCheckList"))

        self.pushButtonCancellation = QtGui.QPushButton(self.frame_2)
        self.pushButtonCancellation.setGeometry(QtCore.QRect(600, 30, 211, 40))
        self.pushButtonCancellation.setObjectName(_fromUtf8("pushButtonCancellation"))

        self.pushButtonPreference = QtGui.QPushButton(self.frame_2)
        self.pushButtonPreference.setGeometry(QtCore.QRect(0, 29, 171, 41))
        self.pushButtonPreference.setObjectName(_fromUtf8("pushButtonPreference"))

        self.pushButtonPreference_2 = QtGui.QPushButton(self.frame_2)
        self.pushButtonPreference_2.setGeometry(QtCore.QRect(190, 30, 171, 41))
        self.pushButtonPreference_2.setObjectName(_fromUtf8("pushButtonPreference_2"))
        
        self.gridLayout.addWidget(self.frame_2, 22, 1, 1, 4)
        self.label_18 = QtGui.QLabel(DialogUpdateApplicant)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 0, 1, 1, 1)


        self.labelWarningMsg = QtGui.QLabel(DialogUpdateApplicant)
        self.labelWarningMsg.setObjectName(_fromUtf8("labelWarningMsg"))
        self.labelWarningMsg.setStyleSheet("color:red")
        self.gridLayout.addWidget(self.labelWarningMsg, 0, 3, 1, 2)




        self.labelId = QtGui.QLabel(DialogUpdateApplicant)
        self.labelId.setText(_fromUtf8(""))
        self.labelId.setObjectName(_fromUtf8("labelId"))
        self.gridLayout.addWidget(self.labelId, 0, 2, 1, 1)
        self.p = p
        self.comboBoxCamp.addItem('')
        self.comboBoxBunkhouse.addItem('')
        self.comboBoxTribe.addItem('')
        self.comboBoxAcceptanceDecision.addItem('')
        self.comboBoxCamp.addItems([str(x.name) for x in self.p.camps])
        self.comboBoxBunkhouse.addItems([str(x.name) for x in self.p.bunkhouses])
        self.comboBoxTribe.addItems([str(x.name) for x in self.p.tribes])
        self.comboBoxAcceptanceDecision.addItems(['1-Accept','2-Conditional Accept', '3-Denial','4-Canceled'])
        
        # click submit button
        self.pushButtonSubmit.clicked.connect(lambda:self.submitDataToDB(DialogUpdateApplicant))
        self.pushButtonCheckList.clicked.connect(lambda:self.generateCheckList(DialogUpdateApplicant))
        self.pushButtonCancellation.clicked.connect(lambda:self.generateCancellationForm(DialogUpdateApplicant))
        self.pushButtonPreference.clicked.connect(lambda:self.showPreferenceForm(DialogUpdateApplicant,self.p,'bkpreference'))
        self.pushButtonPreference_2.clicked.connect(lambda:self.showPreferenceForm(DialogUpdateApplicant,self.p,'tribepreference'))
        
        # value changes
        self.comboBoxCamp.currentIndexChanged.connect(lambda:self.showCampAvilability())

        # self.dateEditDOB = QtGui.QDateEdit(DialogUpdateApplicant)
        # self.dateEditDOB.setObjectName(_fromUtf8("dateEditDOB"))
        # self.dateEditDOB.setDate(QtCore.QDate(1800,1,1))

        
        
        self.retranslateUi(DialogUpdateApplicant)
        QtCore.QMetaObject.connectSlotsByName(DialogUpdateApplicant)
        DialogUpdateApplicant.setTabOrder(self.lineFirstName, self.lineLastName)
        DialogUpdateApplicant.setTabOrder(self.lineLastName, self.lineGender)
        DialogUpdateApplicant.setTabOrder(self.lineGender, self.dateEditDOB)
        DialogUpdateApplicant.setTabOrder(self.dateEditDOB, self.lineEmail)
        DialogUpdateApplicant.setTabOrder(self.lineEmail, self.lineHomePhone)
        DialogUpdateApplicant.setTabOrder(self.lineHomePhone, self.lineCellPhone)
        DialogUpdateApplicant.setTabOrder(self.lineCellPhone, self.comboBoxCamp)
        DialogUpdateApplicant.setTabOrder(self.comboBoxCamp, self.lineLine1)
        DialogUpdateApplicant.setTabOrder(self.lineLine1, self.lineLine2)
        DialogUpdateApplicant.setTabOrder(self.lineLine2, self.lineCity)
        DialogUpdateApplicant.setTabOrder(self.lineCity, self.lineState)
        DialogUpdateApplicant.setTabOrder(self.lineState, self.lineZipCode)
        DialogUpdateApplicant.setTabOrder(self.lineZipCode, self.lineEmergencyName)
        DialogUpdateApplicant.setTabOrder(self.lineEmergencyName, self.lineEmergencyPhone)
        DialogUpdateApplicant.setTabOrder(self.lineEmergencyPhone, self.dateApplicationDate)
        DialogUpdateApplicant.setTabOrder(self.dateApplicationDate, self.dateReviewDate)
        DialogUpdateApplicant.setTabOrder(self.dateReviewDate, self.checkBoxPayment)
        DialogUpdateApplicant.setTabOrder(self.checkBoxPayment, self.comboBoxAcceptanceDecision)
        DialogUpdateApplicant.setTabOrder(self.comboBoxAcceptanceDecision, self.checkBoxFormsCheck)
        DialogUpdateApplicant.setTabOrder(self.checkBoxFormsCheck, self.checkBoxEquipmentsCheck)
        DialogUpdateApplicant.setTabOrder(self.checkBoxEquipmentsCheck, self.comboBoxBunkhouse)
        DialogUpdateApplicant.setTabOrder(self.comboBoxBunkhouse, self.comboBoxTribe)
        DialogUpdateApplicant.setTabOrder(self.comboBoxTribe, self.pushButtonCheckList)
        DialogUpdateApplicant.setTabOrder(self.pushButtonCheckList, self.pushButtonSubmit)


    def checkBlankCells(self):
        if self.lineFirstName.text()=='' or self.lineGender.text()==''\
        or self.lineLastName.text()=='' or self.dateEditDOB.date().toPyDate()==datetime.date(1800,1,1)\
        or self.lineEmail.text()=='' or self.lineHomePhone.text()=='' or self.lineCellPhone.text()==''\
        or self.comboBoxCamp.currentIndex==0 or self.lineLine1.text()=='' or self.lineCity.text()==''\
        or self.lineState.text()=='' or self.lineZipCode.text()=='':
            return True
        else:
            return False
        

    def showCampAvilability(self):
        campId = self.comboBoxCamp.currentIndex()
        if campId ==0:
            return
        else:
            boys = self.p.interacteDB('select','applicant','campId = \''+str(campId)+\
        '\' and gender = \''+'M'+ '\' and decisionId != \'3\' ')
            girls = self.p.interacteDB('select','applicant','campId = \''+str(campId)+\
        '\' and gender = \''+'F'+ '\' and decisionId != \'3\' ')
        self.labelCampAvilability.setText('M: ' + str(self.p.camps[campId-1].totalBoyNumber - len(boys['result']))+', F:'+str(self.p.camps[campId-1].totalGrilNumber -len(girls['result'])))
        

    def generateCheckList(self,DialogUpdateApplicant):
        cl_form = self.p.generateCheckList('form')
        cl_equipment = self.p.generateCheckList('equipment')
        cl = 'Forms:\n'+cl_form + '\n'+'Equipments:\n'+cl_equipment

        self.DialogLetterOfAcceptance = QtGui.QDialog()
        ui = Ui_DialogLetterOfAcceptance()
        ui.setupUi(self.DialogLetterOfAcceptance)
        ui.writeLetter(cl)
        
        self.DialogLetterOfAcceptance.show()


    def generateCancellationForm(self,DialogUpdateApplicant):

        self.comboBoxAcceptanceDecision.setCurrentIndex(4)

        self.DialogCancellation = QtGui.QDialog()
        self.ui_cancellation = Ui_DialogCancellation()
        self.ui_cancellation.setupUi(self.DialogCancellation,self.dateReviewDate.date().toPyDate())
        
        self.DialogCancellation.show()
    
    def showPreferenceForm(self,DialogUpdateApplicant, p,type):
        self.DialogPreference = QtGui.QDialog()
        self.ui_preference = Ui_DialogPreference()
        self.ui_preference.setupUi(self.DialogPreference,int(self.labelId.text()),self.comboBoxCamp.currentIndex(),p,type)
        

        self.DialogPreference.show()
        
    def submitDataToDB(self,DialogUpdateApplicant):
        id = self.labelId.text()
        firstName = self.lineFirstName.text()
        lastName = self.lineLastName.text()
        gender = self.lineGender.text()
        dateOfBirth =self.dateEditDOB.date().toPyDate()
        
        email = self.lineEmail.text()
        homePhone = self.lineHomePhone.text()
        cellPhone = self.lineCellPhone.text()
        campId = self.comboBoxCamp.currentIndex()
        line1 = self.lineLine1.text()
        line2 = self.lineLine2.text()
        city = self.lineCity.text()
        state = self.lineState.text()
        zipCode = self.lineZipCode.text()
        emergencyContactName = self.lineEmergencyName.text()
        emergencyContactPhone = self.lineEmergencyPhone.text()
        applicationDate = self.dateApplicationDate.date().toPyDate()
        age =applicationDate.year - dateOfBirth.year
        reviewDate = self.dateReviewDate.date().toPyDate()
        payment = 1 if self.checkBoxPayment.isChecked() else 0
        decisionId = self.comboBoxAcceptanceDecision.currentIndex()
        formsChecked = 1 if self.checkBoxFormsCheck.isChecked() else 0
        equipmentsChecked = 1 if self.checkBoxEquipmentsCheck.isChecked() else 0
        bunkhouseId = self.comboBoxBunkhouse.currentIndex()
        tribeId = self.comboBoxTribe.currentIndex()

        a = Applicant(firstName = firstName,lastName = lastName,age = age,gender = gender,\
        dateOfBirth = dateOfBirth,email = email, homePhone = homePhone, cellPhone = cellPhone,\
        emergencyContactPhone = emergencyContactPhone,emergencyContactName = emergencyContactName,\
        line1 = line1,line2 = line2,city = city,state = state,zipCode = zipCode,payment = payment,
        applicationDate = applicationDate,
        reviewDate = reviewDate,decisionId = decisionId,formsChecked = formsChecked,\
        equipmentsChecked = equipmentsChecked,campId = campId,bunkhouseId = bunkhouseId,\
        tribeId = tribeId)
        validationRes = self.p.validateApplicant(campId,gender,age)



        if self.checkBlankCells():
            
            # QtGui.QMessageBox.warning(DialogAddNewApplicant,"Invalid Inputs",
            # "The fileds with * cannot be empty.", QtGui.QMessageBox.Cancel,
            # QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
            self.labelWarningMsg.clear()
            self.labelWarningMsg.setText("The fileds with * cannot be empty")
            
        elif self.comboBoxAcceptanceDecision.currentIndex() == 1 and not validationRes['ok']:
            
            # QtGui.QMessageBox.warning(DialogAddNewApplicant,"Application cannot be accepted",
            # "This application cannot be accepted due to {}".format(validationRes['msg']), QtGui.QMessageBox.Cancel,
            # QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
            self.labelWarningMsg.clear()
            self.labelWarningMsg.setText("This application cannot be accepted due to {}".format(validationRes['msg']))
        
        elif self.comboBoxAcceptanceDecision.currentIndex() == 1 and not self.checkBoxPayment.isChecked():
            # QtGui.QMessageBox.warning(DialogAddNewApplicant,"Application cannot be accepted",
            # "This application cannot be accepted since the payment check has not been recieve", QtGui.QMessageBox.Cancel,
            # QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
            self.labelWarningMsg.clear()
            self.labelWarningMsg.setText("This application cannot be accepted since the payment check has not been recieve")

        else:
            res = self.p.addNewApplicant(a)
            # QtGui.QMessageBox.warning(DialogAddNewApplicant,"Success",
            # res['result']['msg'], QtGui.QMessageBox.Ok,
            # QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
            self.labelWarningMsg.clear()
            self.labelWarningMsg.setText("Success! {}".format(validationRes['msg']))
        
            DialogUpdateApplicant.accept()

            

            # popup window
        





    def retranslateUi(self, DialogUpdateApplicant):
        DialogUpdateApplicant.setWindowTitle(_translate("DialogUpdateApplicant", "Update Applicant", None))
        self.labelCamp.setText(_translate("DialogUpdateApplicant", "Camp Interested", None))
        self.labelCampAvilability.setText(_translate("DialogUpdateApplicant", "", None))
        self.label_14.setText(_translate("DialogUpdateApplicant", "Emergency Contact:", None))
        self.labelFirstName.setText(_translate("DialogUpdateApplicant", "First Name", None))
        self.labelPayment.setText(_translate("DialogUpdateApplicant", "Payment", None))
        self.checkBoxPayment.setText(_translate("DialogUpdateApplicant", "Check Recieved?", None))
        self.labelLine2.setText(_translate("DialogUpdateApplicant", "Line 2", None))
        self.labelDOB.setText(_translate("DialogUpdateApplicant", "Date of Birth", None))
        self.labelAcceptanceDecision.setText(_translate("DialogUpdateApplicant", "Accepted?", None))
        self.labelEmergencyName.setText(_translate("DialogUpdateApplicant", "Name", None))
        self.labelReviewDate.setText(_translate("DialogUpdateApplicant", "Review Date", None))
        self.labelBunkhouse.setText(_translate("DialogUpdateApplicant", "Bunkhouse", None))
        self.labelApplicationDate.setText(_translate("DialogUpdateApplicant", "Application Date", None))
        self.labelLine1.setText(_translate("DialogUpdateApplicant", "Line 1", None))
        self.labelEquipmentsCheck.setText(_translate("DialogUpdateApplicant", "Equipments", None))
        self.labelEmergencyPhone.setText(_translate("DialogUpdateApplicant", "Phone", None))
        self.checkBoxFormsCheck.setText(_translate("DialogUpdateApplicant", "Camper has all required forms?", None))
        self.labelZipCode.setText(_translate("DialogUpdateApplicant", "ZipCode", None))
        self.checkBoxEquipmentsCheck.setText(_translate("DialogUpdateApplicant", "Camper has all required equipments?", None))
        self.labelFormsCheck.setText(_translate("DialogUpdateApplicant", "Forms", None))
        self.label_17.setText(_translate("DialogUpdateApplicant", "Admin:", None))
        self.labelHomePhone.setText(_translate("DialogUpdateApplicant", "Home Phone", None))
        self.labelTribe.setText(_translate("DialogUpdateApplicant", "Tribe", None))
        self.labelEmail.setText(_translate("DialogUpdateApplicant", "Email:", None))
        self.labelLastName.setText(_translate("DialogUpdateApplicant", "Last Name", None))
        self.labelGender.setText(_translate("DialogUpdateApplicant", "Gender", None))
        self.labelCity.setText(_translate("DialogUpdateApplicant", "City", None))
        self.labelState.setText(_translate("DialogUpdateApplicant", "State", None))
        self.labelCellPhone.setText(_translate("DialogUpdateApplicant", "Cell Phone", None))
        self.label_5.setText(_translate("DialogUpdateApplicant", "Address:", None))
        self.pushButtonSubmit.setText(_translate("DialogUpdateApplicant", "Submit", None))
        self.pushButtonCheckList.setText(_translate("DialogUpdateApplicant", "Checkin Checklist", None))
        self.pushButtonCancellation.setText(_translate("DialogUpdateApplicant", "Cancellation Request", None))
        self.label_18.setText(_translate("DialogUpdateApplicant", "Applicant Basic Information:", None))
        self.pushButtonPreference.setText(_translate("DialogUpdateApplicant", "BK Preference", None))
        self.pushButtonPreference_2.setText(_translate("DialogUpdateApplicant", "Tribe Preference", None))

        



class Ui_DialogPreference(object):
    def setupUi(self, DialogPreference,applicantId,campId,p,ptype):
        DialogPreference.setObjectName(_fromUtf8("DialogPreference"))
        DialogPreference.resize(733, 665)
        self.textEdit = QtGui.QTextEdit(DialogPreference)
        self.textEdit.setGeometry(QtCore.QRect(80, 130, 221, 381))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(DialogPreference)
        self.textEdit_2.setGeometry(QtCore.QRect(420, 130, 221, 381))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label = QtGui.QLabel(DialogPreference)
        self.label.setGeometry(QtCore.QRect(80, 70, 221, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DialogPreference)
        self.label_2.setGeometry(QtCore.QRect(420, 70, 221, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(DialogPreference)
        self.pushButton.setGeometry(QtCore.QRect(290, 580, 131, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.applicantId = applicantId
        self.campId = campId
        self.pushButton.clicked.connect(lambda:self.submit(DialogPreference,applicantId,campId,ptype))
        self.p = p


        res = self.p.interacteDB('select',ptype,'applicantId={} and campId={}'.format(applicantId,campId))
        res = res['result']
        stay = [str(x['stay']) for x in res if x['stay']!='']
        reject = [str(x['reject']) for x in res if x['reject']!='']
        
        stay = '\n'.join(stay)
        reject = '\n'.join(reject)
        self.textEdit.setText(stay)
        self.textEdit_2.setText(reject)

        self.retranslateUi(DialogPreference)
        QtCore.QMetaObject.connectSlotsByName(DialogPreference)



    def submit(self,DialogPreference,applicantId,campId,ptype):
        stay = self.textEdit.toPlainText()
        reject = self.textEdit_2.toPlainText()
        if stay =='' and reject =='':
            self.p.interacteDB('delete',ptype,{'applicantId':applicantId})
            DialogPreference.accept()
        elif stay !='' and reject =='':
            try:
                stay_list = stay.split('\n')
                stay_list = [int(x) for x in stay_list if x != '']
                dbData = [{'applicantId':str(applicantId),'campId':str(campId),'stay':str(x),'reject':''} for x in stay_list]
                self.p.interacteDB('delete',ptype,{'applicantId':applicantId})
                self.p.interacteDB('insert',ptype,dbData)
                DialogPreference.accept()
                
            except:
                pass
        elif stay =='' and reject !='':
            try:
                reject_list = reject.split('\n')
                reject_list = [int(x) for x in reject_list if x != '']
                dbData = [{'applicantId':str(applicantId),'campId':str(campId),'stay':'','reject':str(x)} for x in reject_list]
                self.p.interacteDB('delete',ptype,{'applicantId':applicantId})
                self.p.interacteDB('insert',ptype,dbData)
                DialogPreference.accept()
            except:
                pass
        elif stay !='' and reject !='':
            # try:
            stay_list = stay.split('\n')
            stay_list = [int(x) for x in stay_list if x != '']
            dbData = [{'applicantId':str(applicantId),'campId':str(campId),'stay':str(x),'reject':''} for x in stay_list]
            self.p.interacteDB('delete',ptype,{'applicantId':applicantId})
            self.p.interacteDB('insert',ptype,dbData)
            reject_list = reject.split('\n')
            reject_list = [int(x) for x in reject_list if x != '']
            dbData = [{'applicantId':str(applicantId),'campId':str(campId),'stay':'','reject':str(x)} for x in reject_list]
            self.p.interacteDB('insert',ptype,dbData)
            DialogPreference.accept()
            
            
            # except:
            #     pass        
            




    def retranslateUi(self, DialogPreference):
        DialogPreference.setWindowTitle(_translate("DialogPreference", "Preference", None))
        self.label.setText(_translate("DialogPreference", "Have to Stay with:", None))
        self.label_2.setText(_translate("DialogPreference", "Cannot Stay with:", None))
        self.pushButton.setText(_translate("DialogPreference", "Submit", None))


        


class Ui_DialogCancellation(object):
    def setupUi(self, Ui_DialogCancellation,review_date):
        Ui_DialogCancellation.setObjectName(_fromUtf8("Ui_DialogCancellation"))
        Ui_DialogCancellation.resize(621, 601)
        self.label = QtGui.QLabel(Ui_DialogCancellation)
        self.label.setGeometry(QtCore.QRect(60, 40, 221, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.dateEditCancellation = QtGui.QDateEdit(Ui_DialogCancellation)
        self.dateEditCancellation.setGeometry(QtCore.QRect(340, 40, 121, 21))
        self.dateEditCancellation.setObjectName(_fromUtf8("dateEditCancellation"))
        self.dateEditCancellation.setDate(QtCore.QDate(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day))
        self.dateEditCancellation.setDisplayFormat('yyyy/MM/dd')
        self.textEditCancellationLetter = QtGui.QTextEdit(Ui_DialogCancellation)
        self.textEditCancellationLetter.setGeometry(QtCore.QRect(30, 110, 561, 421))
        self.textEditCancellationLetter.setObjectName(_fromUtf8("textEditCancellationLetter"))
        # self.pushButtonSubmit = QtGui.QPushButton(Ui_DialogCancellation)
        # self.pushButtonSubmit.setGeometry(QtCore.QRect(240, 550, 131, 40))
        # self.pushButtonSubmit.setObjectName(_fromUtf8("pushButtonSubmit"))

        # self.pushButtonCalculate = QtGui.QPushButton(Ui_DialogCancellation)
        # self.pushButtonCalculate.setGeometry(QtCore.QRect(60, 60, 221, 21))
        # self.pushButtonCalculate.setObjectName(_fromUtf8("textEditCancellationLetter"))



        self.review_date = review_date

        self.calculateRefund()
        self.dateEditCancellation.dateChanged.connect(lambda: self.calculateRefund())
        self.deposit=1000

        self.retranslateUi(Ui_DialogCancellation)
        QtCore.QMetaObject.connectSlotsByName(Ui_DialogCancellation)
    
    def calculateRefund(self):
        res = ''
        time = self.dateEditCancellation.date().toPyDate() - self.review_date
        if time.days<0:
            res += 'Cancellation request date cannot be earlier than review date'
        elif 0 <= time.days <= 21:
            res += 'Welcome to Gila Breath Camp!'
            res += 'You have a 90% refund of payment $' + str(self.deposit * 0.9) + '.\n'
            res += 'Because your cancellation date is within 3 weeks of review date,{}.'.format(str(self.review_date))
        elif 21 < time.days <= 42:
            res += 'Welcome to Gila Breath Camp!'
            res += 'You have a 45% refund of payment $' + str(self.deposit * 0.45) + '.\n'
            res += 'Because your cancellation date is within 6 weeks of review date,{}.'.format(str(self.review_date))
        else:
            res += 'Welcome to Gila Breath Camp!'
            res += 'You have a NO refund of payment '+ '.\n'
            res += 'Because your cancellation date exceeds 6 weeks of review date,{}.'.format(str(self.review_date))
        
        self.textEditCancellationLetter.setText(res)
    
            
            
        


    def retranslateUi(self, Ui_DialogCancellation):
        Ui_DialogCancellation.setWindowTitle(_translate("Ui_DialogCancellation", "Ui_DialogCancellation", None))
        self.label.setText(_translate("Ui_DialogCancellation", "Cancellation Date:", None))
        # self.pushButtonSubmit.setText(_translate("Ui_DialogCancellation", "Submit", None))



