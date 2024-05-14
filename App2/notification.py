import sqlite3

from PyQt6.QtWidgets import QDialog
from App2.UI.mainUI import Ui_MainWindow
from App2.UI.notificationUI import Ui_DialogNot


class Notification(QDialog, Ui_DialogNot, Ui_MainWindow):
    def __init__(self, main_window, username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.main_window = main_window
        self.cleared = None
        self.read = None
        self.main()
        self.loadNotificationText()

    def main(self):
        self.closeBtn.clicked.connect(self.close)
        self.clearBtn.clicked.connect(self.clear)

    def loadInfo(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        query_info = "SELECT read, cleared FROM users WHERE login=?"
        cur.execute(query_info, (self.username,))
        statusInfo = cur.fetchall()
        self.read = statusInfo[0][0]
        self.cleared = statusInfo[0][1]
        con.close()

    def loadNotificationText(self):
        self.loadInfo()
        con = sqlite3.connect("Data/users_info.db")
        cur = con.cursor()
        query_info = """
                            SELECT title, text
                            FROM information
                            """
        cur.execute(query_info)
        info = cur.fetchall()
        con.close()

        if self.cleared == 'no':
            for title, text in reversed(info):
                notification_text = f"<b><font size='3'>Опубликовано новое объявление.</b><br>{'-' * 50}<br><br>"
                cursor = self.notificationEdit.textCursor()
                cursor.insertHtml(notification_text)
        else:
            self.notificationEdit.setText('')

    def clear(self):
        self.notificationEdit.setText('')
        self.main_window.notificationBtn.setText('Уведомления')
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute("UPDATE users SET cleared='yes' WHERE login=?", (self.username,))
        con.commit()
        con.close()

    def read(self):
        self.notificationBtn.setText('Уведомления')

    def updateCleared(self, new_value):
        self.cleared = new_value
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        con.execute("UPDATE users SET cleared='no'")
        con.commit()
        con.close()
        self.loadNotificationText()

    def close(self):
        self.accept()