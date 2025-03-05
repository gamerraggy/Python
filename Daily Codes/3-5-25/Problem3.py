def count_down_up(n):
    for i in range(n, 1, -1):
        print(i, end= " ")
    for i in range(1, n+1, 1):
        print(i, end = " ")
        
count_down_up(5)
