# Form implementation generated from reading ui file 'record_dialogUI.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(394, 221)
        Dialog.setStyleSheet("QDialog {\n"
"    background: #F5FaFE;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"    background: #1E95FE;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    padding: 0px 8px;\n"
"}")
        self.cancelBtn = QtWidgets.QPushButton(parent=Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(50, 170, 113, 32))
        self.cancelBtn.setObjectName("cancelBtn")
        self.recordBtn = QtWidgets.QPushButton(parent=Dialog)
        self.recordBtn.setGeometry(QtCore.QRect(240, 170, 113, 32))
        self.recordBtn.setObjectName("recordBtn")
        self.selectLable = QtWidgets.QLabel(parent=Dialog)
        self.selectLable.setGeometry(QtCore.QRect(50, 70, 201, 21))
        self.selectLable.setObjectName("selectLable")
        self.teacherComboBox = QtWidgets.QComboBox(parent=Dialog)
        self.teacherComboBox.setGeometry(QtCore.QRect(260, 70, 104, 26))
        self.teacherComboBox.setObjectName("teacherComboBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Запись"))
        self.cancelBtn.setText(_translate("Dialog", "Отменить"))
        self.recordBtn.setText(_translate("Dialog", "Записаться"))
        self.selectLable.setText(_translate("Dialog", "Выбрать Преподавателя"))
