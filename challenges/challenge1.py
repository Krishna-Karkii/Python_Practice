while True:
    Users_action = input("Enter whether it is heads or tails ?:")
    Users_action = Users_action.strip()

    match Users_action:
        case 'head' | 'heads':

            with open("Users_input.txt", 'r') as file:
                probability = file.readlines()
                probability.append("head\n")
                numbers_of_heads = int(probability.count("head\n"))
                total_number = int(len(probability))

                probability_number = numbers_of_heads/total_number * 100
                print(f"Heads : {probability_number}")

            with open("Users_input.txt", 'w') as file:
                file.writelines(probability)

        case 'tails' | 'tail' :
            with open("Users_input.txt",'r') as file:
                probability = file.readlines()
                probability.append('tail\n')
                total_number = int(len(probability))
                total_number_tails = int(probability.count('tail\n'))
                probability_number = 100 - total_number_tails/total_number * 100
                print(f"Heads :{probability_number}")

            with open("Users_input.txt",'w') as file:
                file.writelines(probability)

        case 'remove':
            with open("Users_input.txt", 'w') as file:
                file.write('')
