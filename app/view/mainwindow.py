from PyQt5.QtWidgets import *

import sys
from app.view.tasks import Tasks
from app.view.newtask import NewTask


class MainWindow(QMainWindow):

    __app = QApplication(sys.argv)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("ToDo")
        self.setGeometry(50, 50, 800, 400)
        todo_list = QTabWidget()

        #  Tasks content
        tasks = Tasks()
        # new task content
        new_task = NewTask()

        # adding tabs
        todo_list.addTab(tasks, "Tasks")
        todo_list.addTab(new_task, "New Task")
        todo_list.addTab(QLabel("Place for Option"), "Options")
        self.setCentralWidget(todo_list)
        self.setStyleSheet("background-color: #464446; color: white;font: 14px bold;")

    def run(self):
        self.show()
        sys.exit(self.__app.exec_())
