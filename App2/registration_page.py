import sys
from PyQt6.QtWidgets import QWidget, QMessageBox
import sqlite3
from App2.UI.registationUI import Ui_Form
from App2.Data.logger import log_change


class RegistrationPage(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.login_page = None
        self.setupUi(self)

        self.loadUI()

    def loadUI(self):
        self.setWindowTitle("Регистрация")
        self.regBtn.clicked.connect(self.registration)
        self.exitBtn.clicked.connect(self.exit)
        self.inputBtn.clicked.connect(self.login)

    def registration(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()

        login = self.loginInput.text()
        password = self.passInput.text()
        query_login = """
                        SELECT login
                        FROM users           
                        """
        cur.execute(query_login)
        logins = [login[0] for login in cur.fetchall()]

        if self.passInput.text() != self.rePassInput.text():
            QMessageBox.information(self, 'Внимание', 'Пароли не совпадают!')
        elif self.loginInput.text() == '':
            QMessageBox.information(self, "Внимание", "Введите логин!")
        elif self.passInput.text() == '':
            QMessageBox.information(self, 'Внимание', "Введите пароль!")
        elif self.loginInput.text() in logins:
            QMessageBox.information(self, 'Внимание', 'Логин уже используется!')
        else:
            insert = f"""
                    INSERT INTO users(login, password, role)
                    VALUES('{login}', '{password}', 'user')
                    """
            cur.execute(insert)
            self.loginInput.setText('')
            self.passInput.setText('')
            self.rePassInput.setText('')
            QMessageBox.information(self, 'Поздравляем', "Аккаунт успешно создан!")
            log_change("system", f'Зарегестрирован новый пользователь: {login}')
            self.close()
            from login_page import LoginPage
            self.login_page = LoginPage()
            self.login_page.show()

        con.commit()
        con.close()

    def login(self):
        self.close()
        from login_page import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()


    def exit(self):
        sys.exit()
