feet_inches = input("Enter feet and inches : ")


def divider(user_prompt):
    split = user_prompt.split()
    feet = float(split[0])
    inches = float(split[1])
    dictionery = {"feet": feet, "inches": inches}
    return dictionery


def get_output(local_feet, local_inches):
    meters = local_feet * 0.3048 + local_inches * 0.0254
    return meters


user_values = divider(feet_inches)
result = get_output(user_values['feet'], user_values['inches'])

print(f"the kid is {user_values['feet']} feet {user_values['inches']} that is {result} meters.")
if result > 0.8:
    print("Kid can use the slide")

else:
    print("Kid can't use the slide")


