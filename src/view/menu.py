from src.controller.key_event import key_event
from src.view.messages import menu_messages, default_messages, error_messages


def menu():
    for message in menu_messages:
        print(menu_messages[message])

    try:
        print(default_messages['2'])
        key_joined = int(input(default_messages['3']))
        key_event(key_joined)

    except Exception as e:
        print(default_messages['4'])
        print(error_messages['1'], e)
        print(default_messages['4'])
