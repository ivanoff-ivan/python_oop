def genrange(start, end):
    nums = range(start, end + 1)
    for num in nums:
        yield num

print(list(genrange(1, 10)))
