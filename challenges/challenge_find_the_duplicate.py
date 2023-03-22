def find_duplicate(nums: list[int]) -> int:
    if not nums:
        return False

    nums.sort()

    for index in range(len(nums) - 1):
        if not isinstance(nums[index], int) or nums[index] < 0:
            return False

        if nums[index] == nums[index + 1]:
            return nums[index]

    return False
