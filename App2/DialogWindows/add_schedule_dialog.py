import sqlite3

from App2.UI.mainUI import Ui_MainWindow
from App2.UI.addScheduleUI import Ui_Dialog
from App2.Data.logger import log_change

from PyQt6.QtCore import QDateTime, QDate
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem


class AddScheduleDialog(QDialog, Ui_Dialog, Ui_MainWindow):
    def __init__(self, main_window, username):
        super().__init__()
        self.id = None
        self.setupUi(self)

        self.main_window = main_window
        self.username = username
        self.getID()

        self.current_week_start = QDate.currentDate().addDays(
            -QDate.currentDate().dayOfWeek() + 1)

        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        self.day_combo.addItems(days_of_week)

        self.time_edit.setDisplayFormat("HH:mm")

        self.add_button.clicked.connect(self.add)

    def get_data(self):
        name = self.name_edit.text()
        day = self.day_combo.currentText()
        time = self.time_edit.time().toString("HH:mm")
        return name, day, time

    def load_schedule(self):
        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        time_slots = ["{:02d}:00".format(hour) for hour in range(9, 21)]

        self.main_window.scheduleTableWidget.setRowCount(len(time_slots))
        self.main_window.scheduleTableWidget.setColumnCount(len(days_of_week))

        dates = [(self.current_week_start.addDays(i)).toString("dd MMM") for i in range(7)]
        self.main_window.scheduleTableWidget.setHorizontalHeaderLabels(dates)
        self.main_window.scheduleTableWidget.setVerticalHeaderLabels(time_slots)

        self.main_window.scheduleTableWidget.clearContents()

        con = sqlite3.connect("Data/users_info.db")
        cur = con.cursor()
        start_date = self.current_week_start.toString("yyyy-MM-dd")
        end_date = self.current_week_start.addDays(6).toString("yyyy-MM-dd")
        cur.execute("SELECT name, datetime, day_of_week FROM schedule WHERE date BETWEEN ? AND ?",
                    (start_date, end_date))
        rows = cur.fetchall()
        con.close()

        for name, datetime_str, day_of_week in rows:
            datetime_obj = QDateTime.fromString(datetime_str, "HH:mm:ss")
            if datetime_obj.isValid():
                time_str = datetime_obj.time().toString("HH:mm")
                if time_str in time_slots:
                    time_index = time_slots.index(time_str)
                    if day_of_week >= 0 and day_of_week < 7:
                        item = QTableWidgetItem()
                        item.setBackground(QColor("green"))
                        self.main_window.scheduleTableWidget.setItem(time_index, day_of_week, item)

    def getID(self):
        con = sqlite3.connect('Data/users_info.db')
        cur = con.cursor()
        cur.execute("SELECT id FROM users WHERE login=?", (self.username,))
        self.id = [id[0] for id in cur.fetchall()]
        con.close()

    def add_schedule_to_db(self, name, day, time):
        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        day_index = days_of_week.index(day)
        date = self.current_week_start.addDays(day_index).toString("yyyy-MM-dd")

        datetime_str = f"{time}:00"

        con = sqlite3.connect("Data/users_info.db")
        cur = con.cursor()
        cur.execute("INSERT INTO schedule (name, datetime, date, day_of_week, teacher_id) VALUES (?, ?, ?, ?, ?)",
                    (name, datetime_str, date, day_index, self.id[0]))
        con.commit()
        con.close()
        log_change(self.username, 'Добавил новое расписание')
        self.load_schedule()

    def add(self):
        if self.name_edit.text() == '':
            QMessageBox.information(self, "Внимание", "Введите название занятия")
        else:
            self.accept()


