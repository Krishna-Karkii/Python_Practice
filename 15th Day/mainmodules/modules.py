import glob
import webbrowser
import shutil
import csv
test = glob.glob("../../files/*.txt")
print(test)
for filepath in test:
    print(filepath)


# user_prompt = input("Enter a Topic : ")
# webbrowser.open(f"https://www.google.com/search?q={user_prompt}")

with open("test_file.csv") as file:
    its_secret = list(csv.reader(file))

print(its_secret)
user_prompt1 = input("Enter a Name : ")
for row in its_secret:
    if row[0] == user_prompt1:
        print(row[1])
