def reverse(word):
    """This function reverses the string"""
    new_word = ""
    for i in range(len(word) - 1, -1, -1):
        new_word += word[i]

    return new_word


print(reverse("regina"))
