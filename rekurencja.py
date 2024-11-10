import time
def fibonacci(n):
    if n < 0:
        raise ValueError("Wartość musi być nieujemna")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
start = time.time()
n = 100 
print(f"Numer wartość ciągu fibonnaciego dla wartości {n} jest {fibonacci(n)}")
koniec = time.time()

print(koniec - start)
