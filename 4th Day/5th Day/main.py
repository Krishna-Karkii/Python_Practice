print("Welcome dear user!")
# in 5th day we want to make an numbering system appear in front of the todo list
# so we can make the user easy to make an edit in his todo list
# today we will use the enumerate and fstring
# we also asked the user for which todo he wants to complete and modified it
Users_list = []
while True:
    User_action = input("Type add, show, edit, complete or exit :")
    User_action = User_action.strip()
    match User_action:
        case 'add':
            User_prompt = input("Enter a todo task :")
            User_prompt = User_prompt.title()
            Users_list.append(User_prompt)
        case  'show':
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