class logged:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        result = self.func(*args)
        return f"you called {self.func.__name__}{args}\nit returned {result}"


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
