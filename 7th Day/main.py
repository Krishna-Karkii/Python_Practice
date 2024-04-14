# 7th Day

print("Welcome Dear Users!")
while True:

    # Here we take input form the user and strip the space characters
    User_action = input("Type add, show, edit, complete or exit :")
    User_action = User_action.strip()
    match User_action:

        case 'add':

            Users_prompt = input("Enter a todo task :") + "\n"
            Users_prompt = Users_prompt.title()

            Users_file = open("todos.txt", "r")
            Users_list = Users_file.readlines()
            Users_file.close()

            Users_list.append(Users_prompt)

            Users_file = open("todos.txt", "w")
            Users_file.writelines(Users_list)
            Users_file.close()

        case  'show':

            Users_file = open("todos.txt", 'r')
            Users_list = Users_file.readlines()
            Users_file.close()

            # New_Users_list = [todo.strip('\n') for todo in Users_list]

            for index, todo in enumerate(Users_list):
                todo = todo.strip('\n') # here we applied strip to remove '\n'
                index = index + 1
                print(f"{index}. {todo}")

        case  'complete':

            Users_file = open('todos.txt', 'r')
            Users_list = Users_file.readlines()
            Users_file.close()

            complete_prompt = int(input("Enter the number of todo you want to complete :"))
            complete_prompt = complete_prompt - 1
            print(f"Completed the todo {Users_list[complete_prompt]}")
            Users_list.pop(complete_prompt)

            Users_file = open('todos.txt','w')
            Users_file.writelines(Users_list)

        case  'edit':

            Users_file = open('todos.txt', 'r')
            Users_list = Users_file.readlines()
            Users_file.close()

            num = int(input("Enter the number of todo you want to edit :"))
            new_todo = input("Enter new todo :") + '\n'
            new_todo = new_todo.title()
            num = num - 1
            Users_list[num] = new_todo

            Users_file = open("todos.txt", 'w')
            Users_file.writelines(Users_list)
            Users_file.close()

        case  'exit':
            break

print("Thanks for using us")