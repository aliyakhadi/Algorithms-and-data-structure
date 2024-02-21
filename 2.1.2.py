def countKDifference(self, nums: list[int], k: int) -> int:
    lst = [0 for i in range(200)]
    cnt = 0
    for i in range(len(nums)):
        lst[nums[i]] += 1
        cnt = cnt + lst[nums[i] + k] + lst[nums[i] - k]

    return cnt