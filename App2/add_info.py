from PyQt6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
import sqlite3
from App2.UI.addInfoDialogUI import Ui_Dialog
from App2.UI.mainUI import Ui_MainWindow
from notification import Notification


class AddInfoDialog(QDialog, Ui_Dialog, Ui_MainWindow):
    def __init__(self, main_window, username):
        super().__init__()
        self.setupUi(self)
        self.main()
        self.username = username
        self.main_window = main_window

    def main(self):
        self.cancelBtn.clicked.connect(self.close)
        self.confirmBtn.clicked.connect(self.addInformation)

    def addInformation(self):
        title = self.titleInput.text()
        text = self.infoEdit.toPlainText()

        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()

        cur.execute("SELECT title FROM information")
        checkTitle = [tle[0] for tle in cur.fetchall()]

        if title in checkTitle:
            QMessageBox.information(self, "Ошибка", "Новость с таким заголовком уже опубликована.")
        else:
            cur.execute("INSERT INTO information (title, text) VALUES (?, ?)", (title, text))
            con.commit()
            QMessageBox.information(self, "Успех", "Информация добавлена")
            self.accept()
            add = Notification(main_window=self, username=self.username)
            add.updateCleared('yes')
            self.main_window.notificationBtn.setText('Прочтиать')
        con.close()

    def loadInfoText(self):
        con = sqlite3.connect("Data/users_info.db")
        cur = con.cursor()
        query_info = """
                    SELECT title, text
                    FROM information
                    """
        cur.execute(query_info)
        info = cur.fetchall()
        con.close()

        for title, text in reversed(info):
            formatted_text = f"<b><font size='4'>{title}</font></b><br><br>{text}<br>{'-' * 93}<br><br>"
            cursor = self.main_window.infoTextEdit.textCursor()
            cursor.insertHtml(formatted_text)

    def close(self):
        self.accept()
