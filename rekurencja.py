import time

def fibonacci(n, memo={}):
    if n < 0:
        raise ValueError("Wartość musi być nieujemna")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        memo[n] = result
        return result

start = time.time()
n = 100 
print(f"Liczba {n} w ciągu Fibonacciego to {fibonacci(n)}")
koniec = time.time()

print(f"Czas obliczeń: {koniec - start} sekund")