def sum_even(x):
    x = 10
    sum = 0
    for i in range(1, x):
        if i % 2 == 0:
            sum += i
    return sum

print(sum_even(10))
