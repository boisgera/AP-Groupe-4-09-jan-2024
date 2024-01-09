import time

cache_succ = {}

def succ(x):
    if x in cache_succ:
        return cache_succ[x]
    time.sleep(3.0)
    y = x + 1
    cache_succ[x] = y
    return y

cache_times_two = {}

def times_two(x):
    if x in cache_times_two:
        return cache_times_two[x]
    time.sleep(3.0)
    y = 2*x
    cache_times_two[x] = y
    return y

print(succ(1.0))
print(succ(2.0))
print(succ(1.0))
print(times_two(1.0))