from app.model import database

import sqlite3


class Controller:

    def add_task(self, model):
        name = model.get_name()
        description = model.get_description()
        due = model.get_due()
        label = model.get_type()

    def delete_task(self):
        pass

    def edit_task(self):
        pass

    def load_tasks(self):
        pass
