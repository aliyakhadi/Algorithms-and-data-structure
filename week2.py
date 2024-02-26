def countPairs(self, nums: list[int], target: int) -> int:
    lst = [0 for i in range(101)]
    cnt = 0
    for i in range(len(nums)):
        if target >= 0:
            cnt += sum(lst[:target - nums[i] + 50])
        else:
            cnt += sum(lst[:target - nums[i] - 51])
        lst[nums[i]+50] += 1
    return cnt


print(countPairs(0, [-24,-21,-20,-19,35,22,27,34,-41,-20,-3,37,-6,28,-18,48,-43,40,31,-50,33,19,44,31,13], -11))
# The time complexity is O(n*target) in worst case but it should still work fast for large n if nums[i] will ve in  a short range
# Memory complexity is 101*4 + n*4 bytes -> O(n)
# I think this is better than two nested 'for' loops but I don't know how to make it faster