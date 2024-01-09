
def f(x, *args, **kwargs):
    print(x, args, kwargs)

f(1, 2, 7, 89, debug=True, verbose=False)