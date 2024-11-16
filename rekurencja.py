import time
import sys

sys.set_int_max_str_digits(10000)

def fibonacci(n):
    if n < 0:
        raise ValueError("Wartość musi być nieujemna")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

start = time.time()
n = 40000 
print(f"Numer wartość ciągu Fibonacciego dla wartości {n} jest {fibonacci(n)}")
koniec = time.time()

print(f"Czas wykonania: {koniec - start} sekund")