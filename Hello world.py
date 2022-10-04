# let's learn some stuff!
print('hello world')


numberlist = [1, 2, 3, 7 ,5]
target = 6


def twoSum(nums: numberlist, target: target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

twoSum(numberlist, target)

