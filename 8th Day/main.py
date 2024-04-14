print("Welcome Dear Users!")
while True:

    # Here we take input form the user and strip the space characters
    User_action = input("Type add, show, edit, complete or exit :")
    User_action = User_action.strip()
    match User_action:

        case 'add':

            Users_prompt = input("Enter a todo task :") + "\n"
            Users_prompt = Users_prompt.title()

            with open("todos.txt", "r") as Users_file:
                Users_list = Users_file.readlines()

            Users_list.append(Users_prompt)

            with open("todos.txt", "w") as Users_file:
                Users_file.writelines(Users_list)

        case  'show':

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

        case  'complete':

            with open("todos.txt", 'r') as Users_file:
                Users_list = Users_file.readlines()

            complete_prompt = int(input("Enter the number of todo you want to complete :"))
            complete_prompt = complete_prompt - 1
            print(f"Completed the todo {Users_list[complete_prompt]}")
            Users_list.pop(complete_prompt)

            with open("todos.txt", 'w') as Users_file:
                Users_file.writelines(Users_list)

        case  'edit':

            with open("todos.txt", 'r') as Users_file:
                Users_list = Users_file.readlines()

            num = int(input("Enter the number of todo you want to edit :"))
            new_todo = input("Enter new todo :") + '\n'
            new_todo = new_todo.title()
            num = num - 1
            Users_list[num] = new_todo

            with open("todos.txt", 'w') as Users_file:
                Users_file.writelines(Users_list)

        case  'exit':
            break

print("Thanks for using us")