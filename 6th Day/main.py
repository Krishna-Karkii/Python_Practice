# 6th Day
# in day 6th we learned how to file handel like open and read/write the instructions of a txt file

print("Welcome Dear Users!")
while True:
    User_action = input("Type add, show, edit, complete or exit :")
    User_action = User_action.strip()
    match User_action:
        case 'add':
            Users_prompt = input("Enter a todo task :") + "\n"
            Users_prompt = Users_prompt.title()

            Users_file = open("../7th Day/todos.txt", "r")
            Users_list = Users_file.readlines()
            Users_file.close()

            Users_list.append(Users_prompt)

            Users_file = open("../7th Day/todos.txt", "w")
            Users_file.writelines(Users_list)
            Users_file.close()
        case  'show':
            Users_file = open("../7th Day/todos.txt", 'r')
            Users_list = Users_file.readlines()
            Users_file.close()

            for index, todo in enumerate(Users_list):
                index = index + 1
                print(f"{index}. {todo}")

        case  'complete':
            complete_prompt = int(input("Enter the number of todo you want to complete :"))
            complete_prompt = complete_prompt - 1
            print(f"Completed the todo {Users_list[complete_prompt]}")
            Users_list.pop(complete_prompt)

        case  'edit':
            num = int(input("Enter the number of todo you want to edit :"))
            new_todo = input("Enter new todo :")
            new_todo = new_todo.title()
            num = num - 1
            Users_list[num] = new_todo

        case  'exit':
            break

print("Thanks for using us")