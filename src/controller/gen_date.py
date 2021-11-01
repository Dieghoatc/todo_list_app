import datetime
import uuid

from src.view.task_view import input_read_task


def gen_uuid():
    return uuid.uuid4().hex


def gen_date():
    t = datetime.time(1, 2, 3)
    d = datetime.date.today()
    date = str(datetime.datetime.combine(d, t))
    return date


def input_task():
    (uid) = input_read_task()
    return uid