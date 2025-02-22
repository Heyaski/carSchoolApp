from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel
from App2.UI.shedule_detailsUI import Ui_Dialog
from App2.DialogWindows.record_dialog import recordDialog

class ScheduleDetailsDialog(QDialog, Ui_Dialog):
    def __init__(self, username, date_details, details, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setupUi(self)
        self.details = details
        self.username = username
        self.date_details = date_details



        if not self.details:
            label = QLabel("Занятий нет")
            layout.addWidget(label)
        else:
            for detail in self.details:
                self.name, self.teacher = detail
                layout.addWidget(QLabel(f"Занятие: {self.name}"))
                layout.addWidget(QLabel(f"Преподаватель: {self.teacher}"))

        self.setLayout(layout)
        self.closeBtn.clicked.connect(self.accept)
        self.recordBtn.clicked.connect(self.record)
        layout.addWidget(self.recordBtn)
        layout.addWidget(self.closeBtn)



    def record(self):
        self.accept()
        rec = recordDialog(self.date_details, self.details, self.username)
        rec.exec()

