class Solution:
    def pivotIndex(self, nums: list) -> int:
        total = sum(nums)
        cntleft = 0
        for i in range(len(nums)):
            if cntleft == (total - nums[i]) / 2:
                return i
            cntleft += nums[i]
        return -1


n = [-1, -1, 0, 1, 1, 0]
s = Solution()
print('correct: 5, my answer:', s.pivotIndex(n))
