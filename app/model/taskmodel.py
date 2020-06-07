class TaskModel:

    def __init__(self, name, description, due, label):
        self.__name = str(name)
        self.__description = str(description)
        self.__due = str(due)
        self.__label = str(label)

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_due(self):
        return self.__due

    def get_type(self):
        return self.__label

    def __repr__(self) -> str:
        return self.__name


