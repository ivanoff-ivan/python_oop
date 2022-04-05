from timeit import default_timer as timer


class exec_time:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        start = timer()
        self._func(*args)
        end = timer()
        result = end - start
        return result


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))
