from src.controller.key_event import key_event


def menu():
    print("1 => Create Task")
    print("2 => Read Task")
    print("3 => Update Task")
    print("4 => Delete Task")
    print("5 => Exit")
    print("------------- Enter a number --------------")

    try:
        key_joined = int(input())
        key_event(key_joined)
    except Exception as e:
        print(f"\n--------------------------------")
        print("ERROR =>", e)
        print(f"--------------------------------\n")
        menu()
