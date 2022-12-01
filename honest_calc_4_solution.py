msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept " \
        "through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

memory = 0
running = True
result = 0


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
        print(msg_3)


def is_one_digit(v):
    try:
        if v == int(v):
            return -10 < v < 10
    except ValueError:
        return False


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
        msg = msg + msg_6
    if (a == 1 or b == 1) and op == "*":
        msg = msg + msg_7
    if (a == 0 or b == 0) and (op == "*" or op == "+" or op == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while running:
    print(msg_0)
    x, operation, y = input().split()

    try:
        if x == "M":
            x = memory
        elif y == "M":
            y = memory

        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    valid_operations = '+-*/'
    if operation not in valid_operations:
        print(msg_2)

    check(x, operation, y)

    result = calculate(x, operation, y)
    if result is not None:
        print(result)
    else:
        continue

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_4)
        answer = input()
        if answer == "y":
            memory = result

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_5)
        answer = input()
        if answer == "n":
            running = False



