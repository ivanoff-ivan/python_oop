class store_results:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        with open("results.txt", "a") as file:
            result = f"Function {self._func.__name__} was called." \
                     f" Result. {self._func(*args)}\n"
            file.write(result)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
