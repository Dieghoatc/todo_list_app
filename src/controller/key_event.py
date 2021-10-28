from src.view import menu
from src.controller.task import Task
import uuid
from src.view.create_task_view import create_task


def key_event(key):
    def create():
        (title, description, user_name) = create_task()
        task = Task(uuid.uuid4().hex, title, description, user_name)
        task.getTask()
        print("______________________")
        menu()

    def read():
        #read_task()
        print("read")

    def update():
        #update_task()
        print("update")

    def delete():
        #delete_task()
        print("delete")

    def error():
        print("Errorrrrrrrr")

    switch_key = {
        1: create,
        2: read,
        3: update,
        4: delete,
    }
    switch_key.get(key, error)()
