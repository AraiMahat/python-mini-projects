def count_less_than_ten(a: list[int]) -> int:
    count = 0
    for i in range(len(a)):
        if 0 < a[i] < 10:
            count += 1
    return count


print(count_less_than_ten([1, 2, 3, 100, 3, 2, 1]))
