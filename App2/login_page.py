from PyQt6.QtWidgets import QWidget, QMessageBox
from mainWindow import mainWindow
from registration_page import RegistrationPage
from App2.UI.login_pageUI import Ui_Form
from App2.Data.logger import log_change
import sqlite3
import sys
import bcrypt

class LoginPage(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.personalCabinet = None  # Добавляем атрибут personalCabinet
        self.registration_page = None
        self.cabinet = None
        self.setupUi(self)

        self.loadUI()

    def loadUI(self):
        self.setWindowTitle("Вход")
        self.logBtn.clicked.connect(self.login)
        self.createAccBtn.clicked.connect(self.reg)
        self.exitBtn.clicked.connect(self.exit)

    def login(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()

        loginIn = self.loginInput.text()
        passwordIn = self.passInput.text()

        query_userInfo = """
                        SELECT login, password, id
                        FROM users           
                        """
        cur.execute(query_userInfo)
        user_info = {row[0]: row[1] for row in cur.fetchall()}

        if loginIn in user_info and bcrypt.checkpw(passwordIn.encode('utf-8'), user_info[loginIn].encode('utf-8')):
            self.close()  # Скрываем окно авторизации
            self.personalCabinet = mainWindow(loginIn)  # Создаем объект personalCabinet и сохраняем его как атрибут
            self.personalCabinet.show()  # Показываем окно личного кабинета
            log_change(loginIn, "Вошел в систему")
        else:
            QMessageBox.information(self, "Внимание", "Логин или пароль введены неверно!")
            log_change("system", f"Неудачная попытка входа в аккаунт {loginIn}")

        con.commit()
        con.close()

    def reg(self):
        self.close()
        self.registration_page = RegistrationPage()
        self.registration_page.show()

    def exit(self):
        sys.exit()