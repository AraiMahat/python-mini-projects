def zero_to_one(a: list[int]) -> list[int]:
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1
    return a


print(zero_to_one([1, 2, 3, 4, 0, 5, 6]))
