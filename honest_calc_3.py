msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept " \
        "through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"
memory = 0

while True:
    print(msg_0)
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
            print(msg_2)
        else:
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
            print(msg_4)
            answer = input()
            if answer == "y":
                memory = result
                print(msg_5)
            elif answer == "n":
                print(msg_5)
            else:
                print(msg_4)
            answer = input()
            if answer == "y":
                continue
            elif answer == "n":
                break
            else:
                break
    except ValueError:
        print(msg_1)
        continue
    except ZeroDivisionError:
        print(msg_3)
        continue

