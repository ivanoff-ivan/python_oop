class make_bold:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        result = self.func(*args)
        return f"<b>{result}</b>"


class make_italic:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        result = self.func(*args)
        return f"<i>{result}</i>"


class make_underline:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        result = self.func(*args)
        return f"<u>{result}</u>"


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
