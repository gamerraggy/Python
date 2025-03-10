def zigzag_pattern(n):
    for i in range(1, n, 2):
        print(i, end = " ")
    for i in range(n-3, 1-2, -2):
        print(i, end = " ")
        
zigzag_pattern(10)
