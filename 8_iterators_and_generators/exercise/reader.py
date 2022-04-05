def read_next(*args):
    for arg in args:
        for a in arg:
            yield str(a)


