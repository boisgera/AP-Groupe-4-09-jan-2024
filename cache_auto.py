import time


def succ(x):
    time.sleep(3.0)
    return x + 1


def times_two(x):
    time.sleep(3.0)
    return 2 * x


def cached_function(fct):
    cache = {}

    def function(x):
        nonlocal cache
        if x in cache:
            return cache[x]
        y = fct(x)
        cache[x] = y
        return y

    return function


succ_cached = cached_function(succ)
times_two_cached = cached_function(times_two)

print(succ_cached(1.0))
print(succ_cached(2.0))
print(succ_cached(1.0))
print(times_two_cached(1.0))
print(times_two_cached(2.0))
print(times_two_cached(1.0))
