msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept " \
        "through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

while True:
    print(msg_0)
    x, operation, y = input().split()
    try:
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
            break
    except ValueError:
        print(msg_1)
        continue
    except ZeroDivisionError:
        print(msg_3)
        continue

