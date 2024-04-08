# my_list = [1, 2, 3, 4, 5, 10, 9, 8]
# # New_list = my_list.sort()
# # print(New_list)
# my_list.sort()
# print(my_list)
# my_list.sort( reverse=True)
# print(my_list)
my_list = []
v = int(input("Enter number of todos you like: "))
n = 0
while n < v:
    users_prompt = input("Enter a todo :")
    n = n+1
    my_list.append(users_prompt)

print("Your todos are ",my_list)
