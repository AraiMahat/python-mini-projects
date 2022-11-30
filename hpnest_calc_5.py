msg_ = ["Enter an equation",
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept " \
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


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


while True:
    print(msg_[0])
    x, operation, y = input().split()
    try:
        result = 0
        if x == "M":
            x = memory
        elif y == "M":
            y = memory
        x = float(x)
        y = float(y)
        if operation not in "+-*/":
            print(msg_[2])
        else:
            check(x, y, operation)
            if x or y == 0:
                pass
            if operation == "/":
                result = x / y
                print(result)
            elif operation == "+":
                result = x + y
                print(result)
            elif operation == "-":
                result = x - y
                print(result)
            elif operation == "*":
                result = x * y
                print(result)
            print(msg_[4])
            answer = input()
            if answer == "y":
                if is_one_digit(result):
                    msg_index = 10
                    print(msg_[msg_index])
                    answer = input()
                    if answer == "y":
                        if msg_index < 12:
                            msg_index = msg_index + 1
                    elif answer == "n":
                        memory = result
                        print(msg_[5])
            elif answer == "n":
                print(msg_[5])
            else:
                print(msg_[4])
            answer = input()
            if answer == "y":
                continue
            elif answer == "n":
                break
            else:
                break
    except ValueError:
        print(msg_[1])
        continue
    except ZeroDivisionError:
        print(msg_[3])
        continue



