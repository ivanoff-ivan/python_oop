class type_check:
    def __init__(self, type):
        self.type = type

    def __call__(self, func):
        def wrapper(arg):
            if isinstance(arg, self.type):
                return func(arg)
            return "Bad Type"

        return wrapper


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
