# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'campRegLookUpApplicant.ui'
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

class Ui_DialogLookUpApplicant(object):
    def setupUi(self, DialogLookUpApplicant):
        DialogLookUpApplicant.setObjectName(_fromUtf8("DialogLookUpApplicant"))
        DialogLookUpApplicant.resize(1291, 999)
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
        self.labelDOB = QtGui.QLabel(DialogLookUpApplicant)
        self.labelDOB.setObjectName(_fromUtf8("labelDOB"))
        self.gridLayout.addWidget(self.labelDOB, 0, 4, 1, 1)
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
        self.pushButtonLookUp = QtGui.QPushButton(DialogLookUpApplicant)
        self.pushButtonLookUp.setObjectName(_fromUtf8("pushButtonLookUp"))
        self.gridLayout.addWidget(self.pushButtonLookUp, 1, 5, 1, 1)
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
        self.dateEditDOB = QtGui.QDateEdit(DialogLookUpApplicant)
        self.dateEditDOB.setObjectName(_fromUtf8("dateEditDOB"))
        self.gridLayout.addWidget(self.dateEditDOB, 0, 5, 1, 1)

        self.retranslateUi(DialogLookUpApplicant)
        QtCore.QMetaObject.connectSlotsByName(DialogLookUpApplicant)

    def retranslateUi(self, DialogLookUpApplicant):
        DialogLookUpApplicant.setWindowTitle(_translate("DialogLookUpApplicant", "Look Up Applicant", None))
        self.labelLastName.setText(_translate("DialogLookUpApplicant", "Last Name", None))
        self.labelFirstName.setText(_translate("DialogLookUpApplicant", "First Name", None))
        self.labelDOB.setText(_translate("DialogLookUpApplicant", "Date of Birth", None))
        self.pushButtonUpdate.setText(_translate("DialogLookUpApplicant", "Update", None))
        self.pushButtonLookUp.setText(_translate("DialogLookUpApplicant", "Look Up", None))
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
        item = self.tableWidgetApplicantTable.horizontalHeaderItem(23)
        item.setText(_translate("DialogLookUpApplicant", "Waiting List", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogLookUpApplicant = QtGui.QDialog()
    ui = Ui_DialogLookUpApplicant()
    ui.setupUi(DialogLookUpApplicant)
    DialogLookUpApplicant.show()
    sys.exit(app.exec_())

