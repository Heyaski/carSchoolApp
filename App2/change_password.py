from PyQt6.QtWidgets import QDialog, QMessageBox
from App2.UI.changePassUI import Ui_Dialog
import sqlite3


class ChangePasswordDialog(QDialog, Ui_Dialog):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setupUiChange(self)
        self.main()

    def main(self):
        self.savePassBtn.clicked.connect(self.save)
        self.cancelBtn.clicked.connect(self.cancel)

    def save(self):
        newPass = self.newPassInput.text()
        rePass = self.reNewPassInput.text()

        if newPass != rePass:
            QMessageBox.information(self, "Внимание", "Пароли не совпадают")
        elif newPass == '' or rePass == '':
            QMessageBox.information(self, "Внимание", "Введите пароль")
        else:
            con = sqlite3.connect("Data/users_info.db")
            cur = con.cursor()
            update_query = """
                            UPDATE users
                            SET password = ?
                            WHERE login = ?
                        """
            cur.execute(update_query, (newPass, self.username))
            con.commit()
            con.close()
            QMessageBox.information(self, "Успех", "Пароль успешно изменён")
            self.close()

    def cancel(self):
        self.close()
