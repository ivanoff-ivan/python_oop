def store_results(func):
    def wrapper(*args):
        with open("results.txt", "a") as file:
            result = f"Function {func.__name__} was called." \
                     f" Result. {func(*args)}\n"
            file.write(result)

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
