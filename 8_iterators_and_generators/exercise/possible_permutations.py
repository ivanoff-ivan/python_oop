def possible_permutations(expected_list):
    for i in range(len(expected_list)):
        for j in range(len(expected_list)):
            if j == i:
                continue
            for k in range(len(expected_list)):
                if k == j or k == i:
                    continue
                yield [expected_list[i], expected_list[j], expected_list[k]]


[print(n) for n in possible_permutations([1, 2, 3])]
