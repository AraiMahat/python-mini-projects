msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept " \
        "through all classes, haven't you?"

while True:
    try:
        print(msg_0)
        x, operation, y = input().split()
        if operation not in "+-*/":
            print(msg_2)
        else:
            x = float(x)
            y = float(y)
            break
    except ValueError:
        print(msg_1)

