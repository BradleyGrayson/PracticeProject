class Solution:
    # 我的解法
    def findMaxConsecutiveOnes1(self, nums: list) -> int:
        slow = -1
        maxn = 0

        for index, num in enumerate(nums):
            if num == 1:
                tmp = index - slow
                maxn = max(maxn, tmp)
            if num == 0:
                slow = index
        return maxn
    # 别人的解法
    def findMaxConsecutiveOnes2(self, nums: list) -> int:
        curr_cnt = 0
        maxn = 0
        nums.append(0)
        for num in nums:
            if num == 1:
                curr_cnt += 1
            else:
                if curr_cnt > maxn:
                    maxn = curr_cnt
                curr_cnt = 0
        return maxn

# n = [0, 1, 0, 1, 1]   # correct: 2
# n = [1, 1, 0, 1]    # correct: 2
# n = [0]   # correct: 0
n = [1]   # correct: 1
s = Solution()
print('my ans:', s.findMaxConsecutiveOnes2(n))