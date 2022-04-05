nums = [3,3]
target = 6

result = []
for i in range(len(nums)):
    if nums[i] + nums[i - 1] == target:
        result.append(i - 1)
        if i - 1 == 0:
            result.append(len(nums) - 3)
        else:
            result.append(len(nums) - 1)
        break
print(result)
