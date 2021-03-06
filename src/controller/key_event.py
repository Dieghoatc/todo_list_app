from src.controller.gen_date import gen_uuid, input_task
from src.controller.gen_date import gen_date
from src.controller.key_event_uptade_task import update_key_event
from src.controller.task import Task, Read, Delete, GetAll
from src.view.task_view import create_task, print_task, input_update_task, alert, print_all_task


def key_event(key):
    def create():
        (title, description, user_name) = create_task()
        uuid = gen_uuid()
        date = gen_date()
        date_modified = gen_date()
        task = Task(uuid, title, description, user_name, date, date_modified)
        task.set_task()
        print("______________________")

    def read():
        read_task = Read()
        read_task.uid = input_task()
        response = read_task.read_self()
        print_task(response)

    def update():
        user_input = input_update_task()
        update_key_event(user_input)

    def delete():
        delete_task = Delete()
        delete_task.uid = input_task()
        delete_task.del_self()
        alert("Tarea Eliminada")

    def get_all():
        get_all_task = GetAll()
        response = get_all_task.get_all()
        print_all_task(response)

    def error():
        print("Errorrrrrrrr")

    switch_key = {
        1: create,
        2: read,
        3: update,
        4: delete,
        5: get_all,
    }
    switch_key.get(key, error)()
