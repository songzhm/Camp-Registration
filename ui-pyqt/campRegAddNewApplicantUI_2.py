# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'campRegAddNewApplicant.ui'
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

class Ui_DialogAddNewApplicant(object):
    def setupUi(self, DialogAddNewApplicant):
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

    def retranslateUi(self, DialogAddNewApplicant):
        DialogAddNewApplicant.setWindowTitle(_translate("DialogAddNewApplicant", "Add New Applicant", None))
        self.labelCamp.setText(_translate("DialogAddNewApplicant", "Camp Interested", None))
        self.labelCampAvilability.setText(_translate("DialogAddNewApplicant", "TextLabel", None))
        self.label_14.setText(_translate("DialogAddNewApplicant", "Emergency Contact:", None))
        self.labelFirstName.setText(_translate("DialogAddNewApplicant", "First Name", None))
        self.labelPayment.setText(_translate("DialogAddNewApplicant", "Payment", None))
        self.checkBoxPayment.setText(_translate("DialogAddNewApplicant", "Check Recieved?", None))
        self.labelLine2.setText(_translate("DialogAddNewApplicant", "Line 2", None))
        self.labelDOB.setText(_translate("DialogAddNewApplicant", "Date of Birth", None))
        self.labelAcceptanceDecision.setText(_translate("DialogAddNewApplicant", "Accepted?", None))
        self.labelEmergencyName.setText(_translate("DialogAddNewApplicant", "Name", None))
        self.labelReviewDate.setText(_translate("DialogAddNewApplicant", "Review Date", None))
        self.labelBunkhouse.setText(_translate("DialogAddNewApplicant", "Bunkhouse", None))
        self.labelApplicationDate.setText(_translate("DialogAddNewApplicant", "Application Date", None))
        self.labelLine1.setText(_translate("DialogAddNewApplicant", "Line 1", None))
        self.labelEquipmentsCheck.setText(_translate("DialogAddNewApplicant", "Equipments", None))
        self.labelEmergencyPhone.setText(_translate("DialogAddNewApplicant", "Phone", None))
        self.checkBoxFormsCheck.setText(_translate("DialogAddNewApplicant", "Camper has all required forms?", None))
        self.labelZipCode.setText(_translate("DialogAddNewApplicant", "ZipCode", None))
        self.checkBoxEquipmentsCheck.setText(_translate("DialogAddNewApplicant", "Camper has all required equipments?", None))
        self.labelFormsCheck.setText(_translate("DialogAddNewApplicant", "Forms", None))
        self.label_17.setText(_translate("DialogAddNewApplicant", "Admin:", None))
        self.labelHomePhone.setText(_translate("DialogAddNewApplicant", "Home Phone", None))
        self.labelTribe.setText(_translate("DialogAddNewApplicant", "Tribe", None))
        self.labelEmail.setText(_translate("DialogAddNewApplicant", "Email:", None))
        self.labelLastName.setText(_translate("DialogAddNewApplicant", "Last Name", None))
        self.labelGender.setText(_translate("DialogAddNewApplicant", "Gender", None))
        self.labelCity.setText(_translate("DialogAddNewApplicant", "City", None))
        self.labelState.setText(_translate("DialogAddNewApplicant", "State", None))
        self.labelCellPhone.setText(_translate("DialogAddNewApplicant", "Cell Phone", None))
        self.label_5.setText(_translate("DialogAddNewApplicant", "Address:", None))
        self.label_18.setText(_translate("DialogAddNewApplicant", "Applicant Basic Information:", None))
        self.pushButtonGenerateLetter.setText(_translate("DialogAddNewApplicant", "Generate Acceptance Letter", None))
        self.pushButtonSubmit.setText(_translate("DialogAddNewApplicant", "Submit", None))
        self.pushButtonCheckList.setText(_translate("DialogAddNewApplicant", "Checkin Checklist", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAddNewApplicant = QtGui.QDialog()
    ui = Ui_DialogAddNewApplicant()
    ui.setupUi(DialogAddNewApplicant)
    DialogAddNewApplicant.show()
    sys.exit(app.exec_())

