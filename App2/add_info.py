from PyQt6.QtWidgets import QDialog, QMessageBox,QTableWidgetItem
import sqlite3
from App2.UI.addInfoDialogUI import Ui_Dialog
from App2.UI.mainUI import Ui_MainWindow


class AddInfoDialog(QDialog, Ui_Dialog, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.cancelBtn.clicked.connect(self.close)
        self.confirmBtn.clicked.connect(self.addInformation)

    def addInformation(self):
        title = self.titleInput.text()
        text = self.infoEdit.toPlainText()

        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute("INSERT INTO information (title, text) VALUES (?, ?)", (title, text))
        con.commit()
        con.close()
        QMessageBox.information(self, "Успех", "Информация добавлена")
        self.close()

    def cancel(self):
        self.close()