cases = int(input().rstrip())
firstPart = []
secondPart = []
for i in range(cases):
    line = input().rstrip()
    firstPart.append(line + " =")
    first, second = line.split("|")
    if first == second:
        secondPart.append("NOT AN ANAGRAM")
    else:
        first = sorted(first)
        second = sorted(second)
    
        if first == second:
            secondPart.append("ANAGRAM")
        else:
            secondPart.append("NOT AN ANAGRAM")             
for i in range(len(firstPart)):
    print(firstPart[i], secondPart[i]) 
