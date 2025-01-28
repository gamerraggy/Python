fibonacci = []
fibonacci.append(0)
fibonacci.append(1)

for i in range(88):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
    
cases = int(input().rstrip())
for i in range(cases):
    line = int(input().rstrip())
    print(line, "=", fibonacci[line-1])
