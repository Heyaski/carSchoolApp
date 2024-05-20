from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class ScheduleDetailsDialog(QDialog):
    def __init__(self, details, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Детали занятия")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        if not details:
            label = QLabel("Занятий нет")
            layout.addWidget(label)
        else:
            for detail in details:
                name, teacher = detail
                layout.addWidget(QLabel(f"Занятие: {name}"))
                layout.addWidget(QLabel(f"Преподаватель: {teacher}"))

        close_button = QPushButton("Закрыть")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

        self.setLayout(layout)