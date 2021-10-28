from src.db import db
from src.model.task_model import TaskModel


class Task:
    # uid = TaskModel.uid
    # title = TaskModel.title
    # description = TaskModel.description
    # user_name = TaskModel.user_name

    def __init__(self, uid, title, description, user_name):
        self.uid = uid
        self.title = title
        self.description = description
        self.user_name = user_name

    def getTask(self):
        db[self.uid] = [self.title, self.description, self.user_name]
        print(db)


