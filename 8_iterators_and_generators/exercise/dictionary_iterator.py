class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = [(k, v) for k, v in self.dictionary.items()]
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter < len(self.keys):
            return self.keys[self.counter]
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
