class Solution:
    # 使用内置方法排序
    def arrayPairSum(self, nums: list) -> int:
        sorted_nums = sorted(nums)
        cnt = 0
        for i in sorted_nums[::2]:
            cnt += i
        return cnt


inputs = [1, 4, 3, 2]
s = Solution()
print('correct: 4, my answer:', s.arrayPairSum(inputs))
