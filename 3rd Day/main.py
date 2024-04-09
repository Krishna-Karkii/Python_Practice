print("Welcome dear user!")
Users_list = []
while True:
    User_action= input("Type add or show or exit :")
    User_action = User_action.strip()
    match User_action:
        case 'add':
            User_prompt = input("Enter a todo task :")
            Users_list.append(User_prompt)
        case  'show':
            for todo in Users_list:
                print(todo)
        case  'exit':
            break
