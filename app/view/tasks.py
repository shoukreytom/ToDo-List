from PyQt5.QtWidgets import *

from app.model.taskmodel import TaskModel


class Tasks(QSplitter):

    items = dict()

    def __init__(self):
        super(Tasks, self).__init__()
        # Layouts
        self.__left_section = QFrame()
        self.__right_section = QFrame()
        self.__left_layout = QVBoxLayout()
        self.__right_layout = QFormLayout()
        self.__buttons_layout = QHBoxLayout()

        # Widgets
        self.__tasks = QListWidget()
        self.__task_f = QLineEdit()
        self.__desc_f = QTextEdit()
        self.__due = QLineEdit()
        self.__delete = QPushButton("Delete")
        self.__edit = QPushButton("Edit")

        #  components
        self.add_widgets()
        self.stylesheet()
        self.add_items_list()
        self.setup()

    def add_widgets(self):
        self.__buttons_layout.addWidget(self.__delete)
        self.__buttons_layout.addWidget(self.__edit)

        self.__left_layout.addWidget(self.__tasks)
        self.__right_layout.addRow(self.__task_f)
        self.__right_layout.addRow(self.__desc_f)
        self.__right_layout.addRow(self.__due)
        self.__right_layout.addItem(self.__buttons_layout)

        self.__left_section.setLayout(self.__left_layout)
        self.__right_section.setLayout(self.__right_layout)

        # adding sections to the main layout
        self.addWidget(self.__left_section)
        self.addWidget(self.__right_section)

    def stylesheet(self):
        css = """
            QLineEdit {
                background-color: #3B3B3B;
                color: white;
                min-height: 30px;
                font: 16px bold large MonoSpace;
            }
            QTextEdit {
                background-color: #3B3B3B;
                color: white;
                font: 20px bold large MonoSpace;
            }
            QPushButton {
                background-color: #3B3B3B;
                min-height: 30px;
                color: white;
                font: 18px bold large Serif;
            }
        """
        self.setStyleSheet(css)

    def add_items_list(self):
        item1 = TaskModel("NPM", "No More Pornography", "2/5/2020", None)
        item2 = TaskModel("ToDo", "ToDo List app", "5/6/2020", None)
        self.items[f"{item1.get_name()}"] = item1
        self.items[f"{item2.get_name()}"] = item2
        self.__tasks.addItems(self.items.keys())
        self.__tasks.setSelectionMode(QListWidget.SingleSelection)
        self.__tasks.clicked.connect(self.item_changed)

    def item_changed(self):
        self.__tasks.currentItem()
        sender = self.sender()
        item = self.items[sender.currentItem().text()]
        self.__task_f.setText(item.get_name())
        self.__desc_f.setText(item.get_description())
        self.__due.setText(f"Due: {item.get_due()}")

    def setup(self):
        #   Frames
        self.__right_section.setFrameShape(QFrame.Panel)
        self.__right_section.setFrameShadow(QFrame.Sunken)
        self.__left_section.setFrameShape(QFrame.Panel)
        self.__left_section.setFrameShadow(QFrame.Sunken)
        #################################################
        #   LineEdit and TextEdit
        self.__task_f.setReadOnly(True)
        self.__desc_f.setReadOnly(True)
        self.__due.setReadOnly(True)
