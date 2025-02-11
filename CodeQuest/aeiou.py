cases = int(input().rstrip())
vowels = 0
for i in range(cases):
    line = input().rstrip()

    for j in line:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            vowels += 1
    print(vowels)
    vowels = 0
