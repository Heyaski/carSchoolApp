from PyQt6.QtWidgets import QWidget, QMessageBox
from mainWindow import PersonalCabinet
from registration_page import RegistrationPage
from App2.UI.login_pageUI import Ui_Form
import sqlite3, sys

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
                        SELECT login, password, role
                        FROM users           
                        """
        cur.execute(query_userInfo)
        user_info = {row[0]: row[1] for row in cur.fetchall()}

        if loginIn in user_info and passwordIn == user_info[loginIn]:
            self.close()  # Скрываем окно авторизации
            self.personalCabinet = PersonalCabinet(loginIn)  # Создаем объект personalCabinet и сохраняем его как атрибут
            self.personalCabinet.show()  # Показываем окно личного кабинета
        else:
            QMessageBox.information(self, "Внимание", "Логин или пароль введены неверно!")

        con.commit()
        con.close()

    def reg(self):
        self.close()
        self.registation_page = RegistrationPage()
        self.registation_page.show()

    def exit(self):
        sys.exit()
