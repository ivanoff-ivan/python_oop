# def squares(n):
#     nums = range(1, n + 1)
#     for num in nums:
#         yield num ** 2

def squares(n):
    return (i ** 2 for i in range(1, n + 1))


asd = squares(6)
print(list(asd))
