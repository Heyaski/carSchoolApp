# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 557)
        MainWindow.setStyleSheet("background: #F5FaFE;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 231, 561))
        self.widget.setStyleSheet("QWidget {\n"
"    background: #1E95FE\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"    padding: 5px 0px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    color: #1F95EF;\n"
"    background: #F5FAFE;\n"
"    border-radius: 10px;\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(50, 20, 121, 31))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.profileBtn = QtWidgets.QPushButton(parent=self.widget)
        self.profileBtn.setGeometry(QtCore.QRect(20, 90, 181, 32))
        self.profileBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.profileBtn.setCheckable(True)
        self.profileBtn.setChecked(True)
        self.profileBtn.setAutoExclusive(True)
        self.profileBtn.setObjectName("profileBtn")
        self.informationBtn = QtWidgets.QPushButton(parent=self.widget)
        self.informationBtn.setGeometry(QtCore.QRect(20, 140, 181, 32))
        self.informationBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.informationBtn.setCheckable(True)
        self.informationBtn.setAutoExclusive(True)
        self.informationBtn.setObjectName("informationBtn")
        self.teachersBtn = QtWidgets.QPushButton(parent=self.widget)
        self.teachersBtn.setGeometry(QtCore.QRect(20, 190, 181, 32))
        self.teachersBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.teachersBtn.setCheckable(True)
        self.teachersBtn.setAutoExclusive(True)
        self.teachersBtn.setObjectName("teachersBtn")
        self.scheduleBtn = QtWidgets.QPushButton(parent=self.widget)
        self.scheduleBtn.setGeometry(QtCore.QRect(22, 240, 181, 32))
        self.scheduleBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.scheduleBtn.setCheckable(True)
        self.scheduleBtn.setAutoExclusive(True)
        self.scheduleBtn.setObjectName("scheduleBtn")
        self.adminPanelBtn = QtWidgets.QPushButton(parent=self.widget)
        self.adminPanelBtn.setGeometry(QtCore.QRect(22, 290, 181, 32))
        self.adminPanelBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.adminPanelBtn.setCheckable(True)
        self.adminPanelBtn.setAutoExclusive(True)
        self.adminPanelBtn.setObjectName("adminPanelBtn")
        self.exitBtn = QtWidgets.QPushButton(parent=self.widget)
        self.exitBtn.setGeometry(QtCore.QRect(22, 480, 181, 32))
        self.exitBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.exitBtn.setStyleSheet("QPushButton {\n"
"    color: #1F95EF;\n"
"    background: #F5FAFE;\n"
"    border-radius: 10px;\n"
"}")
        self.exitBtn.setCheckable(True)
        self.exitBtn.setObjectName("exitBtn")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(230, 0, 641, 561))
        self.widget_2.setObjectName("widget_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_2)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 90, 591, 441))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.profile_page = QtWidgets.QWidget()
        self.profile_page.setStyleSheet("QLabel {\n"
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
        self.profile_page.setObjectName("profile_page")
        self.infoLable = QtWidgets.QLabel(parent=self.profile_page)
        self.infoLable.setGeometry(QtCore.QRect(30, 10, 201, 21))
        self.infoLable.setObjectName("infoLable")
        self.surnameLable = QtWidgets.QLabel(parent=self.profile_page)
        self.surnameLable.setGeometry(QtCore.QRect(30, 60, 81, 21))
        self.surnameLable.setObjectName("surnameLable")
        self.nameLable = QtWidgets.QLabel(parent=self.profile_page)
        self.nameLable.setGeometry(QtCore.QRect(30, 120, 60, 21))
        self.nameLable.setObjectName("nameLable")
        self.fatherLable = QtWidgets.QLabel(parent=self.profile_page)
        self.fatherLable.setGeometry(QtCore.QRect(30, 180, 81, 21))
        self.fatherLable.setObjectName("fatherLable")
        self.dateLable = QtWidgets.QLabel(parent=self.profile_page)
        self.dateLable.setGeometry(QtCore.QRect(30, 240, 131, 21))
        self.dateLable.setObjectName("dateLable")
        self.countLable = QtWidgets.QLabel(parent=self.profile_page)
        self.countLable.setGeometry(QtCore.QRect(310, 60, 171, 21))
        self.countLable.setObjectName("countLable")
        self.changePassBtn = QtWidgets.QPushButton(parent=self.profile_page)
        self.changePassBtn.setGeometry(QtCore.QRect(150, 310, 141, 32))
        self.changePassBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.changePassBtn.setObjectName("changePassBtn")
        self.editBtn = QtWidgets.QPushButton(parent=self.profile_page)
        self.editBtn.setGeometry(QtCore.QRect(320, 310, 113, 32))
        self.editBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.editBtn.setObjectName("editBtn")
        self.saveBtn = QtWidgets.QPushButton(parent=self.profile_page)
        self.saveBtn.setGeometry(QtCore.QRect(460, 310, 113, 32))
        self.saveBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.saveBtn.setObjectName("saveBtn")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.profile_page)
        self.dateEdit.setGeometry(QtCore.QRect(180, 240, 110, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.surnameEdit = QtWidgets.QLineEdit(parent=self.profile_page)
        self.surnameEdit.setGeometry(QtCore.QRect(120, 60, 171, 21))
        self.surnameEdit.setText("")
        self.surnameEdit.setObjectName("surnameEdit")
        self.nameEdit = QtWidgets.QLineEdit(parent=self.profile_page)
        self.nameEdit.setGeometry(QtCore.QRect(120, 120, 171, 21))
        self.nameEdit.setObjectName("nameEdit")
        self.fatherEdit = QtWidgets.QLineEdit(parent=self.profile_page)
        self.fatherEdit.setGeometry(QtCore.QRect(120, 180, 171, 21))
        self.fatherEdit.setObjectName("fatherEdit")
        self.countEdit = QtWidgets.QLineEdit(parent=self.profile_page)
        self.countEdit.setGeometry(QtCore.QRect(490, 60, 31, 21))
        self.countEdit.setStyleSheet("border: none;")
        self.countEdit.setObjectName("countEdit")
        self.stackedWidget.addWidget(self.profile_page)
        self.Information_page = QtWidgets.QWidget()
        self.Information_page.setObjectName("Information_page")
        self.infoTextEdit = QtWidgets.QTextEdit(parent=self.Information_page)
        self.infoTextEdit.setGeometry(QtCore.QRect(10, 10, 571, 411))
        self.infoTextEdit.setReadOnly(True)
        self.infoTextEdit.setObjectName("infoTextEdit")
        self.stackedWidget.addWidget(self.Information_page)
        self.teachers_page = QtWidgets.QWidget()
        self.teachers_page.setObjectName("teachers_page")
        self.label_4 = QtWidgets.QLabel(parent=self.teachers_page)
        self.label_4.setGeometry(QtCore.QRect(160, 160, 251, 91))
        self.label_4.setStyleSheet("font-size: 30px;")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.teachers_page)
        self.schedule_page = QtWidgets.QWidget()
        self.schedule_page.setObjectName("schedule_page")
        self.label_5 = QtWidgets.QLabel(parent=self.schedule_page)
        self.label_5.setGeometry(QtCore.QRect(180, 160, 251, 91))
        self.label_5.setStyleSheet("font-size: 30px;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.schedule_page)
        self.admin_panel = QtWidgets.QWidget()
        self.admin_panel.setStyleSheet("QLabel {\n"
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
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    background: #1E95FE;\n"
"    width: 5px;\n"
"    height: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: lightgray;\n"
"    selection-color: #1E95FE;\n"
"}")
        self.admin_panel.setObjectName("admin_panel")
        self.newTeacherLable = QtWidgets.QLabel(parent=self.admin_panel)
        self.newTeacherLable.setGeometry(QtCore.QRect(40, 70, 181, 31))
        self.newTeacherLable.setObjectName("newTeacherLable")
        self.addInfoLable = QtWidgets.QLabel(parent=self.admin_panel)
        self.addInfoLable.setGeometry(QtCore.QRect(40, 140, 191, 31))
        self.addInfoLable.setObjectName("addInfoLable")
        self.addTeacherInfoLable = QtWidgets.QLabel(parent=self.admin_panel)
        self.addTeacherInfoLable.setGeometry(QtCore.QRect(40, 210, 201, 31))
        self.addTeacherInfoLable.setObjectName("addTeacherInfoLable")
        self.deleteUserLable = QtWidgets.QLabel(parent=self.admin_panel)
        self.deleteUserLable.setGeometry(QtCore.QRect(40, 280, 181, 31))
        self.deleteUserLable.setObjectName("deleteUserLable")
        self.newTeacherComboBox = QtWidgets.QComboBox(parent=self.admin_panel)
        self.newTeacherComboBox.setGeometry(QtCore.QRect(220, 70, 119, 26))
        self.newTeacherComboBox.setObjectName("newTeacherComboBox")
        self.addAdminBtn = QtWidgets.QPushButton(parent=self.admin_panel)
        self.addAdminBtn.setGeometry(QtCore.QRect(350, 60, 113, 32))
        self.addAdminBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addAdminBtn.setObjectName("addAdminBtn")
        self.removeAdminBtn = QtWidgets.QPushButton(parent=self.admin_panel)
        self.removeAdminBtn.setGeometry(QtCore.QRect(470, 60, 113, 32))
        self.removeAdminBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.removeAdminBtn.setObjectName("removeAdminBtn")
        self.addInfoBtn = QtWidgets.QPushButton(parent=self.admin_panel)
        self.addInfoBtn.setGeometry(QtCore.QRect(350, 140, 113, 32))
        self.addInfoBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addInfoBtn.setObjectName("addInfoBtn")
        self.addTeacherBtn = QtWidgets.QPushButton(parent=self.admin_panel)
        self.addTeacherBtn.setGeometry(QtCore.QRect(350, 210, 113, 32))
        self.addTeacherBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addTeacherBtn.setObjectName("addTeacherBtn")
        self.deleteUserComboBox = QtWidgets.QComboBox(parent=self.admin_panel)
        self.deleteUserComboBox.setGeometry(QtCore.QRect(220, 280, 119, 26))
        self.deleteUserComboBox.setObjectName("deleteUserComboBox")
        self.deleteUserBtn = QtWidgets.QPushButton(parent=self.admin_panel)
        self.deleteUserBtn.setGeometry(QtCore.QRect(350, 280, 113, 32))
        self.deleteUserBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.deleteUserBtn.setObjectName("deleteUserBtn")
        self.removeTeacherBtn = QtWidgets.QPushButton(parent=self.admin_panel)
        self.removeTeacherBtn.setGeometry(QtCore.QRect(470, 210, 113, 32))
        self.removeTeacherBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.removeTeacherBtn.setObjectName("removeTeacherBtn")
        self.removeInfoBtn = QtWidgets.QPushButton(parent=self.admin_panel)
        self.removeInfoBtn.setGeometry(QtCore.QRect(470, 140, 113, 32))
        self.removeInfoBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.removeInfoBtn.setObjectName("removeInfoBtn")
        self.stackedWidget.addWidget(self.admin_panel)
        self.notificationBtn = QtWidgets.QPushButton(parent=self.widget_2)
        self.notificationBtn.setGeometry(QtCore.QRect(482, 30, 121, 32))
        self.notificationBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.notificationBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background: #1E95FE;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"}")
        self.notificationBtn.setObjectName("notificationBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Картинка"))
        self.profileBtn.setText(_translate("MainWindow", "Профиль"))
        self.informationBtn.setText(_translate("MainWindow", "Информация"))
        self.teachersBtn.setText(_translate("MainWindow", "Преподаватели"))
        self.scheduleBtn.setText(_translate("MainWindow", "Расписание"))
        self.adminPanelBtn.setText(_translate("MainWindow", "Админ панель"))
        self.exitBtn.setText(_translate("MainWindow", "Выйти"))
        self.infoLable.setText(_translate("MainWindow", "Личная Информация"))
        self.surnameLable.setText(_translate("MainWindow", "Фамилия"))
        self.nameLable.setText(_translate("MainWindow", "Имя"))
        self.fatherLable.setText(_translate("MainWindow", "Отчество"))
        self.dateLable.setText(_translate("MainWindow", "Дата Рождения"))
        self.countLable.setText(_translate("MainWindow", "Количество поедок:"))
        self.changePassBtn.setText(_translate("MainWindow", "Изменить пароль"))
        self.editBtn.setText(_translate("MainWindow", "Редактировать"))
        self.saveBtn.setText(_translate("MainWindow", "Сохранить"))
        self.countEdit.setText(_translate("MainWindow", "0"))
        self.infoTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Teachers"))
        self.label_5.setText(_translate("MainWindow", "Schedule"))
        self.newTeacherLable.setText(_translate("MainWindow", "Новый преподаватель"))
        self.addInfoLable.setText(_translate("MainWindow", "Добавить информацию"))
        self.addTeacherInfoLable.setText(_translate("MainWindow", "Добавить преподавателя"))
        self.deleteUserLable.setText(_translate("MainWindow", "Удалить пользователя"))
        self.addAdminBtn.setText(_translate("MainWindow", "Назначить"))
        self.removeAdminBtn.setText(_translate("MainWindow", "Удалить"))
        self.addInfoBtn.setText(_translate("MainWindow", "Добавить"))
        self.addTeacherBtn.setText(_translate("MainWindow", "Добавить"))
        self.deleteUserBtn.setText(_translate("MainWindow", "Удалить"))
        self.removeTeacherBtn.setText(_translate("MainWindow", "Удалить"))
        self.removeInfoBtn.setText(_translate("MainWindow", "Удалить"))
        self.notificationBtn.setText(_translate("MainWindow", "Прочитать"))
        self.infoTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Скрыть вертикальную полосу прокрутки
        self.infoTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Скрыть горизонтальную полосу прокрутки
        self.infoTextEdit.setStyleSheet("""
                            QTextEdit {
                                border: none;  # Убрать границы
                                padding: 10px;  # Добавить отступы вокруг текста
                                background-color: #f0f0f0;  # Цвет фона
                                color: #333333;  # Цвет текста
                                font-size: 14px;  # Размер шрифта
                            }
                        """)
        self.adminPanelBtn.hide()
        self.nameEdit.setEnabled(False)
        self.surnameEdit.setEnabled(False)
        self.fatherEdit.setEnabled(False)
        self.dateEdit.setEnabled(False)
        self.countEdit.setEnabled(False)
