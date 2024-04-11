print("Welcome dear user!")
Users_list = []
while True:
    User_action= input("Type add, show, edit or exit :")
    User_action = User_action.strip()
    match User_action:
        case 'add':
            User_prompt = input("Enter a todo task :")
            Users_list.append(User_prompt)
        case  'show':
            for todo in Users_list:
                print(todo)
        case  'edit':
            num = int(input("Enter the number of todo you want to edit :"))
            new_todo = input("Enter new todo :")
            num = num - 1
            Users_list[num] = new_todo

        case  'exit':
            break