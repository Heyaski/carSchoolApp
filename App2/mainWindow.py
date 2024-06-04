from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import QDate, QTime
from App2.UI.mainUI import Ui_MainWindow
from App2.DialogWindows.add_schedule_dialog import AddScheduleDialog
from App2.DialogWindows.change_password import ChangePasswordDialog
import sqlite3

from App2.DialogWindows.add_info import AddInfoDialog
from App2.Data.logger import log_change
from App2.DialogWindows.delete_info import deletInfoDialog
from App2.DialogWindows.notification import Notification
from App2.DialogWindows.schedule_details import ScheduleDetailsDialog
from App2.DialogWindows.show_records import showRecords
from App2.DialogWindows.schow_teacher_records import TeacherShowRecord
from App2.DialogWindows.delete_info_teacherDialog import deleteInfoTeacher


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.addScheduleDialog = AddScheduleDialog(self, self.username)
        self.adminRole = 'heyaski'
        self.login_page = None
        self.setupUi(self)
        self.main()
        self.getID()
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
        self.addScheduleBtn.clicked.connect(self.open_add_schedule_dialog)
        self.nextWeekBtn.clicked.connect(self.next_week)
        self.prevWeekBtn.clicked.connect(self.prev_week)
        self.scheduleTableWidget.cellClicked.connect(self.show_schedule_details)
        self.addScheduleDialog.load_schedule()
        self.addTeacherBtn.clicked.connect(self.openAddTeacherInfo)
        self.removeTeacherBtn.clicked.connect(self.deleteTeacherInfo)
        self.showUsersBtn.clicked.connect(self.openShowRecords)

        con = sqlite3.connect("Data/users_info.db")
        cur = con.cursor()
        query_nameInfo = """
                        SELECT firstname, lastname, fathername, date, role, read, contact
                        FROM users
                        WHERE login = ?
                        """
        cur.execute(query_nameInfo, (self.username,))
        self.nameInfo = cur.fetchall()
        if self.nameInfo[0][5] == 'yes':
            self.notificationBtn.setText('Уведомления')
        else:
            self.notificationBtn.setText('Прочитать')
        self.role = self.nameInfo[0][4]
        if self.nameInfo[0] != None:
            self.nameEdit.setText(self.nameInfo[0][0])
            self.surnameEdit.setText(self.nameInfo[0][1])
            self.fatherEdit.setText(self.nameInfo[0][2])
            self.contactEdit.setText(self.nameInfo[0][6])
            date_str = self.nameInfo[0][3]
            default_date = "01.01.2000"
            default_date = QDate.fromString(date_str, "dd.MM.yyyy")
            date = QDate.fromString(date_str, "dd.MM.yyyy")
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

        if self.role == 'teacher' or self.username == self.adminRole:
            self.addScheduleBtn.show()

    def show_schedule_details(self, row, column):
        day = self.addScheduleDialog.current_week_start.addDays(column)
        date = day.toString("yyyy-MM-dd")
        time = QTime.fromString(self.scheduleTableWidget.verticalHeaderItem(row).text(), "HH:mm")

        con = sqlite3.connect("Data/users_info.db")
        cur = con.cursor()
        query = """
            SELECT schedule.name, users.firstname || ' ' || users.lastname
            FROM schedule
            JOIN users ON schedule.teacher_id = users.id
            WHERE schedule.datetime = ? AND schedule.date = ?
        """
        cur.execute(query, (f"{time.toString('HH:mm')}:00", date))
        self.details = cur.fetchall()
        query_date = ("""SELECT schedule.datetime, schedule.date FROM schedule
                      JOIN users ON schedule.teacher_id = users.id
                      WHERE schedule.datetime = ? AND schedule.date = ?""")
        cur.execute(query_date, (f"{time.toString('HH:mm')}:00", date))
        self.date_details = cur.fetchall()
        con.close()

        dialog = ScheduleDetailsDialog(self.username, self.date_details, self.details, self)
        dialog.exec()

    def getID(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute("SELECT id FROM users WHERE login=?", (self.username,))
        self.id = cur.fetchone()[0]
        con.close()

    def open_add_schedule_dialog(self):
        if self.addScheduleDialog.exec():
            name, day, time = self.addScheduleDialog.get_data()
            self.addScheduleDialog.add_schedule_to_db(name, day, time)
            self.addScheduleDialog.load_schedule()

    def next_week(self):
        self.addScheduleDialog.current_week_start = self.addScheduleDialog.current_week_start.addDays(7)
        self.addScheduleDialog.load_schedule()

    def prev_week(self):
        self.addScheduleDialog.current_week_start = self.addScheduleDialog.current_week_start.addDays(-7)
        self.addScheduleDialog.load_schedule()

    def changeInfo(self):
        self.nameEdit.setEnabled(True)
        self.surnameEdit.setEnabled(True)
        self.fatherEdit.setEnabled(True)
        self.dateEdit.setEnabled(True)
        self.contactEdit.setEnabled(True)

    def save(self):
        self.nameEdit.setEnabled(False)
        self.surnameEdit.setEnabled(False)
        self.fatherEdit.setEnabled(False)
        self.dateEdit.setEnabled(False)
        self.contactEdit.setEnabled(False)

        new_name = self.nameEdit.text()
        surname = self.surnameEdit.text()
        fathername = self.fatherEdit.text()
        contact = self.contactEdit.text()
        date = self.dateEdit.date().toString("dd.MM.yyyy")

        con = sqlite3.connect("Data/users_info.db")
        cur = con.cursor()
        update_query = """
                           UPDATE users
                           SET firstname = ?, lastname = ?, fathername = ?, date = ?, contact=?
                           WHERE login = ?
                           """
        cur.execute(update_query, (new_name, surname, fathername, date, contact, self.username))
        con.commit()
        con.close()
        log_change("system", f'{self.username} изменил настройки профиля')

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
        cur.execute("SELECT login FROM users WHERE role='user' OR (role='teacher' AND login!=? AND login!='heyaski')",
                    (self.username,))
        users = cur.fetchall()
        for user in users:
            self.newTeacherComboBox.addItem(user[0])
            self.deleteUserComboBox.addItem(user[0])
        con.close()

    def get_teacher_info(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute("SELECT login F")

    def assignAdmin(self):
        selected_user = self.newTeacherComboBox.currentText()
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute(f"UPDATE users SET role='teacher' WHERE login='{selected_user}'")
        cur.execute(f"SELECT id, firstname, lastname, fathername FROM users WHERE login='{selected_user}'")
        teacher_info = cur.fetchall()
        cur.execute(f"INSERT INTO teachers(id, name, surname, fathername, login) VALUES(?, ?, ?, ?, ?)", (teacher_info[0][0], teacher_info[0][1], teacher_info[0][2], teacher_info[0][3], selected_user))
        con.commit()
        con.close()
        QMessageBox.information(self, 'Успех', f'Пользователь "{selected_user}" назначен преподавателем.')
        log_change(self.username, f'Пользователю {selected_user} выданы права')

    def removeAdmin(self):
        selected_user = self.newTeacherComboBox.currentText()
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute(f"UPDATE users SET role='user' WHERE login='{selected_user}'")
        cur.execute(f"DELETE FROM teachers WHERE login='{selected_user}'")
        con.commit()
        con.close()
        QMessageBox.information(self, 'Успех', f'Пользователь "{selected_user}" снят с должности преподаватель.')
        log_change(self.username, f'У пользователя {selected_user} сняты права')

    def deleteUser(self):
        selected_user = self.deleteUserComboBox.currentText()
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM users WHERE login='{selected_user}'")
        con.commit()
        con.close()
        QMessageBox.information(self, 'Успех', f'Пользователь {selected_user} удален из системы.')
        log_change(self.username, f'{selected_user} удален из системы')
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
        notification.read_notification()
        notification.exec()

    def openAddTeacherInfo(self):
        from App2.DialogWindows.add_info_teacherDialog import addTeacherInfo
        add = addTeacherInfo(self)
        add.exec()

    def deleteTeacherInfo(self):
        delete = deleteInfoTeacher()
        delete.exec()

    def openShowRecords(self):
        if self.role == "user":
            showRecord = showRecords(self.username)
            showRecord.exec()
        else:
            teacherRecord = TeacherShowRecord(self.id)
            teacherRecord.exec()

    def logout(self):
        self.close()
        log_change(self.username, "Вышел из системы")
        from login_page import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()
