cases = int(input())
for _ in range(cases):
    line = input()
    decyphered = ""
    nextValidLetter = 0
    for i in range(len(line) - 1):
        if line[i] in "aeiou" and i >= nextValidLetter:
            decyphered += line[i+1]
            nextValidLetter = i + 2
    print(decyphered)
