import string

pencils = int(input("How many pencils would you like to use:\n"))
turn = input("Who will be the first (John, Jack):\n")
if turn not in ["John", "Jack"]:
    print("Choose between 'John' and 'Jack'")
else:
    while pencils > 0:
    if pencils in string.digits:
        print("|" * pencils)
        pencils -= int(input(turn + "'s turn:\n"))
        turn = "John" if turn == "Jack" else "Jack"
    elif pencils == 0:
        print("The number of pencils should be positive")
    else:
        print("The number of pencils should be numeric")
        continue
