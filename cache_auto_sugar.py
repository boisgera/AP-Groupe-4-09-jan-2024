import time


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


@cached_function  # decorator
def succ(x):
    time.sleep(3.0)
    return x + 1

# succ = cached_function(succ)

def times_two(x):
    time.sleep(3.0)
    return 2 * x

times_two = cached_function(times_two)

print(succ(1.0))
print(succ(2.0))
print(succ(1.0))
print(times_two(1.0))
print(times_two(2.0))
print(times_two(1.0))
