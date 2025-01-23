num = int(input())
for j in range(num):

    line = input().split()
    for i in range(int(line[1])):
        if int(line[2])-5 < 0:
            break
        else:
            line[2] = int(line[2])-5
        
    if int(line[0])>=int(line[2]):
        print("true")
    else:
        print("false")
