User_prompt = input("Enter a password = ")
result = {}
while True:
    if len(User_prompt) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for digits in User_prompt:
        if digits.isdigit() is True:
            digit = True

    result["Number"] = digit

    uppercase = False
    for case in User_prompt:
        if case.isupper() is True:
            uppercase = True

    result["capital"] = uppercase

    if all(result.values()) is True:
        print("This password is strong")
        break

    else:
        print("This password is weak")
        break
