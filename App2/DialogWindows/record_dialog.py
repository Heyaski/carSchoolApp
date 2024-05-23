import sqlite3

from PyQt6.QtWidgets import QDialog, QMessageBox
from App2.UI.record_dialogUI import Ui_Dialog
from App2.Data.logger import log_change

class recordDialog(QDialog, Ui_Dialog):
    def __init__(self, date_details, details, username):
        super().__init__()
        self.setupUi(self)
        self.main()
        self.details = details
        self.date_details = date_details
        self.loadTeacherList()
        self.username = username

    def main(self):
        self.cancelBtn.clicked.connect(self.accept)
        self.recordBtn.clicked.connect(self.record)

    def loadTeacherList(self):
        for detail in self.details:
            self.name, self.teacher = detail
            self.teacherComboBox.addItem(self.teacher)

    def record(self):
        selected_teacher = self.teacherComboBox.currentText().split(' ')
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        query_id = "SELECT id FROM users WHERE login=?"
        user_id = cur.execute(query_id, (self.username,)).fetchall()
        query_tId = "SELECT id FROM teachers WHERE surname=?"
        teacher_id = cur.execute(query_tId, (selected_teacher[1],)).fetchall()
        query_record = "INSERT INTO record_info(user_id, teacher_id, date, datetime) VALUES(?, ?, ?, ?)"
        cur.execute(query_record, (user_id[0][0], teacher_id[0][0], self.date_details[0][1], self.date_details[0][0]))
        con.commit()
        con.close()
        QMessageBox.information(self, "Успешно", f"Вы успешно записались на занятие {self.date_details[0][1]} в {self.date_details[0][0]}")
        log_change(self.username, f"Записался на занятие к {self.teacher}")
        self.accept()


