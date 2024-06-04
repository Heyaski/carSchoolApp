import sqlite3

from PyQt6.QtWidgets import QMessageBox, QDialog

from App2.UI.delete_info_teacherUI import Ui_Dialog
from App2.Data.logger import log_change


class deleteInfoTeacher(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.loadTeacherInfo()
        self.cancelBtn.clicked.connect(self.accept)
        self.deleteBtn.clicked.connect(self.delete)

    def loadTeacherInfo(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        query = "SELECT login FROM teachers_info"
        teachers = cur.execute(query)
        for teacher in teachers:
            self.selectTeacherComboBox.addItem(teacher[0])
        con.close()

    def delete(self):
        selected_teacher = self.selectTeacherComboBox.currentText()
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute("DELETE FROM teachers_info WHERE login=?", (selected_teacher,))
        con.commit()
        con.close()
        QMessageBox.information(self, "Успешно", "Вы удалили информацию о преподавателе со странице")
        log_change("system", f'Информация о преподавателе {selected_teacher} удалена со страницы')
        self.accept()