def get_primes(nums):
    for num in nums:
        if num == 1 or num == 0:
            continue

        is_prime = True
        possible_nums = [i for i in range(2, num // 2 + 1)]
        for possible_num in possible_nums:
            if num % possible_num == 0:
                is_prime = False

        if is_prime:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
