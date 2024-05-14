from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QDialog, QTableWidgetItem
from PyQt6.QtCore import QDate, QTimer
from PyQt6.uic.properties import QtGui

from App2.UI.mainUI import Ui_MainWindow
from delete_info import deletInfoDialog
from add_info import AddInfoDialog
from change_password import ChangePasswordDialog  # Подключаем UI для диалогового окна
from notification import Notification
import sqlite3


class PersonalCabinet(QMainWindow, Ui_MainWindow):
    def __init__(self, username):
        super().__init__()

        self.username = username
        self.login_page = None
        self.setupUi(self)
        self.main()
        self.setWindowTitle("Ехай")
        self.setFixedSize(864, 557)

    def main(self):
        self.exitBtn.clicked.connect(self.logout)
        self.profileBtn.clicked.connect(self.showProfile)
        self.scheduleBtn.clicked.connect(self.showSchedule)
        self.informationBtn.clicked.connect(self.showInfo)
        self.teachersBtn.clicked.connect(self.showTeacher)
        self.adminPanelBtn.clicked.connect(self.showAdmin)
        self.changePassBtn.clicked.connect(self.changePass)
        self.saveBtn.clicked.connect(self.save)
        self.editBtn.clicked.connect(self.changeInfo)
        self.notificationBtn.clicked.connect(self.openNotification)

        con = sqlite3.connect("Data/users_info.db")
        cur = con.cursor()
        query_nameInfo = """
                        SELECT firstname, lastname, fathername, date, role, cleared
                        FROM users
                        WHERE login = ?
                        """
        cur.execute(query_nameInfo, (self.username,))
        nameInfo = cur.fetchall()
        if nameInfo[0][5] == 'yes':
            self.notificationBtn.setText('Уведомления')
        else:
            self.notificationBtn.setText('Прочитать')
        self.role = nameInfo[0][4]
        if nameInfo[0] != None:
            self.nameEdit.setText(nameInfo[0][0])
            self.surnameEdit.setText(nameInfo[0][1])
            self.fatherEdit.setText(nameInfo[0][2])
            date_str = nameInfo[0][3]
            default_date = "01.01.2000"
            default_date = QDate.fromString(date_str,
                                            "dd.MM.yyyy")
            date = QDate.fromString(date_str,
                                    "dd.MM.yyyy")
            if date.isValid():
                self.dateEdit.setDate(date)
            else:
                self.dateEdit.setDate(default_date)
        else:
            self.nameEdit.setText('')
            self.surnameEdit.setText('')
            self.fatherEdit.setText('')

        if self.role == 'admin':
            self.adminPanelBtn.show()
            self.loadUserList()
            self.adminPanel()

    def changeInfo(self):
        self.nameEdit.setEnabled(True)
        self.surnameEdit.setEnabled(True)
        self.fatherEdit.setEnabled(True)
        self.dateEdit.setEnabled(True)

    def save(self):
        self.nameEdit.setEnabled(False)
        self.surnameEdit.setEnabled(False)
        self.fatherEdit.setEnabled(False)
        self.dateEdit.setEnabled(False)

        new_name = self.nameEdit.text()
        surname = self.surnameEdit.text()
        fathername = self.fatherEdit.text()
        date = self.dateEdit.date().toString("dd.MM.yyyy")

        con = sqlite3.connect("Data/users_info.db")
        cur = con.cursor()
        update_query = """
                           UPDATE users
                           SET firstname = ?, lastname = ?, fathername = ?, date = ?
                           WHERE login = ?
                           """
        cur.execute(update_query, (new_name, surname, fathername, date, self.username))
        con.commit()
        con.close()

    def loadInfo(self):
        con = sqlite3.connect("Data/users_info.db")
        cur = con.cursor()
        query_info = """
                    SELECT firstname, lastname, fathername, password, date, role
                    FROM users
                    """
        cur.execute(query_info)
        self.usInfo = cur.fetchall()
        con.close()

    def showProfile(self):
        self.stackedWidget.setCurrentIndex(0)

    def showSchedule(self):
        self.stackedWidget.setCurrentIndex(3)

    def showInfo(self):
        self.stackedWidget.setCurrentIndex(1)
        self.infoTextEdit.clear()
        load = AddInfoDialog(self, self.username)
        load.loadInfoText()

    def showTeacher(self):
        self.stackedWidget.setCurrentIndex(2)

    def showAdmin(self):
        self.stackedWidget.setCurrentIndex(4)

    def adminPanel(self):
        self.addAdminBtn.clicked.connect(self.assignAdmin)
        self.removeAdminBtn.clicked.connect(self.removeAdmin)
        self.deleteUserBtn.clicked.connect(self.deleteUser)
        self.addInfoBtn.clicked.connect(self.addInfo)
        self.removeInfoBtn.clicked.connect(self.deleteInfo)

    def loadUserList(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute("SELECT login FROM users WHERE role='user' OR (role='admin' AND login!=? AND login!='heyaski')",
                    (self.username,))
        users = cur.fetchall()
        for user in users:
            self.newTeacherComboBox.addItem(user[0])
            self.deleteUserComboBox.addItem(user[0])
        con.close()

    def assignAdmin(self):
        selected_user = self.newTeacherComboBox.currentText()
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute(f"UPDATE users SET role='admin' WHERE login='{selected_user}'")
        con.commit()
        con.close()
        QMessageBox.information(self, 'Успех', f'Пользователь "{selected_user}" назначен администратором.')

    def removeAdmin(self):
        selected_user = self.newTeacherComboBox.currentText()
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute(f"UPDATE users SET role='user' WHERE login='{selected_user}'")
        con.commit()
        con.close()
        QMessageBox.information(self, 'Успех', f'Администраторские права у пользователя "{selected_user}" сняты.')

    def deleteUser(self):
        selected_user = self.deleteUserComboBox.currentText()
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM users WHERE login='{selected_user}'")
        con.commit()
        con.close()
        QMessageBox.information(self, 'Успех', f'Пользователь {selected_user} удален из системы.')
        self.deleteUserComboBox.removeItem(self.deleteUserComboBox.findText(selected_user))
        self.newTeacherComboBox.removeItem(self.newTeacherComboBox.findText(selected_user))

    def changePass(self):
        change_password_dialog = ChangePasswordDialog(self.username)
        change_password_dialog.exec()

    def addInfo(self):
        add_info = AddInfoDialog(self, self.username)
        add_info.exec()

    def deleteInfo(self):
        delete_info = deletInfoDialog()
        delete_info.exec()

    def openNotification(self):
        notification = Notification(self, self.username)
        self.notificationBtn.setText('Уведомления')
        notification.exec()

    def logout(self):
        self.close()
        from login_page import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()
