class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_num = 0 - step
        self.aiming_num = step * count

    def __iter__(self):
        return self

    def __next__(self):
        self.current_num += self.step
        if self.current_num < self.aiming_num:
            return self.current_num
        raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

[print(i) for i in range(0, self.aiming_n)]
