from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from datetime import *


class NewTask(QFrame):
    def __init__(self, *args, **kwargs):
        super(NewTask, self).__init__(*args, **kwargs)

        # layouts
        self.main_layout = QHBoxLayout()
        self.left_section = QVBoxLayout()
        self.right_section = QVBoxLayout()
        self.save_layout = QVBoxLayout()
        self.due_layout = QVBoxLayout()
        self.calendar_layout = QVBoxLayout()

        # widgets
        self.new_task = QLineEdit()
        self.task_desc = QTextEdit()
        self.save = QPushButton("Save")
        self.due_bar = QToolBar()
        self.today = QToolButton()
        self.tomorrow = QToolButton()
        self.menu = QMenu()
        self.calendar = QCalendarWidget()
        self.date = QToolButton()
        self.type_options = QComboBox()
        self.others = QToolBar()
        self.other = QLineEdit()
        self.add_other = QPushButton("+")

        # components
        self.add_widgets()
        self.setup()
        self.stylesheet()

    def add_widgets(self):
        self.menu.setLayout(self.calendar_layout)
        self.calendar_layout.addWidget(self.calendar)
        self.due_bar.addWidget(self.today)
        self.due_bar.addWidget(self.tomorrow)
        self.due_bar.addWidget(self.date)
        self.due_layout.addWidget(self.due_bar)
        self.others.addWidget(self.other)
        self.others.addWidget(self.add_other)
        self.save_layout.addWidget(self.save)
        self.left_section.addWidget(self.new_task)
        self.left_section.addWidget(self.task_desc)
        self.right_section.addLayout(self.save_layout)
        self.right_section.addLayout(self.due_layout)
        self.right_section.addWidget(self.type_options)
        self.right_section.addWidget(self.others)
        self.main_layout.addLayout(self.left_section)
        self.main_layout.addLayout(self.right_section)

        self.setLayout(self.main_layout)

    # setup widgets layouts
    def setup(self):
        self.other.setPlaceholderText("Add other types")
        self.due_layout.setSpacing(5)
        self.calendar_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.save_layout.setAlignment(Qt.AlignTop)
        self.calendar.setGridVisible(True)
        self.calendar.setAutoFillBackground(True)
        self.calendar.setStyleSheet("background-color: #464446;")
        self.menu.setStyleSheet("background-color: #464446;")

        # date edit
        # now = datetime.now()
        # year, month, day = now.year, now.month, now.day
        # current_date = QDate(year, month, day)
        self.calendar.selectionChanged.connect(self.__close_calendar)
        self.date.setMenu(self.menu)
        self.date.setPopupMode(QToolButton.InstantPopup)
        ############################################

        # due buttons (today, tomorrow)
        self.today.setText("Today")
        self.tomorrow.setText("Tomorrow")
        self.date.setText("No date set")
        self.today.setCheckable(True)
        self.tomorrow.setCheckable(True)
        self.date.setCheckable(True)
        self.today.setAutoExclusive(True)
        self.tomorrow.setAutoExclusive(True)
        self.date.setAutoExclusive(True)
        ############################################

        # LineEdit and TextEdit
        self.new_task.setPlaceholderText("enter your task here")
        self.task_desc.setPlaceholderText("add notes about your task")

        # task type (type_options)
        self.type_options.addItem("Personal")
        self.type_options.addItem("Project")

        # signals
        self.add_other.clicked.connect(self.__add)
        self.save.clicked.connect(self.__save)

    def stylesheet(self):
        css = """
            QLineEdit {
                background-color: #3B3B3B;
                color: white;
                min-height: 30px;
                font: 14px bold large MonoSpace;
            }
            QTextEdit {
                background-color: #3B3B3B;
                color: white;
                font: 18px bold large MonoSpace;
            }
            QPushButton {
                background-color: #3B3B3B;
                min-height: 30px;
                color: white;
                font: 18px bold large Serif;
            }
            QToolButton {
                background-color: #565456;
                min-height: 30px;
                color: white;
                font: 18px bold large Serif;
            }
            QListWidget {
                color: white;
                font: 16px bold large Serif;
            }
            QDateEdit {
                background-color: #3B3B3B;
                min-height: 30px;
                color: white;
                font: 16px bold large serif;
            }
            QComboBox {
                background-color: #3B3B3B;
                color: white;
                font: 14px bold large Serif;
                min-height: 30px;
            }
        """
        self.setStyleSheet(css)

    def __add(self):
        text = self.other.text()
        if len(text) > 0 and not text.isspace():
            self.type_options.addItem(text)
            self.type_options.setCurrentText(text)

    def __save(self):
        task = self.new_task.text()
        desc = self.task_desc.toPlainText()
        istoday = self.today.isChecked()
        istomorrow = self.tomorrow.isChecked()
        due = date.today()
        if not (istoday or istomorrow):
            due = self.date.text()
        elif istomorrow:
            due = date(due.year, due.month, due.day+1)
        print(due)

    def __close_calendar(self):
        self.date.setChecked(True)
        selected_date = self.calendar.selectedDate()
        year, month, day = selected_date.year(), selected_date.month(), selected_date.day()
        str_date = date(year, month, day)
        self.date.setText(f"{str_date}")
        self.menu.close()
