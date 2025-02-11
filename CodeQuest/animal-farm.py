cases = int(input().rstrip())
for i in range(cases):
    line = input().rstrip()
    data = line.split(" ")
    for i in range(len(data)):
        data[i] = int(data[i])

    num = data[0]*2 + data[1]*4 + data[2]*4
    print(num)
