def fibonacci():
    first_num = 0
    second_num = 1
    while True:
        yield first_num
        second_num += first_num
        yield second_num
        first_num += second_num


generator = fibonacci()
for i in range(10):
    print(next(generator))
