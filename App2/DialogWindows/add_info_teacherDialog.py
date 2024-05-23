import sqlite3
from App2.UI.add_info_teacherUI import Ui_dialog
from PyQt6.QtWidgets import QMessageBox, QDialog
from App2.UI.mainUI import Ui_MainWindow
from App2.Data.logger import log_change

class addTeacherInfo(QDialog, Ui_dialog, Ui_MainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main()
        self.main_window = main_window
        self.loadTeacherInfo()

    def main(self):
        self.addBtn.clicked.connect(self.add_info_to_db)
        self.cancelBtn.clicked.connect(self.accept)

    def loadTeacherInfo(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        query = "SELECT login FROM teachers"
        teachers = cur.execute(query)
        for teacher in teachers:
            self.addTeacherComboBox.addItem(teacher[0])
        con.close()

    def add_info_to_db(self):
        selected_user = self.addTeacherComboBox.currentText()
        expirience = self.ExpirienceEdit.text()
        info = self.shorInfoEdit.toPlainText()
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        query_select = "SELECT id, login FROM teachers WHERE login=?"
        id = cur.execute(query_select, (selected_user,)).fetchall()
        query_update = "INSERT INTO teachers_info(id, login, expirience, info) VALUES(?, ?, ?, ?)"
        cur.execute(query_update, (id[0][0], selected_user, expirience, info))
        con.commit()
        con.close()
        QMessageBox.information(self, "Успешно", "Информация о перподавателе добавлена")
        log_change("system", f"Информация о преподавателе {selected_user} добавлена на страницу")
        self.accept()

    def addInfo(self):
        pass