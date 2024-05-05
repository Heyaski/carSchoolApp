import sys
from PyQt6.QtWidgets import QApplication
from login_page import LoginPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    logPage = LoginPage()
    logPage.show()
    sys.exit(app.exec())
