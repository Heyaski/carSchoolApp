import sqlite3

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt6.QtWidgets import QAbstractItemView
from App2.UI.teacher_show_recordUI import Ui_Dialog

class TeacherShowRecord(QDialog, Ui_Dialog):
    def __init__(self, teacher_id):
        super().__init__()
        self.setupUi(self)
        self.teacher_id = teacher_id
        self.main()

    def main(self):
        self.closeBtn.clicked.connect(self.accept)
        self.loadUsersRecord()

    def loadUsersRecord(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        query = """SELECT u.firstname, u.lastname, u.contact, r.date, r.datetime 
                   FROM users u
                   JOIN record_info r ON u.id = r.user_id
                   WHERE r.teacher_id=?"""
        results = cur.execute(query, (self.teacher_id,)).fetchall()
        con.close()

        self.teacherShowRecorTableWidget.setRowCount(len(results))
        self.teacherShowRecorTableWidget.setColumnCount(5)
        self.teacherShowRecorTableWidget.setHorizontalHeaderLabels(["Имя", "Фамилия", "Контакты", "Дата", "Время"])
        self.teacherShowRecorTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        for row_idx, row_data in enumerate(results):
            for col_idx, data in enumerate(row_data):
                item = QTableWidgetItem(data)
                self.teacherShowRecorTableWidget.setItem(row_idx, col_idx, item)

    def showUsersRecord(self):
        self.loadUsersRecord()
        self.exec()
