from time import time


def fibon(n):
    if n < 2:
        return n
    return fibon(n - 1) + fibon(n - 2)


cache = {}


def fibon_cache(n):
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    value = fibon_cache(n - 1) + fibon_cache(n - 2)
    cache[n] = value
    return value


for n in range(0, 7):
    print(fibon(n))

start = time()
print(fibon(30))
end = time()
print(end - start)

start = time()
print(fibon_cache(30))
end = time()
print(end - start)

print(fibon_cache(5))
