def fibonacci(n): 
    a, b = 0, 1 
    for i in range(n): 
        print(f"\n{a}")
        a, b = b, a + b

fibonacci(6) 
