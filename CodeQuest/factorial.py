cases = int(input().rstrip())
for i in range(cases):
    line = int(input().rstrip())
    num = 1
    for i in range(line):
        num *= i+1
    print(num)
