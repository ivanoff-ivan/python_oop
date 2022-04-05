class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = {"a", "o", "e", "i", "u", "y"}
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_index < len(self.text):
            ch = self.text[self.current_index]
            self.current_index += 1
            if ch.lower() in self.vowels:
                return ch
            else:
                continue
        raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
