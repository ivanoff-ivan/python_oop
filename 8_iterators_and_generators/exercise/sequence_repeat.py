class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter < self.number:
            return self.sequence[self.counter % len(self.sequence)]
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
