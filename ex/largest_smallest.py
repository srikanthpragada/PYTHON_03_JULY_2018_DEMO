def big_small(nums):
    max = min = nums[0]
    for n in nums:
        if n > max:
            max = n

        if n < min:
            min = n

    return (max, min)


def avg(*nums):
    return sum(nums) / len(nums)


nums = (10, 20, 30, 15, 1, 34)
print(avg(10, 20, 30, 1, 2, 3))

print(big_small(nums))
