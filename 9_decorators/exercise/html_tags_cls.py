class tags:
    def __init__(self, ch):
        self.ch = ch

    def __call__(self, func):
        def wrapper(*args):
            result = func(*args)
            return f"<{self.ch}>{result}</{self.ch}>"
        return wrapper


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
