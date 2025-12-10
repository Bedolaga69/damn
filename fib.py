def fib(n, l = []):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = fib(n - 1) + fib(n - 2)
        if a not in l:
            l.append(a)
            print(fib(n - 1) + fib(n - 2))
        return fib(n - 1) + fib(n - 2)

n = 2
print(f"число фибоначи для n= {n}: {fib(n)}")
