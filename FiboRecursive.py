fib = {}  # Boş bir sözlük oluşturuluyor

def fib2(n):
    if n <= 1:
        fib[str(n)] = 1
        return 1
    elif str(n-1) in fib:
        fib[str(n)] = fib[str(n-1)] + fib[str(n-2)]
        return fib[str(n)]
    else:
        fib[str(n)] = fib2(n-1) + fib2(n-2)
        return fib[str(n)]

print(fib2(7))
# Çıktı olarak, 7. Fibonacci sayısı olan 13 elde edilir.