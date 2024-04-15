# 9th day
# today we replaced match case with if else conditional because the case doesn't support anymore
# cont- then one argument
# we used in to check if the user_action contains the specified string or not

print("Welcome Dear Users!")
while True:

    # Here we take input form the user and strip the space characters
    User_action = input("Type add, show, edit, complete or exit :")
    User_action = User_action.strip()

    if 'add' in User_action:

        Users_prompt = User_action[4:] + "\n"
        Users_prompt = Users_prompt.title()

        with open("todos.txt", "r") as Users_file:
            Users_list = Users_file.readlines()

        Users_list.append(Users_prompt)

        with open("todos.txt", "w") as Users_file:
            Users_file.writelines(Users_list)

    elif 'show' in User_action:

        # Users_file = open("todos.txt", 'r')
        # Users_list = Users_file.readlines()
        # Users_file.close()

        with open("todos.txt", 'r') as Users_file:
            Users_list = Users_file.readlines()

        # New_Users_list = [todo.strip('\n') for todo in Users_list]

        for index, todo in enumerate(Users_list):
            todo = todo.strip('\n') # here we applied strip to remove '\n'
            index = index + 1
            print(f"{index}. {todo}")

    elif 'complete' in User_action:

        with open("todos.txt", 'r') as Users_file:
            Users_list = Users_file.readlines()

        complete_prompt = int(User_action[9:])
        complete_prompt = complete_prompt - 1
        print(f"Completed the todo {Users_list[complete_prompt]}")
        Users_list.pop(complete_prompt)

        with open("todos.txt", 'w') as Users_file:
            Users_file.writelines(Users_list)

    elif 'edit' in User_action:

        with open("todos.txt", 'r') as Users_file:
            Users_list = Users_file.readlines()

        num = int(User_action[4:])
        new_todo = input("Enter new todo :") + '\n'
        new_todo = new_todo.title()
        num = num - 1
        Users_list[num] = new_todo

        with open("todos.txt", 'w') as Users_file:
            Users_file.writelines(Users_list)

    elif 'exit' in User_action:
        break

    else:
        print("Incorrect Command")

print("Thanks for using us")