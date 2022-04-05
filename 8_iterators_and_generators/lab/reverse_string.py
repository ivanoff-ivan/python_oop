def reverse_text(text):
    current_index = len(text)
    while current_index > 0:
        current_index -= 1
        yield text[current_index]


for char in reverse_text("step"):
    print(char, end='')
