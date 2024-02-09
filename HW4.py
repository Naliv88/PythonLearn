"""
Використовуйте модуль часу, щоб порівняти продуктивність «ефективного» методу пошуку простих чисел із простою 
реалізацією (без перерв, тестування за всіма числами тощо). 
Перевірте кілька діапазонів пошуку простих чисел (наприклад, до 100, до 1000 і т.д.)
Ефективний метод - будь який математично визначиний підхід обрахунку
Рекомендую дивитись метод Решето Эратосфена - https://uk.wikipedia.org/wiki/Решето_Ератосфена
import math
N = 1000000  # діапазон в якому шукаємо прості числа
prime = [True] * N
prime[0], prime[1] = False, False # 0 та 1 не є простими
for i in range(2, math.ceil(math.sqrt(N))):  # від 2 до квадратного кореня з N 
    if prime[i]:  # якщо просте видаляємо всі числа кратні до нього
        j = i * i   # для i=2,j будуть такі значення 4,6,8,10,12... для i=3 j — 9,12,15,18,21...
        while j < N:
            prime[j] = False
            j += i

"""

import time

def time_function_execution(func, rang):
    start_time = time.time()
    sieve_primes = func(rang)
    end_time = time.time()
    return [start_time, sieve_primes, end_time]

def simple_prime_search(n):
    primes = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes

ranges = [100, 1000, 100000] 

for r in ranges:
    simple_primes=time_function_execution(simple_prime_search, r)
    print(f"Прості числа до {r} за простим методом: {len(simple_primes[1])} чисел, час виконання: {simple_primes[2] - simple_primes[0]} сек")

    sieve_primes =time_function_execution(sieve_of_eratosthenes, r)
    print(f"Прості числа до {r} за методом Решета Ератосфена: {len(sieve_primes[1])} чисел, час виконання: {sieve_primes[2] - sieve_primes[0]} сек")
