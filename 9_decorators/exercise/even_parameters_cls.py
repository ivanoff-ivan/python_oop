class even_parameters:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        nums = self.func(args)  ##
        for num in nums:
            if not isinstance(num, int):
                return "Please use only even numbers!"
            elif num % 2 != 0:
                return "Please use only even numbers!"
        return self.func(*args)


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
