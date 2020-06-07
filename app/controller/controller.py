from app.model import database


global __tasks


class Controller:

    # finished
    @staticmethod
    def add_task(model):
        name = model.get_name()
        description = model.get_description()
        due = model.get_due()
        label = model.get_type()
        database.Database.add_task(name, description, due, label)
        Controller.refresh()

    @staticmethod
    def delete_task(id_):
        database.Database.delete_task(id_)
        Controller.refresh()

    def edit_task(self):
        pass

    @staticmethod
    def load_tasks():
        storage = dict()
        tasks = database.Database.load_tasks()
        for task in tasks:
            storage[f"{task.get_name()}"] = task
        return storage

    @staticmethod
    def refresh():
        global __tasks
        if __tasks:
            __tasks.clear()
            items = Controller.load_tasks()
            __tasks.addItems(items.keys())

    @staticmethod
    def set_list(list_widget):
        global __tasks
        __tasks = list_widget
