# today we gonna do some bonus task
contents = ["hello i am krishna",
           "i am 20 yrs old",
           "i am an male"]
filenames = ['name.txt','age.txt','gender.txt']
for filename,content in zip(filenames,contents):
    file_name = open(f"../files/{filename}",'w')
    Users_file = file_name.writelines(content)
