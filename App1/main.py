import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.user_info = {}
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 450, 500)
        self.setWindowTitle('Авторизация')

        self.login_name = QLabel('Введите логин', self)
        self.login_name.move(30, 150)

        self.password_name = QLabel("Введите пароль", self)
        self.password_name.move(30, 180)

        self.login_input = QLineEdit(self)
        self.login_input.resize(80, 20)
        self.login_input.move(140, 147)

        self.password_input = QLineEdit(self)
        self.password_input.resize(100, 20)
        self.password_input.move(140, 177)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.logBtn = QPushButton("Войти", self)
        self.logBtn.move(190, 220)
        self.logBtn.clicked.connect(self.login)

    def login(self):
        self.connection()
        login = self.login_input.text()
        password = self.password_input.text()

        if login in self.user_info and self.user_info[login][0] == int(password):
            user_role = self.user_info[login][1]
            self.close()
            self.openUserInfoWindow(login, user_role)
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль.')

    def connection(self):
        con = sqlite3.connect('Data/info_users.db')
        cur = con.cursor()

        query = """
                    SELECT login, password, role
                    FROM users
                    """
        cur.execute(query)

        self.user_info = {login: (password, role) for login, password, role in cur.fetchall()}

        con.close()

    def openUserInfoWindow(self, login, role):
        self.user_info_window = UserInfoWindow(login, role)
        self.user_info_window.show()


class UserInfoWindow(QWidget):
    def __init__(self, login, role):
        super().__init__()
        self.login = login
        self.role = role
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 450, 200)
        self.setWindowTitle('Информация о пользователе')

        self.login_label = QLabel(f'Логин: {self.login}', self)
        self.login_label.move(30, 30)

        self.role_label = QLabel(f'Роль: {self.role}', self)
        self.role_label.move(30, 60)

        if self.role == 'admin':
            self.user_list = QComboBox(self)
            self.user_list.move(30, 90)
            self.loadUserList()

            self.assignBtn = QPushButton('Назначить админом', self)
            self.assignBtn.move(200, 90)
            self.assignBtn.clicked.connect(self.assignAdmin)

            self.removeBtn = QPushButton('Убрать админку', self)
            self.removeBtn.move(200, 120)
            self.removeBtn.clicked.connect(self.removeAdmin)

        self.changeAccountBtn = QPushButton('Сменить аккаунт', self)
        self.changeAccountBtn.move(30, 150)
        self.changeAccountBtn.clicked.connect(self.changeAccount)

        self.exitBtn = QPushButton('Выйти', self)
        self.exitBtn.move(200, 150)
        self.exitBtn.clicked.connect(self.exit)

    def loadUserList(self):
        con = sqlite3.connect('Data/info_users.db')
        cur = con.cursor()
        cur.execute("SELECT login FROM users WHERE role='user' OR (role='admin' AND login!=? AND login!='stepan')", (self.login,))
        users = cur.fetchall()
        for user in users:
            self.user_list.addItem(user[0])
        con.close()

    def assignAdmin(self):
        selected_user = self.user_list.currentText()
        con = sqlite3.connect('Data/info_users.db')
        cur = con.cursor()
        cur.execute(f"UPDATE users SET role='admin' WHERE login='{selected_user}'")
        con.commit()
        con.close()
        QMessageBox.information(self, 'Успех', f'Пользователь {selected_user} назначен администратором.')

    def removeAdmin(self):
        selected_user = self.user_list.currentText()
        con = sqlite3.connect('Data/info_users.db')
        cur = con.cursor()
        cur.execute(f"UPDATE users SET role='user' WHERE login='{selected_user}'")
        con.commit()
        con.close()
        QMessageBox.information(self, 'Успех', f'Администраторские права у пользователя {selected_user} сняты.')

    def changeAccount(self):
        self.close()
        login_window = LoginWindow()
        login_window.show()

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
