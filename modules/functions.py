def return_todos(filename="todos.txt"):
    with open(filename, "r") as local_Users_file:
        local_Users_list = local_Users_file.readlines()
    return local_Users_list


def write_todos(local_users_list, filename="todos.txt"):
    with open(filename, "w") as local_Users_file:
        new_Users_list = local_Users_file.writelines(local_users_list)
        return new_Users_list

