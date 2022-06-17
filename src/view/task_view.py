from src.view.messages import default_messages, describe_task_messages


def create_task():
    print(default_messages['5'])
    title = input(describe_task_messages['1'])
    description = input(describe_task_messages['2'])
    user_name = input(describe_task_messages['3'])

    return title, description, user_name


def input_read_task():
    print("\nLeer Tarea\n")
    uid = input("Ingrese el id de la tarea: ")
    print("\n_________________________________\n")
    return uid


def print_task(response):
    print("______________Tarea_________________")
    print("Title                : ", response[0])
    print("Descripción          : ", response[1])
    print("Usuario              : ", response[2])
    print("Fecha de creación    : ", response[3])
    print("Ultima actualización : ", response[4])
    print("____________________________________")


def input_update_task():
    print("Elija el campo que quiere actualizar: ")
    print("1: Titulo")
    print("2: Descripción")
    print("3: Usuario")
    print("----------------Ingrese un numero --------------")
    user_input = int(input("Dato ingresado: "))

    return user_input


def input_info(text):
    user_input = input(text + " nuevo: ")
    return user_input


def alert(text):
    print("-----------------------------")
    print(text)
    print("-----------------------------")


def print_all_task(value):
    fields = ["Titulo", "Descripción", "Usuario", "Fecha de creación", "Ultima Actualización"]

    for clave in value.items():
        print("_________________________________\n")
        print("Id: ", clave[0])
        for list_fields, list_details in zip(fields, clave[1]):
            print(list_fields, ": ", list_details)

        print("_________________________________\n")
