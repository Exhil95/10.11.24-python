import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("Wartość musi być liczbą całkowitą")
    if n < 0:
        raise ValueError("Wartość musi być nieujemna")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    start = time.time()
    n = 200
    try:
        print(f"Liczba {n} w ciągu Fibonacciego to {fibonacci(n)}")
    except (ValueError, TypeError) as e:
        print(f"Błąd: {e}")
    end = time.time()
    print(f"Czas obliczeń: {end - start} sekund")

if __name__ == "__main__":
    main()