from src.controller.gen_date import input_task, gen_date
from src.controller.task import Update
from src.view.task_view import input_info


def update_key_event(key):
    def title():
        update_task = Update()
        update_task.uid = input_task()
        update_task.title = input_info("Title")
        update_task.date_modified = gen_date()
        update_task.get_title()

    def description():
        update_task = Update()
        update_task.uid = input_task()
        update_task.description = input_info("Descripción")
        update_task.date_modified = gen_date()
        get_data = update_task.get_description()
        get_data.description

    def user():
        update_task = Update()
        update_task.uid = input_task()
        update_task.user_name = input_info("Usuario")
        update_task.date_modified = gen_date()
        get_data = update_task.get_user()
        get_data.user

    def error():
        print("Errorrrrrrrr")

    switch_key_update = {
        1: title,
        2: description,
        3: user
    }
    switch_key_update.get(key, error)()
