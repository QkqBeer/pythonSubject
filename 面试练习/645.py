__author__ = "那位先生Beer"


def findErrorNums( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    duplicate = -1
    dismatch = -1
    for i in range(n):
        if nums[abs(nums[i]) - 1] < 0:
            duplicate = abs(nums[i])
        else:
            nums[abs(nums[i]) - 1] *= -1
    print(nums)
    for i in range(n):
        if nums[i] > 0:
            dismatch = i + 1
    return [duplicate, dismatch]
print(findErrorNums([4,3,1,1]))
