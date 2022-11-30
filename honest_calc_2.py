msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept " \
        "through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

while True:
    try:
        print(msg_0)
        x, operation, y = input().split()
        if operation not in "+-*/":
            print(msg_2)
        else:
            x = float(x)
            y = float(y)
            if operation == "+":
                result = x + y
                print(result)
                break
            if operation == "-":
                result = x - y
                print(result)
                break
            if operation == "*":
                result = x * y
                print(result)
                break
            if operation == "/" and y != 0:
                result = x / y
                print(result)
                break
            else:
                print(msg_3)
                break
    except ZeroDivisionError:
        print(msg_3)
    except ValueError:
        print(msg_1)
