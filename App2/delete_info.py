import sqlite3

from PyQt6.QtWidgets import QDialog, QMessageBox
from App2.UI.deleteInfoDialogUI import Ui_DialogDelete
from App2.logger import log_change


class deletInfoDialog(QDialog, Ui_DialogDelete):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.loadTitle()
        self.cancelBtn.clicked.connect(self.close)
        self.deleteBtn.clicked.connect(self.delete)

    def delete(self):
        selected_title = self.titleComboBox.currentText()
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM information WHERE title='{selected_title}'")
        con.commit()
        con.close()
        QMessageBox.information(self, 'Успех', f'Новость "{selected_title}" удалена из системы')
        log_change("heyaski", f'Новость {selected_title} удалена из системы')
        self.accept()

    def loadTitle(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute("SELECT title FROM information")
        infos = cur.fetchall()
        for info in infos:
            self.titleComboBox.addItem(info[0])
        con.close()

    def close(self):
        self.accept()
