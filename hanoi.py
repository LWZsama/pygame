def hanoi(A, B, C, n):
    if n == 1:
        print(A, "->", C)
        return
    hanoi(A, C, B, n-1)
    print(A, "->", C)
    hanoi(B, A, C, n-1)
    
hanoi("A", "B", "C", 3)
