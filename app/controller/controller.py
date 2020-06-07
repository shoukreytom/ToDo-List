from app.model import database


class Controller:

    # finished
    @staticmethod
    def add_task(model):
        name = model.get_name()
        description = model.get_description()
        due = model.get_due()
        label = model.get_type()
        database.Database.connect()
        database.Database.add_task(name, description, due, label)
        database.Database.disconnect()

    def delete_task(self):
        pass

    def edit_task(self):
        pass

    def load_tasks(self):
        pass
