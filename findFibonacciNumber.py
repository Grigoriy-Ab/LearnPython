close = 0
while True:
    f1 = 0
    f2 = 1
    n = int(input("введите n: "))
    if n == -1:
        break
    
    fib = f2 + f1
    sum1 = 0
    
    if n == 0:
        fib = f1
    elif n == 1:
        fib = f2
    elif n == 2:
        fib = fib
    elif n == 3:
        fib = f2 + fib    
    else:
        sum1 = fib
        sum2 = f2 + fib
        for i in range(3, n+1):
            sum2 = fib
            fib = sum1 + sum2
            sum1 = sum2
    
    print("число Фибоначчи: " + str(fib))    