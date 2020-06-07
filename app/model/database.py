from app.model import DATABASE_PATH

import sqlite3

global __DB


class Database:

    @staticmethod
    def __connect():
        try:
            global __DB
            __DB = sqlite3.connect("tasks.db")
            __DB.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, "
                         "description TEXT, due TEXT, label TEXT)")
            print("Database is connected successfully")
        except sqlite3.DatabaseError as e:
            raise Exception("Can't connect to db")

    @staticmethod
    def __disconnect():
        global __DB
        if __DB:
            __DB.close()
            print("Database is disconnected")

    # finished
    @staticmethod
    def add_task(name, description, due, label):
        Database.__connect()
        statement = "INSERT INTO tasks(task, description, due, label) VALUES(?,?,?,?)"
        global __DB
        __DB.execute(statement, (name, description, due, label))
        __DB.commit()
        print("Task is added successfully")
        Database.__disconnect()

    def update_task(self, old_id, new_name, new_description, new_due, new_label):
        pass

    @staticmethod
    def delete_task(id_):
        Database.__connect()
        statement = f"DELETE FROM tasks WHERE id={id_}"
        global __DB
        __DB.execute(statement)
        __DB.commit()
        Database.__disconnect()

    @staticmethod
    def load_tasks():
        Database.__connect()
        statement = "SELECT * FROM tasks"
        global __DB
        __DB.row_factory = sqlite3.Row
        result = __DB.execute(statement)
        Database.__disconnect()
        return result
