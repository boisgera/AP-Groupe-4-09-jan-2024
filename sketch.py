
def universal_answer(fct):
    def forty_two(x):
        return 42
    return forty_two

@universal_answer
def succ(x):
    return x + 1

@universal_answer
def times_two(x):
    return 2*x

# succ = universal_answer(succ)
print(succ(3.14))
print(times_two(56))