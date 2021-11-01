from src.db import db
from src.model.task_model import TaskModel


class Task:
    uid = TaskModel.uid
    title = TaskModel.title
    description = TaskModel.description
    user_name = TaskModel.user_name
    date = TaskModel.date
    date_modified = TaskModel.date_modified

    def __init__(self, uid, title, description, user_name, date, date_modified):
        self.uid = uid
        self.title = title
        self.description = description
        self.user_name = user_name
        self.date = date
        self.date_modified = date_modified

    def set_task(self):
        db[self.uid] = [self.title, self.description, self.user_name, self.date, self.date_modified]
        print(db)


class Read:
    def read_self(self):
        return db.get(self.uid)


class Update:
    def get_title(self):
        db[self.uid][0] = self.title
        db[self.uid][4] = self.date_modified

    def get_description(self):
        db[self.uid][1] = self.description
        db[self.uid][4] = self.date_modified

    def get_user(self):
        db[self.uid][2] = self.user_name
        db[self.uid][4] = self.date_modified


class Delete:
    def del_self(self):
        del (db[self.uid])


class GetAll:
    def get_all(self):
        return db
