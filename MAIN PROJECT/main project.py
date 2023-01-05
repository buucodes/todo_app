import time

from functions import get_todos, write_todos
import datetime

now = time.strftime("%b %d, %Y %I:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip(),

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}--{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos("todos.txt")

            new_item = input("What do you want the new item to be?: ")
            todos[number] = new_item + '\n'

            write_todos(todos)


        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            completed_item = int(user_action[9:])

            todos = get_todos("todos.txt")

            index = completed_item - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Item does not exist")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid!")

print("Thank you! All done!")