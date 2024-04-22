import random
print("Python Random Generator!\n")
lower_index = int(input("Enter the lower index :"))
higher_index = int(input("Enter the higher index :"))

result = random.randint(lower_index, higher_index)
print(result)
