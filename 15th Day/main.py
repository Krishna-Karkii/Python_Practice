from modules import functions
import time

print("Welcome Dear Users!")
time_now = time.strftime("%b %d, %Y %H-%M-%S")
print("it is ", time_now)

while True:

    # Here we take input form the user and strip the space characters
    User_action = input("Type add, show, edit, complete or exit :")
    User_action = User_action.strip()

    if User_action.startswith("add"):

        Users_prompt = User_action[4:] + "\n"
        Users_prompt = Users_prompt.title()

        Users_list = functions.return_todos()

        Users_list.append(Users_prompt)

        functions.write_todos(Users_list)

    elif User_action.startswith("show"):

        # Users_file = open("todos.txt", 'r')
        # Users_list = Users_file.readlines()
        # Users_file.close()

        Users_list = functions.return_todos()

        # New_Users_list = [todo.strip('\n') for todo in Users_list]

        for index, todo in enumerate(Users_list):
            todo = todo.strip('\n') # here we applied strip to remove '\n'
            index = index + 1
            print(f"{index}. {todo}")

    elif User_action.startswith("complete"):
        try:
            Users_list = functions.return_todos()

            complete_prompt = int(User_action[9:])
            complete_prompt = complete_prompt - 1
            print(f"Completed the todo {Users_list[complete_prompt]}")
            Users_list.pop(complete_prompt)

            functions.write_todos(Users_list)

        except ValueError:
            print("Invalid command!, Please enter the number of todo"
                  " you wanna edit\n")
            continue

        except IndexError:
            print("Invalid! Please enter the correct number of the todo to edit")
            continue

    elif User_action.startswith("edit"):
        try:
            Users_list = functions.return_todos()
            num = int(User_action[4:])
            num = num - 1

            new_todo = input("Enter new todo :") + '\n'
            new_todo = new_todo.title()

            Users_list[num] = new_todo

            functions.write_todos(Users_list)

        except ValueError:
            print("Command Invalid!, Please enter"
                  " the number of the todo you want to edit\n")

            continue

        except IndexError:
            print("Command Invalid!, Please enter the correct number of "
                  "todo to edit\n")

            continue

    elif 'exit' in User_action:
        break

    else:
        print("Incorrect Command")

print("Thanks for using us")