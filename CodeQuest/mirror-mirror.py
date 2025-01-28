cases = int(input().rstrip())
for i in range(cases):
    line = input().rstrip()
    for i in range(len(line)):
        print(line[len(line)-i-1], end = "")
    print()
