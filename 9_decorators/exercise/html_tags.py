def tags(ch):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            return f"<{ch}>{result}</{ch}>"

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
