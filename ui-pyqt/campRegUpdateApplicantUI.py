# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'campRegUpdateApplicant.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_DialogUpdateApplicant(object):
    def setupUi(self, DialogUpdateApplicant):
        DialogUpdateApplicant.setObjectName(_fromUtf8("DialogUpdateApplicant"))
        DialogUpdateApplicant.resize(1389, 1010)
        DialogUpdateApplicant.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        DialogUpdateApplicant.setAutoFillBackground(False)
        DialogUpdateApplicant.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(DialogUpdateApplicant)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_14 = QtGui.QLabel(DialogUpdateApplicant)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 13, 1, 1, 4)
        self.comboBoxTribe = QtGui.QComboBox(DialogUpdateApplicant)
        self.comboBoxTribe.setObjectName(_fromUtf8("comboBoxTribe"))
        self.gridLayout.addWidget(self.comboBoxTribe, 21, 4, 1, 1)
        self.labelFirstName = QtGui.QLabel(DialogUpdateApplicant)
        self.labelFirstName.setObjectName(_fromUtf8("labelFirstName"))
        self.gridLayout.addWidget(self.labelFirstName, 1, 1, 1, 1)
        self.checkBoxPayment = QtGui.QCheckBox(DialogUpdateApplicant)
        self.checkBoxPayment.setObjectName(_fromUtf8("checkBoxPayment"))
        self.gridLayout.addWidget(self.checkBoxPayment, 18, 2, 1, 1)
        self.labelApplicationDate = QtGui.QLabel(DialogUpdateApplicant)
        self.labelApplicationDate.setObjectName(_fromUtf8("labelApplicationDate"))
        self.gridLayout.addWidget(self.labelApplicationDate, 17, 1, 1, 1)
        self.lineEmergencyPhone = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineEmergencyPhone.setObjectName(_fromUtf8("lineEmergencyPhone"))
        self.gridLayout.addWidget(self.lineEmergencyPhone, 14, 4, 1, 1)
        self.dateApplicationDate = QtGui.QDateEdit(DialogUpdateApplicant)
        self.dateApplicationDate.setObjectName(_fromUtf8("dateApplicationDate"))
        self.gridLayout.addWidget(self.dateApplicationDate, 17, 2, 1, 1)
        self.labelEquipmentsCheck = QtGui.QLabel(DialogUpdateApplicant)
        self.labelEquipmentsCheck.setObjectName(_fromUtf8("labelEquipmentsCheck"))
        self.gridLayout.addWidget(self.labelEquipmentsCheck, 19, 3, 1, 1)
        self.labelLine2 = QtGui.QLabel(DialogUpdateApplicant)
        self.labelLine2.setObjectName(_fromUtf8("labelLine2"))
        self.gridLayout.addWidget(self.labelLine2, 9, 3, 1, 1)
        self.lineFirstName = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineFirstName.setObjectName(_fromUtf8("lineFirstName"))
        self.gridLayout.addWidget(self.lineFirstName, 1, 2, 1, 1)
        self.lineCity = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineCity.setObjectName(_fromUtf8("lineCity"))
        self.gridLayout.addWidget(self.lineCity, 10, 2, 1, 1)
        self.labelDOB = QtGui.QLabel(DialogUpdateApplicant)
        self.labelDOB.setObjectName(_fromUtf8("labelDOB"))
        self.gridLayout.addWidget(self.labelDOB, 2, 3, 1, 1)
        self.labelAcceptanceDecision = QtGui.QLabel(DialogUpdateApplicant)
        self.labelAcceptanceDecision.setObjectName(_fromUtf8("labelAcceptanceDecision"))
        self.gridLayout.addWidget(self.labelAcceptanceDecision, 18, 3, 1, 1)
        self.labelEmergencyName = QtGui.QLabel(DialogUpdateApplicant)
        self.labelEmergencyName.setObjectName(_fromUtf8("labelEmergencyName"))
        self.gridLayout.addWidget(self.labelEmergencyName, 14, 1, 1, 1)
        self.dateReviewDate = QtGui.QDateEdit(DialogUpdateApplicant)
        self.dateReviewDate.setObjectName(_fromUtf8("dateReviewDate"))
        self.gridLayout.addWidget(self.dateReviewDate, 17, 4, 1, 1)
        self.labelReviewDate = QtGui.QLabel(DialogUpdateApplicant)
        self.labelReviewDate.setObjectName(_fromUtf8("labelReviewDate"))
        self.gridLayout.addWidget(self.labelReviewDate, 17, 3, 1, 1)
        self.labelPayment = QtGui.QLabel(DialogUpdateApplicant)
        self.labelPayment.setObjectName(_fromUtf8("labelPayment"))
        self.gridLayout.addWidget(self.labelPayment, 18, 1, 1, 1)
        self.labelLine1 = QtGui.QLabel(DialogUpdateApplicant)
        self.labelLine1.setObjectName(_fromUtf8("labelLine1"))
        self.gridLayout.addWidget(self.labelLine1, 9, 1, 1, 1)
        self.labelEmergencyPhone = QtGui.QLabel(DialogUpdateApplicant)
        self.labelEmergencyPhone.setObjectName(_fromUtf8("labelEmergencyPhone"))
        self.gridLayout.addWidget(self.labelEmergencyPhone, 14, 3, 1, 1)
        self.line = QtGui.QFrame(DialogUpdateApplicant)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 7, 1, 1, 4)
        self.comboBoxBunkhouse = QtGui.QComboBox(DialogUpdateApplicant)
        self.comboBoxBunkhouse.setObjectName(_fromUtf8("comboBoxBunkhouse"))
        self.gridLayout.addWidget(self.comboBoxBunkhouse, 21, 2, 1, 1)
        self.labelBunkhouse = QtGui.QLabel(DialogUpdateApplicant)
        self.labelBunkhouse.setObjectName(_fromUtf8("labelBunkhouse"))
        self.gridLayout.addWidget(self.labelBunkhouse, 21, 1, 1, 1)
        self.labelZipCode = QtGui.QLabel(DialogUpdateApplicant)
        self.labelZipCode.setObjectName(_fromUtf8("labelZipCode"))
        self.gridLayout.addWidget(self.labelZipCode, 11, 1, 1, 1)
        self.lineEmergencyName = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineEmergencyName.setObjectName(_fromUtf8("lineEmergencyName"))
        self.gridLayout.addWidget(self.lineEmergencyName, 14, 2, 1, 1)
        self.lineLine1 = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineLine1.setObjectName(_fromUtf8("lineLine1"))
        self.gridLayout.addWidget(self.lineLine1, 9, 2, 1, 1)
        self.checkBoxEquipmentsCheck = QtGui.QCheckBox(DialogUpdateApplicant)
        self.checkBoxEquipmentsCheck.setObjectName(_fromUtf8("checkBoxEquipmentsCheck"))
        self.gridLayout.addWidget(self.checkBoxEquipmentsCheck, 19, 4, 1, 1)
        self.labelEmail = QtGui.QLabel(DialogUpdateApplicant)
        self.labelEmail.setObjectName(_fromUtf8("labelEmail"))
        self.gridLayout.addWidget(self.labelEmail, 5, 1, 1, 1)
        self.comboBoxAcceptanceDecision = QtGui.QComboBox(DialogUpdateApplicant)
        self.comboBoxAcceptanceDecision.setObjectName(_fromUtf8("comboBoxAcceptanceDecision"))
        self.gridLayout.addWidget(self.comboBoxAcceptanceDecision, 18, 4, 1, 1)
        self.lineLastName = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineLastName.setObjectName(_fromUtf8("lineLastName"))
        self.gridLayout.addWidget(self.lineLastName, 1, 4, 1, 1)
        self.lineZipCode = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineZipCode.setObjectName(_fromUtf8("lineZipCode"))
        self.gridLayout.addWidget(self.lineZipCode, 11, 2, 1, 1)
        self.labelFormsCheck = QtGui.QLabel(DialogUpdateApplicant)
        self.labelFormsCheck.setObjectName(_fromUtf8("labelFormsCheck"))
        self.gridLayout.addWidget(self.labelFormsCheck, 19, 1, 1, 1)
        self.labelHomePhone = QtGui.QLabel(DialogUpdateApplicant)
        self.labelHomePhone.setObjectName(_fromUtf8("labelHomePhone"))
        self.gridLayout.addWidget(self.labelHomePhone, 5, 3, 1, 1)
        self.lineCellPhone = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineCellPhone.setObjectName(_fromUtf8("lineCellPhone"))
        self.gridLayout.addWidget(self.lineCellPhone, 6, 2, 1, 1)
        self.line_3 = QtGui.QFrame(DialogUpdateApplicant)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 15, 1, 1, 4)
        self.lineLine2 = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineLine2.setObjectName(_fromUtf8("lineLine2"))
        self.gridLayout.addWidget(self.lineLine2, 9, 4, 1, 1)
        self.labelLastName = QtGui.QLabel(DialogUpdateApplicant)
        self.labelLastName.setObjectName(_fromUtf8("labelLastName"))
        self.gridLayout.addWidget(self.labelLastName, 1, 3, 1, 1)
        self.labelGender = QtGui.QLabel(DialogUpdateApplicant)
        self.labelGender.setObjectName(_fromUtf8("labelGender"))
        self.gridLayout.addWidget(self.labelGender, 2, 1, 1, 1)
        self.dateEditDOB = QtGui.QDateEdit(DialogUpdateApplicant)
        self.dateEditDOB.setObjectName(_fromUtf8("dateEditDOB"))
        self.gridLayout.addWidget(self.dateEditDOB, 2, 4, 1, 1)
        self.lineHomePhone = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineHomePhone.setObjectName(_fromUtf8("lineHomePhone"))
        self.gridLayout.addWidget(self.lineHomePhone, 5, 4, 1, 1)
        self.label_17 = QtGui.QLabel(DialogUpdateApplicant)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 16, 1, 1, 1)
        self.labelTribe = QtGui.QLabel(DialogUpdateApplicant)
        self.labelTribe.setObjectName(_fromUtf8("labelTribe"))
        self.gridLayout.addWidget(self.labelTribe, 21, 3, 1, 1)
        self.lineGender = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineGender.setObjectName(_fromUtf8("lineGender"))
        self.gridLayout.addWidget(self.lineGender, 2, 2, 1, 1)
        self.checkBoxFormsCheck = QtGui.QCheckBox(DialogUpdateApplicant)
        self.checkBoxFormsCheck.setObjectName(_fromUtf8("checkBoxFormsCheck"))
        self.gridLayout.addWidget(self.checkBoxFormsCheck, 19, 2, 1, 1)
        self.lineState = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineState.setObjectName(_fromUtf8("lineState"))
        self.gridLayout.addWidget(self.lineState, 10, 4, 1, 1)
        self.lineEmail = QtGui.QLineEdit(DialogUpdateApplicant)
        self.lineEmail.setObjectName(_fromUtf8("lineEmail"))
        self.gridLayout.addWidget(self.lineEmail, 5, 2, 1, 1)
        self.labelState = QtGui.QLabel(DialogUpdateApplicant)
        self.labelState.setObjectName(_fromUtf8("labelState"))
        self.gridLayout.addWidget(self.labelState, 10, 3, 1, 1)
        self.label_5 = QtGui.QLabel(DialogUpdateApplicant)
        self.label_5.setMinimumSize(QtCore.QSize(90, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 8, 1, 1, 1)
        self.label_18 = QtGui.QLabel(DialogUpdateApplicant)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 0, 1, 1, 1)
        self.labelId = QtGui.QLabel(DialogUpdateApplicant)
        self.labelId.setText(_fromUtf8(""))
        self.labelId.setObjectName(_fromUtf8("labelId"))
        self.gridLayout.addWidget(self.labelId, 0, 2, 1, 1)
        self.labelCity = QtGui.QLabel(DialogUpdateApplicant)
        self.labelCity.setObjectName(_fromUtf8("labelCity"))
        self.gridLayout.addWidget(self.labelCity, 10, 1, 1, 1)
        self.line_2 = QtGui.QFrame(DialogUpdateApplicant)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 12, 1, 1, 4)
        self.labelCellPhone = QtGui.QLabel(DialogUpdateApplicant)
        self.labelCellPhone.setObjectName(_fromUtf8("labelCellPhone"))
        self.gridLayout.addWidget(self.labelCellPhone, 6, 1, 1, 1)
        self.widget = QtGui.QWidget(DialogUpdateApplicant)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 8, 2, 1, 2)
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
        self.pushButtonPreference = QtGui.QPushButton(self.frame_2)
        self.pushButtonPreference.setGeometry(QtCore.QRect(0, 29, 171, 41))
        self.pushButtonPreference.setObjectName(_fromUtf8("pushButtonPreference"))
        self.pushButtonPreference_2 = QtGui.QPushButton(self.frame_2)
        self.pushButtonPreference_2.setGeometry(QtCore.QRect(190, 30, 171, 41))
        self.pushButtonPreference_2.setObjectName(_fromUtf8("pushButtonPreference_2"))
        self.gridLayout.addWidget(self.frame_2, 22, 1, 1, 4)

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

    def retranslateUi(self, DialogUpdateApplicant):
        DialogUpdateApplicant.setWindowTitle(_translate("DialogUpdateApplicant", "Update Applicant", None))
        self.label_14.setText(_translate("DialogUpdateApplicant", "Emergency Contact:", None))
        self.labelFirstName.setText(_translate("DialogUpdateApplicant", "First Name", None))
        self.checkBoxPayment.setText(_translate("DialogUpdateApplicant", "Check Recieved?", None))
        self.labelApplicationDate.setText(_translate("DialogUpdateApplicant", "Application Date", None))
        self.labelEquipmentsCheck.setText(_translate("DialogUpdateApplicant", "Equipments", None))
        self.labelLine2.setText(_translate("DialogUpdateApplicant", "Line 2", None))
        self.labelDOB.setText(_translate("DialogUpdateApplicant", "Date of Birth", None))
        self.labelAcceptanceDecision.setText(_translate("DialogUpdateApplicant", "Accepted?", None))
        self.labelEmergencyName.setText(_translate("DialogUpdateApplicant", "Name", None))
        self.labelReviewDate.setText(_translate("DialogUpdateApplicant", "Review Date", None))
        self.labelPayment.setText(_translate("DialogUpdateApplicant", "Payment", None))
        self.labelLine1.setText(_translate("DialogUpdateApplicant", "Line 1", None))
        self.labelEmergencyPhone.setText(_translate("DialogUpdateApplicant", "Phone", None))
        self.labelBunkhouse.setText(_translate("DialogUpdateApplicant", "Bunkhouse", None))
        self.labelZipCode.setText(_translate("DialogUpdateApplicant", "ZipCode", None))
        self.checkBoxEquipmentsCheck.setText(_translate("DialogUpdateApplicant", "Camper has all required equipments?", None))
        self.labelEmail.setText(_translate("DialogUpdateApplicant", "Email:", None))
        self.labelFormsCheck.setText(_translate("DialogUpdateApplicant", "Forms", None))
        self.labelHomePhone.setText(_translate("DialogUpdateApplicant", "Home Phone", None))
        self.labelLastName.setText(_translate("DialogUpdateApplicant", "Last Name", None))
        self.labelGender.setText(_translate("DialogUpdateApplicant", "Gender", None))
        self.label_17.setText(_translate("DialogUpdateApplicant", "Admin:", None))
        self.labelTribe.setText(_translate("DialogUpdateApplicant", "Tribe", None))
        self.checkBoxFormsCheck.setText(_translate("DialogUpdateApplicant", "Camper has all required forms?", None))
        self.labelState.setText(_translate("DialogUpdateApplicant", "State", None))
        self.label_5.setText(_translate("DialogUpdateApplicant", "Address:", None))
        self.label_18.setText(_translate("DialogUpdateApplicant", "Applicant Basic Information:", None))
        self.labelCity.setText(_translate("DialogUpdateApplicant", "City", None))
        self.labelCellPhone.setText(_translate("DialogUpdateApplicant", "Cell Phone", None))
        self.labelCamp.setText(_translate("DialogUpdateApplicant", "Camp Interested", None))
        self.labelCampAvilability.setText(_translate("DialogUpdateApplicant", "TextLabel", None))
        self.pushButtonSubmit.setText(_translate("DialogUpdateApplicant", "Submit", None))
        self.pushButtonCheckList.setText(_translate("DialogUpdateApplicant", "Checkin Checklist", None))
        self.pushButtonPreference.setText(_translate("DialogUpdateApplicant", "BK Preference", None))
        self.pushButtonPreference_2.setText(_translate("DialogUpdateApplicant", "Tribe Preference", None))

