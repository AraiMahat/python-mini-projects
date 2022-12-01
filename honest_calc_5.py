msg_ = ["Enter an equation",
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept "\
        "through all classes, haven't you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]
memory = 0
running = True
result = 0
valid_operations = '+-*/'
play_again = False


def add(a, b):
    return a + b


def substr(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    try:
        if b == 0:
            return a / b
    except ZeroDivisionError:
        print(msg_[3])


def is_one_digit(v):
    try:
        if v == int(v):
            return -10 < v < 10
    except ValueError:
        return False


def save_to_memory(v):
    if not is_one_digit(v):
        return True
    else:
        msg_index = 10
        while True:
            print(msg_[msg_index])
            if answer == "y" and msg_index < 12:
                msg_index = msg_index + 1
                continue
            elif answer == "n":
                return False
            else:
                return True


def calculate(a, op, b):
    global result
    if op == "+":
        result = add(a, b)
    if op == "-":
        result = substr(a, b)
    if op == "*":
        result = multiply(a, b)
    if op == "/":
        result = division(a, b)
    return result


def check(a, op, b):
    msg = ""
    if is_one_digit(a) and is_one_digit(b):
        msg = msg + msg_[6]
    if (a == 1 or b == 1) and op == "*":
        msg = msg + msg_[7]
    if (a == 0 or b == 0) and (op == "*" or op == "+" or op == "-"):
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


while running:
    print(msg_[0])
    x, operation, y = input().split()

    try:
        if x == "M":
            x = memory
        elif y == "M":
            y = memory

        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_[1])
        continue

    if operation not in valid_operations:
        print(msg_[2])

    check(x, operation, y)

    result = calculate(x, operation, y)
    if result is not None:
        print(result)
    else:
        continue

    while True:
        print(msg_[4])
        answer = input()
        if answer == "y":
            if save_to_memory(result):
                memory = result
            break
        elif answer == "n":
            break
        else:
            continue

    while True:
        print(msg_[5])
        answer = input()
        if answer == "y":
            play_again = True
            break
        elif answer == "n":
            play_again = False
            break
        else:
            continue

    if play_again:
        continue
    else:
        break


