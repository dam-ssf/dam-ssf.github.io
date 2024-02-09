import time

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def benchmark():
    primes = []
    for i in range(1, 100000):
        if is_prime(i):
            primes.append(i)
    return primes

print("Realizando test de rendimiento...")
before = time.time() 
benchmark()
after = time.time()
diff = after - before
minutes = diff/60
print("[COMPLETADO]")
print(f"Time: {minutes:.2f} minutes")
print("Mark:", int((1/minutes)*1000))