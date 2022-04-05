class cache:
    def __init__(self, func):
        self.func = func
        self.log = {}

    def __call__(self, n):
        self.log[n] = self.func(n)
        return self.func(n)


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
