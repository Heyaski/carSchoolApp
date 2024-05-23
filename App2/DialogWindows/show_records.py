import sqlite3
from PyQt6.QtWidgets import QDialog, QMessageBox
from App2.UI.show_recordsUI import Ui_Dialog
from App2.Data.logger import log_change


class showRecords(QDialog, Ui_Dialog):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.main()

    def main(self):
        self.closeBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.cancelRecord)
        self.loadRecord()

    def loadRecord(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        query_id = "SELECT id FROM users WHERE login=?"
        user_id = cur.execute(query_id, (self.username,)).fetchone()

        if user_id:
            self.user_id = user_id[0]
            query_name_teacher = """SELECT u.firstname, u.lastname 
                                    FROM users u
                                    JOIN record_info r ON u.id = r.teacher_id
                                    WHERE r.user_id=?"""
            name = cur.execute(query_name_teacher, (self.user_id,)).fetchone()
            query_datetime = """
                            SELECT date, datetime
                            FROM record_info
                            WHERE user_id=?"""
            datetime = cur.execute(query_datetime, (self.user_id,)).fetchall()
            if name:
                self.label_2.setText(f"{name[0]} {name[1]}")
                self.label.setText(f"{datetime[0][0]} в {datetime[0][1]}")
            else:
                self.label_2.setText("Учитель не найден")
        else:
            self.label_2.setText("Пользователь не найден")

        con.close()

    def cancelRecord(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        query_delete = """
                        DELETE FROM record_info WHERE user_id=?"""
        cur.execute(query_delete, (self.user_id,))
        con.commit()
        con.close()
        QMessageBox.information(self, "Успешно", "Вы отменили запись")
        log_change(self.username, "Отменил запись на занятие")
        self.accept()
