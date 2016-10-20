# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'campReg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

from processor import *

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,p):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(830, 462)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 120, 471, 151))
        self.label.setStyleSheet(_fromUtf8("font: 75 20pt \"Kristen ITC\";"))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 36))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_New = QtGui.QAction(MainWindow)
        self.actionAdd_New.setObjectName(_fromUtf8("actionAdd_New"))
        ## trigger add new
        self.actionAdd_New.triggered.connect(self.showNewApplicantDialog)
        self.actionLook_Up = QtGui.QAction(MainWindow)
        self.actionLook_Up.setObjectName(_fromUtf8("actionLook_Up"))
        ## trigger add look up
        self.actionLook_Up.triggered.connect(self.showLookUpApplicant)
        self.menuFile.addAction(self.actionAdd_New)
        self.menuFile.addAction(self.actionLook_Up)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.p = p

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.CustomizeWindowHint)




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Main", None))
        self.label.setText(_translate("MainWindow", "Gila Breath Camp", None))
        self.menuFile.setTitle(_translate("MainWindow", "Applicant", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionAdd_New.setText(_translate("MainWindow", "Add New Applicant", None))
        self.actionLook_Up.setText(_translate("MainWindow", "Look Up", None))

    def showNewApplicantDialog(self):
        self.DialogAddNewApplicant = QtGui.QDialog()
        ui = Ui_DialogAddNewApplicant()
        ui.setupUi(self.DialogAddNewApplicant,self.p)
        self.DialogAddNewApplicant.show()
    
    def showLookUpApplicant(self):
        self.DialogLookUpApplicant = QtGui.QDialog()
        ui = Ui_DialogLookUpApplicant()
        ui.setupUi(self.DialogLookUpApplicant,self.p)
        self.DialogLookUpApplicant.show()

















class Ui_DialogAddNewApplicant(object):
    def setupUi(self, DialogAddNewApplicant, p):
        DialogAddNewApplicant.setObjectName(_fromUtf8("DialogAddNewApplicant"))
        DialogAddNewApplicant.resize(1297, 1010)
        DialogAddNewApplicant.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        DialogAddNewApplicant.setAutoFillBackground(False)
        DialogAddNewApplicant.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(DialogAddNewApplicant)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelGender = QtGui.QLabel(DialogAddNewApplicant)
        self.labelGender.setObjectName(_fromUtf8("labelGender"))
        self.gridLayout.addWidget(self.labelGender, 1, 3, 1, 1)
        self.lineGender = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineGender.setObjectName(_fromUtf8("lineGender"))
        self.gridLayout.addWidget(self.lineGender, 1, 4, 1, 1)
        self.dateApplicationDate = QtGui.QDateEdit(DialogAddNewApplicant)
        self.dateApplicationDate.setObjectName(_fromUtf8("dateApplicationDate"))
        self.dateApplicationDate.setDate(QtCore.QDate(1800,1,1))
        self.gridLayout.addWidget(self.dateApplicationDate, 16, 2, 1, 1)
        self.labelLastName = QtGui.QLabel(DialogAddNewApplicant)
        self.labelLastName.setObjectName(_fromUtf8("labelLastName"))
        self.gridLayout.addWidget(self.labelLastName, 2, 1, 1, 1)
        self.label_18 = QtGui.QLabel(DialogAddNewApplicant)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 0, 1, 1, 2)
        self.labelFirstName = QtGui.QLabel(DialogAddNewApplicant)
        self.labelFirstName.setObjectName(_fromUtf8("labelFirstName"))
        self.gridLayout.addWidget(self.labelFirstName, 1, 1, 1, 1)
        self.labelApplicationDate = QtGui.QLabel(DialogAddNewApplicant)
        self.labelApplicationDate.setObjectName(_fromUtf8("labelApplicationDate"))
        self.gridLayout.addWidget(self.labelApplicationDate, 16, 1, 1, 1)
        self.lineLastName = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineLastName.setObjectName(_fromUtf8("lineLastName"))
        self.gridLayout.addWidget(self.lineLastName, 2, 2, 1, 1)
        self.labelDOB = QtGui.QLabel(DialogAddNewApplicant)
        self.labelDOB.setObjectName(_fromUtf8("labelDOB"))
        self.gridLayout.addWidget(self.labelDOB, 2, 3, 1, 1)
        self.lineFirstName = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineFirstName.setObjectName(_fromUtf8("lineFirstName"))
        self.gridLayout.addWidget(self.lineFirstName, 1, 2, 1, 1)
        self.dateReviewDate = QtGui.QDateEdit(DialogAddNewApplicant)
        self.dateReviewDate.setObjectName(_fromUtf8("dateReviewDate"))
        self.dateReviewDate.setDate(QtCore.QDate(1800,1,1))
        self.gridLayout.addWidget(self.dateReviewDate, 16, 4, 1, 1)
        self.comboBoxBunkhouse = QtGui.QComboBox(DialogAddNewApplicant)
        self.comboBoxBunkhouse.setObjectName(_fromUtf8("comboBoxBunkhouse"))
        self.gridLayout.addWidget(self.comboBoxBunkhouse, 20, 2, 1, 1)
        self.labelReviewDate = QtGui.QLabel(DialogAddNewApplicant)
        self.labelReviewDate.setObjectName(_fromUtf8("labelReviewDate"))
        self.gridLayout.addWidget(self.labelReviewDate, 16, 3, 1, 1)
        self.labelAcceptanceDecision = QtGui.QLabel(DialogAddNewApplicant)
        self.labelAcceptanceDecision.setObjectName(_fromUtf8("labelAcceptanceDecision"))
        self.gridLayout.addWidget(self.labelAcceptanceDecision, 17, 3, 1, 1)
        self.comboBoxTribe = QtGui.QComboBox(DialogAddNewApplicant)
        self.comboBoxTribe.setObjectName(_fromUtf8("comboBoxTribe"))
        self.gridLayout.addWidget(self.comboBoxTribe, 20, 4, 1, 1)
        self.labelPayment = QtGui.QLabel(DialogAddNewApplicant)
        self.labelPayment.setObjectName(_fromUtf8("labelPayment"))
        self.gridLayout.addWidget(self.labelPayment, 17, 1, 1, 1)
        self.line = QtGui.QFrame(DialogAddNewApplicant)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 6, 1, 1, 4)
        self.labelBunkhouse = QtGui.QLabel(DialogAddNewApplicant)
        self.labelBunkhouse.setObjectName(_fromUtf8("labelBunkhouse"))
        self.gridLayout.addWidget(self.labelBunkhouse, 20, 1, 1, 1)
        self.checkBoxPayment = QtGui.QCheckBox(DialogAddNewApplicant)
        self.checkBoxPayment.setObjectName(_fromUtf8("checkBoxPayment"))
        self.gridLayout.addWidget(self.checkBoxPayment, 17, 2, 1, 1)
        self.label_5 = QtGui.QLabel(DialogAddNewApplicant)
        self.label_5.setMinimumSize(QtCore.QSize(90, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 7, 1, 1, 1)
        self.lineEmergencyPhone = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineEmergencyPhone.setObjectName(_fromUtf8("lineEmergencyPhone"))
        self.gridLayout.addWidget(self.lineEmergencyPhone, 13, 4, 1, 1)
        self.labelEquipmentsCheck = QtGui.QLabel(DialogAddNewApplicant)
        self.labelEquipmentsCheck.setObjectName(_fromUtf8("labelEquipmentsCheck"))
        self.gridLayout.addWidget(self.labelEquipmentsCheck, 18, 3, 1, 1)
        self.lineLine1 = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineLine1.setObjectName(_fromUtf8("lineLine1"))
        self.gridLayout.addWidget(self.lineLine1, 8, 2, 1, 1)
        self.lineCellPhone = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineCellPhone.setObjectName(_fromUtf8("lineCellPhone"))
        self.gridLayout.addWidget(self.lineCellPhone, 5, 2, 1, 1)
        self.labelLine2 = QtGui.QLabel(DialogAddNewApplicant)
        self.labelLine2.setObjectName(_fromUtf8("labelLine2"))
        self.gridLayout.addWidget(self.labelLine2, 8, 3, 1, 1)
        self.lineEmail = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineEmail.setObjectName(_fromUtf8("lineEmail"))
        self.gridLayout.addWidget(self.lineEmail, 4, 2, 1, 1)
        self.comboBoxCamp = QtGui.QComboBox(DialogAddNewApplicant)
        self.comboBoxCamp.setObjectName(_fromUtf8("comboBoxCamp"))
        self.gridLayout.addWidget(self.comboBoxCamp, 5, 4, 1, 1)
        self.lineHomePhone = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineHomePhone.setObjectName(_fromUtf8("lineHomePhone"))
        self.gridLayout.addWidget(self.lineHomePhone, 4, 4, 1, 1)
        self.comboBoxAcceptanceDecision = QtGui.QComboBox(DialogAddNewApplicant)
        self.comboBoxAcceptanceDecision.setObjectName(_fromUtf8("comboBoxAcceptanceDecision"))
        self.gridLayout.addWidget(self.comboBoxAcceptanceDecision, 17, 4, 1, 1)
        self.checkBoxFormsCheck = QtGui.QCheckBox(DialogAddNewApplicant)
        self.checkBoxFormsCheck.setObjectName(_fromUtf8("checkBoxFormsCheck"))
        self.gridLayout.addWidget(self.checkBoxFormsCheck, 18, 2, 1, 1)
        self.labelLine1 = QtGui.QLabel(DialogAddNewApplicant)
        self.labelLine1.setObjectName(_fromUtf8("labelLine1"))
        self.gridLayout.addWidget(self.labelLine1, 8, 1, 1, 1)
        self.labelCamp = QtGui.QLabel(DialogAddNewApplicant)
        self.labelCamp.setObjectName(_fromUtf8("labelCamp"))
        self.gridLayout.addWidget(self.labelCamp, 5, 3, 1, 1)
        self.labelState = QtGui.QLabel(DialogAddNewApplicant)
        self.labelState.setObjectName(_fromUtf8("labelState"))
        self.gridLayout.addWidget(self.labelState, 9, 3, 1, 1)
        self.labelCity = QtGui.QLabel(DialogAddNewApplicant)
        self.labelCity.setObjectName(_fromUtf8("labelCity"))
        self.gridLayout.addWidget(self.labelCity, 9, 1, 1, 1)
        self.lineCity = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineCity.setObjectName(_fromUtf8("lineCity"))
        self.gridLayout.addWidget(self.lineCity, 9, 2, 1, 1)
        self.lineZipCode = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineZipCode.setObjectName(_fromUtf8("lineZipCode"))
        self.gridLayout.addWidget(self.lineZipCode, 10, 2, 1, 1)
        self.labelEmergencyName = QtGui.QLabel(DialogAddNewApplicant)
        self.labelEmergencyName.setObjectName(_fromUtf8("labelEmergencyName"))
        self.gridLayout.addWidget(self.labelEmergencyName, 13, 1, 1, 1)
        self.labelTribe = QtGui.QLabel(DialogAddNewApplicant)
        self.labelTribe.setObjectName(_fromUtf8("labelTribe"))
        self.gridLayout.addWidget(self.labelTribe, 20, 3, 1, 1)
        self.labelFormsCheck = QtGui.QLabel(DialogAddNewApplicant)
        self.labelFormsCheck.setObjectName(_fromUtf8("labelFormsCheck"))
        self.gridLayout.addWidget(self.labelFormsCheck, 18, 1, 1, 1)
        self.lineState = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineState.setObjectName(_fromUtf8("lineState"))
        self.gridLayout.addWidget(self.lineState, 9, 4, 1, 1)
        self.label_14 = QtGui.QLabel(DialogAddNewApplicant)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 12, 1, 1, 1)
        self.lineLine2 = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineLine2.setObjectName(_fromUtf8("lineLine2"))
        self.gridLayout.addWidget(self.lineLine2, 8, 4, 1, 1)
        self.line_2 = QtGui.QFrame(DialogAddNewApplicant)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 11, 1, 1, 4)
        self.labelCellPhone = QtGui.QLabel(DialogAddNewApplicant)
        self.labelCellPhone.setObjectName(_fromUtf8("labelCellPhone"))
        self.gridLayout.addWidget(self.labelCellPhone, 5, 1, 1, 1)
        self.label_17 = QtGui.QLabel(DialogAddNewApplicant)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 15, 1, 1, 1)
        self.labelZipCode = QtGui.QLabel(DialogAddNewApplicant)
        self.labelZipCode.setObjectName(_fromUtf8("labelZipCode"))
        self.gridLayout.addWidget(self.labelZipCode, 10, 1, 1, 1)
        self.labelEmail = QtGui.QLabel(DialogAddNewApplicant)
        self.labelEmail.setObjectName(_fromUtf8("labelEmail"))
        self.gridLayout.addWidget(self.labelEmail, 4, 1, 1, 1)
        self.labelHomePhone = QtGui.QLabel(DialogAddNewApplicant)
        self.labelHomePhone.setObjectName(_fromUtf8("labelHomePhone"))
        self.gridLayout.addWidget(self.labelHomePhone, 4, 3, 1, 1)
        self.line_3 = QtGui.QFrame(DialogAddNewApplicant)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 14, 1, 1, 4)
        self.checkBoxEquipmentsCheck = QtGui.QCheckBox(DialogAddNewApplicant)
        self.checkBoxEquipmentsCheck.setObjectName(_fromUtf8("checkBoxEquipmentsCheck"))
        self.gridLayout.addWidget(self.checkBoxEquipmentsCheck, 18, 4, 1, 1)
        self.labelEmergencyPhone = QtGui.QLabel(DialogAddNewApplicant)
        self.labelEmergencyPhone.setObjectName(_fromUtf8("labelEmergencyPhone"))
        self.gridLayout.addWidget(self.labelEmergencyPhone, 13, 3, 1, 1)
        self.lineEmergencyName = QtGui.QLineEdit(DialogAddNewApplicant)
        self.lineEmergencyName.setObjectName(_fromUtf8("lineEmergencyName"))
        self.gridLayout.addWidget(self.lineEmergencyName, 13, 2, 1, 1)
        self.pushButtonSubmit = QtGui.QPushButton(DialogAddNewApplicant)
        self.pushButtonSubmit.setObjectName(_fromUtf8("pushButtonSubmit"))
        self.gridLayout.addWidget(self.pushButtonSubmit, 22, 4, 1, 1)
        self.pushButtonGenerateLetter = QtGui.QPushButton(DialogAddNewApplicant)
        self.pushButtonGenerateLetter.setObjectName(_fromUtf8("pushButtonGenerateLetter"))
        self.gridLayout.addWidget(self.pushButtonGenerateLetter, 22, 2, 1, 1)
        # click submit button
        self.pushButtonSubmit.clicked.connect(lambda:self.submitDataToDB(DialogAddNewApplicant))
        self.pushButtonGenerateLetter.clicked.connect(lambda:self.generateLetter(DialogAddNewApplicant))

        self.dateEditDOB = QtGui.QDateEdit(DialogAddNewApplicant)
        self.dateEditDOB.setObjectName(_fromUtf8("dateEditDOB"))
        self.dateEditDOB.setDate(QtCore.QDate(1800,1,1))
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
        DialogAddNewApplicant.setTabOrder(self.comboBoxTribe, self.pushButtonSubmit)
        self.p = p
        self.comboBoxCamp.addItem('')
        self.comboBoxBunkhouse.addItem('')
        self.comboBoxTribe.addItem('')
        self.comboBoxAcceptanceDecision.addItem('')
        self.comboBoxCamp.addItems([str(x.name) for x in self.p.camps])
        self.comboBoxBunkhouse.addItems([str(x.name) for x in self.p.bunkhouses])
        self.comboBoxTribe.addItems([str(x.name) for x in self.p.tribes])
        self.comboBoxAcceptanceDecision.addItems(['1-Accept','2-Conditional Accept', '3-Denial'])

        # list = [firstName, lastName,..]
    def checkBlankCells(self):
        if self.lineFirstName.text()=='' or self.lineGender.text()==''\
        or self.lineLastName.text()=='' or self.dateEditDOB.date().toPyDate()==datetime.date(1800,1,1)\
        or self.lineEmail.text()=='' or self.lineHomePhone.text()=='' or self.lineCellPhone.text()==''\
        or self.comboBoxCamp.currentIndex==0 or self.lineLine1.text()=='' or self.lineCity.text()==''\
        or self.lineState.text()=='' or self.lineState.text()=='' or self.lineZipCode.text()=='':
            return True
        else:
            return False
        
    def generateLetter(self,DialogAddNewApplicant):
        letter = self.p.generateLetterOfAcceptance(self.comboBoxAcceptanceDecision.currentIndex(),\
        self.p.camps[self.comboBoxCamp.currentIndex()-1])

        self.DialogLetterOfAcceptance = QtGui.QDialog()
        ui = Ui_DialogLetterOfAcceptance()
        ui.setupUi(self.DialogLetterOfAcceptance)
        ui.writeLetter(letter)
        
        self.DialogLetterOfAcceptance.show()

        # QtGui.QMessageBox.warning(DialogAddNewApplicant,"Letter Of Acceptance",
        # letter, QtGui.QMessageBox.Cancel,
        # QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
        # QtGui.QMessageBox.about(DialogAddNewApplicant,'Letter Of Acceptance',letter)
        
    def submitDataToDB(self,DialogAddNewApplicant):
        firstName = self.lineFirstName.text()
        lastName = self.lineLastName.text()
        gender = self.lineGender.text()
        dateOfBirth =self.dateEditDOB.date().toPyDate()
        age =datetime.datetime.now().year - dateOfBirth.year
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
        validationRes = self.p.validateApplicant(campId-1,gender,age)
        print(self.checkBlankCells())
        if self.checkBlankCells():
            
            QtGui.QMessageBox.warning(DialogAddNewApplicant,"Invalid Inputs",
            "The fileds with * cannot be empty.", QtGui.QMessageBox.Cancel,
            QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
            
        elif self.comboBoxAcceptanceDecision.currentIndex() == 1 and not validationRes['ok']:
            
            QtGui.QMessageBox.warning(DialogAddNewApplicant,"Application cannot be accepted",
            "This application cannot be accepted due to {}".format(validationRes['msg']), QtGui.QMessageBox.Cancel,
            QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)
        
        elif self.comboBoxAcceptanceDecision.currentIndex() == 1 and not self.checkBoxPayment.isChecked():
            QtGui.QMessageBox.warning(DialogAddNewApplicant,"Application cannot be accepted",
            "This application cannot be accepted since the payment check has not been recieve", QtGui.QMessageBox.Cancel,
            QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)

        else:
            res = self.p.addNewApplicant(a)
            print(res)
            QtGui.QMessageBox.warning(DialogAddNewApplicant,"Success",
            res['result']['msg'], QtGui.QMessageBox.Ok,
            QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)

            DialogAddNewApplicant.accept()

            print(res)
            

            # popup window
        

    def retranslateUi(self, DialogAddNewApplicant):
        DialogAddNewApplicant.setWindowTitle(_translate("DialogAddNewApplicant", "Add New Applicant", None))
        self.labelGender.setText(_translate("DialogAddNewApplicant", "Gender *", None))
        self.labelLastName.setText(_translate("DialogAddNewApplicant", "Last Name *", None))
        self.label_18.setText(_translate("DialogAddNewApplicant", "Applicant Basic Information:", None))
        self.labelFirstName.setText(_translate("DialogAddNewApplicant", "First Name *", None))
        self.labelApplicationDate.setText(_translate("DialogAddNewApplicant", "Application Date *", None))
        self.labelDOB.setText(_translate("DialogAddNewApplicant", "Date of Birth *", None))
        self.labelReviewDate.setText(_translate("DialogAddNewApplicant", "Review Date", None))
        self.labelAcceptanceDecision.setText(_translate("DialogAddNewApplicant", "Accepted?", None))
        self.labelPayment.setText(_translate("DialogAddNewApplicant", "Payment", None))
        self.labelBunkhouse.setText(_translate("DialogAddNewApplicant", "Bunkhouse", None))
        self.checkBoxPayment.setText(_translate("DialogAddNewApplicant", "Check Recieved?", None))
        self.label_5.setText(_translate("DialogAddNewApplicant", "Address:", None))
        self.labelEquipmentsCheck.setText(_translate("DialogAddNewApplicant", "Equipments", None))
        self.labelLine2.setText(_translate("DialogAddNewApplicant", "Line 2", None))
        self.checkBoxFormsCheck.setText(_translate("DialogAddNewApplicant", "Camper has all required forms?", None))
        self.labelLine1.setText(_translate("DialogAddNewApplicant", "Line 1 *", None))
        self.labelCamp.setText(_translate("DialogAddNewApplicant", "Camp Interested *", None))
        self.labelState.setText(_translate("DialogAddNewApplicant", "State *", None))
        self.labelCity.setText(_translate("DialogAddNewApplicant", "City *", None))
        self.labelEmergencyName.setText(_translate("DialogAddNewApplicant", "Name", None))
        self.labelTribe.setText(_translate("DialogAddNewApplicant", "Tribe", None))
        self.labelFormsCheck.setText(_translate("DialogAddNewApplicant", "Forms", None))
        self.label_14.setText(_translate("DialogAddNewApplicant", "Emergency Contact:", None))
        self.labelCellPhone.setText(_translate("DialogAddNewApplicant", "Cell Phone *", None))
        self.label_17.setText(_translate("DialogAddNewApplicant", "Admin:", None))
        self.labelZipCode.setText(_translate("DialogAddNewApplicant", "ZipCode *", None))
        self.labelEmail.setText(_translate("DialogAddNewApplicant", "Email *", None))
        self.labelHomePhone.setText(_translate("DialogAddNewApplicant", "Home Phone *", None))
        self.checkBoxEquipmentsCheck.setText(_translate("DialogAddNewApplicant", "Camper has all required equipments?", None))
        self.labelEmergencyPhone.setText(_translate("DialogAddNewApplicant", "Phone", None))
        self.pushButtonSubmit.setText(_translate("DialogAddNewApplicant", "Submit", None))
        self.pushButtonSubmit.setText(_translate("DialogAddNewApplicant", "Submit", None))
        self.pushButtonGenerateLetter.setText(_translate("DialogAddNewApplicant", "Generate Acceptance Letter", None))


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
        self.tableWidgetApplicantTable.setColumnCount(23)
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
        self.gridLayout.addWidget(self.tableWidgetApplicantTable, 3, 0, 1, 6)
        self.labelCamp = QtGui.QLabel(DialogLookUpApplicant)
        self.labelCamp.setObjectName(_fromUtf8("labelCamp"))
        self.gridLayout.addWidget(self.labelCamp, 1, 0, 1, 1)
        self.labelDOB = QtGui.QLabel(DialogLookUpApplicant)
        self.labelDOB.setObjectName(_fromUtf8("labelDOB"))
        self.gridLayout.addWidget(self.labelDOB, 1, 2, 1, 1)
        self.dateEditDOB = QtGui.QDateEdit(DialogLookUpApplicant)
        self.dateEditDOB.setObjectName(_fromUtf8("dateEditDOB"))
        self.dateEditDOB.setDate(QtCore.QDate(1800,1,1))
        self.gridLayout.addWidget(self.dateEditDOB, 1, 3, 1, 1)
        self.pushButtonLookUp = QtGui.QPushButton(DialogLookUpApplicant)
        self.pushButtonLookUp.setObjectName(_fromUtf8("pushButtonLookUp"))
        self.gridLayout.addWidget(self.pushButtonLookUp, 0, 5, 2, 1)
        self.comboBoxCamp = QtGui.QComboBox(DialogLookUpApplicant)
        self.comboBoxCamp.setObjectName(_fromUtf8("comboBoxCamp"))
        self.gridLayout.addWidget(self.comboBoxCamp, 1, 1, 1, 1)

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


    def lookUpApplicant(self):
        firstName = self.lineFirstName.text()
        lastName = self.lineLastName.text()
        dob = self.dateEditDOB.date().toPyDate()
        campId = self.comboBoxCamp.currentText()
        if firstName=='' and lastName == '' and dob < datetime.date(2016,1,1) and campId =='':
            condition = ''
        else:
            cols = ['firstName', 'lastName','dateOfBirth','campId']
            values = [firstName,lastName,dob,campId]
            tests = [firstName!='',lastName!='',dob>datetime.date(2016,1,1),campId!='']
            cons = [cols[i] + '=' +'\''+str(values[i])+'\'' for i in range(len(cols)) if tests[i]]
            condition = ' and '.join(cons)
        
        res = self.p.interacteDB('select','applicant',condition) 
        applicants = res['result']
        self.tableWidgetApplicantTable.clear()
        if len(applicants)>0:
            self.tableWidgetApplicantTable.setRowCount(len(applicants))
            self.tableWidgetApplicantTable.setColumnCount(len(applicants[0]))

            cols = ['First Name', 'Last Name','Gender','Date Of Birth','Line 1',\
            'Line 2','City','State','Zip Code','Email','Home Phone','Cell Phone',\
            'Payment','Application Date','Review Date','Decision Id','Forms Checked',\
            'Equipments Checked', 'Camp Id', 'Emergency Contact Name', \
            'Emergency Contact Phone','Bunkhouse Id','Tribe Id']
            for i in range(23):
                self.tableWidgetApplicantTable.setHorizontalHeaderItem(i, QtGui.QTableWidgetItem(cols[i]))
            
            
            
            applicants_list = []
            # print(applicants)
            for a in applicants:
                address = self.p.interacteDB('select','address','id = \''+str(a['addressId'])+'\'')['result'][0]
                if a['emergencyContactId'] == '':
                    emergencyContact = {'name':'','phone':''}
                else:
                    emergencyContact = self.p.interacteDB('select','emergencyContact','id = \''+str(a['emergencyContactId'])+'\'')['result'][0]
                l = [a['firstName'],a['lastName'],a['gender'],\
                a['dateOfBirth'],address['line1'],address['line2'],address['city'],address['state'],\
                address['zipCode'],a['email'],a['homePhone'],a['cellPhone'],a['payment'],\
                a['applicationDate'],a['reviewDate'],a['decisionId'],a['formsChecked'],\
                a['equipmentsChecked'], a['campId'],emergencyContact['name'],\
                emergencyContact['phone'],a['bunkhouseId'],a['tribeId']]
                applicants_list.append(l)

            for i, a in enumerate(applicants_list):
                for j,item in enumerate(a):
                    self.tableWidgetApplicantTable.setItem(i,j,QtGui.QTableWidgetItem(item))
   


    def retranslateUi(self, DialogLookUpApplicant):
        DialogLookUpApplicant.setWindowTitle(_translate("DialogLookUpApplicant", "Look Up Applicant", None))
        self.labelLastName.setText(_translate("DialogLookUpApplicant", "Last Name", None))
        self.labelFirstName.setText(_translate("DialogLookUpApplicant", "First Name", None))
        self.pushButtonUpdate.setText(_translate("DialogLookUpApplicant", "Update", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(0)
        item.setText(_translate("DialogLookUpApplicant", "First Name", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(1)
        item.setText(_translate("DialogLookUpApplicant", "Last Name", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(2)
        item.setText(_translate("DialogLookUpApplicant", "Gender", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(3)
        item.setText(_translate("DialogLookUpApplicant", "Date Of Birth", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(4)
        item.setText(_translate("DialogLookUpApplicant", "Line 1", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(5)
        item.setText(_translate("DialogLookUpApplicant", "Line 2", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(6)
        item.setText(_translate("DialogLookUpApplicant", "City", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(7)
        item.setText(_translate("DialogLookUpApplicant", "State", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(8)
        item.setText(_translate("DialogLookUpApplicant", "Zip Code", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(9)
        item.setText(_translate("DialogLookUpApplicant", "Email", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(10)
        item.setText(_translate("DialogLookUpApplicant", "Home Phone", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(11)
        item.setText(_translate("DialogLookUpApplicant", "Cell Phone", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(12)
        item.setText(_translate("DialogLookUpApplicant", "Payment", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(13)
        item.setText(_translate("DialogLookUpApplicant", "Application Date", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(14)
        item.setText(_translate("DialogLookUpApplicant", "Review Date", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(15)
        item.setText(_translate("DialogLookUpApplicant", "Decision Id", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(16)
        item.setText(_translate("DialogLookUpApplicant", "Forms Checked", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(17)
        item.setText(_translate("DialogLookUpApplicant", "Equipments Checked", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(18)
        item.setText(_translate("DialogLookUpApplicant", "Camp Id", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(19)
        item.setText(_translate("DialogLookUpApplicant", "Emergency Contact Name", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(20)
        item.setText(_translate("DialogLookUpApplicant", "Emergency Contact Phone Number", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(21)
        item.setText(_translate("DialogLookUpApplicant", "Bunkhouse Id", None))
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(22)
        item.setText(_translate("DialogLookUpApplicant", "Tribe Id", None))
        self.labelCamp.setText(_translate("DialogLookUpApplicant", "Camp", None))
        self.labelDOB.setText(_translate("DialogLookUpApplicant", "Date of Birth", None))
        self.pushButtonLookUp.setText(_translate("DialogLookUpApplicant", "Look Up", None))










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
        DialogLetterOfAcceptance.setWindowTitle(_translate("DialogLetterOfAcceptance", "Letter of Acceptance", None))
        self.pushButtonOkay.setText(_translate("DialogLetterOfAcceptance", "Okay", None))


if __name__ == "__main__":
    p = Processor()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,p)
    MainWindow.show()
    sys.exit(app.exec_())
    p.kill()

