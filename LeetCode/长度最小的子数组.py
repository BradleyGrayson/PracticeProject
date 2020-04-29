class Solution:
    # 超时
    def minSubArrayLen1(self, s: int, nums: list) -> int:
        minn = len(nums)

        for index, num in enumerate(nums):
            tmp = 0
            for subindex, subnum in enumerate(nums[index:]):
                tmp += subnum
                if tmp >= s:
                    minn = min(minn, subindex + 1)
                if index == 0 and subindex == len(nums) - 1 and tmp < s:
                    return 0
        return minn

    # 两个指针
    def minSubArrayLen2(self, s: int, nums: list) -> int:
        head = 0
        tail = len(nums) - 1
        sums = sum(nums)
        if sums < s:
            return 0
        while head + 1 != tail and head != tail:
            if sums - nums[head] >= s and sums - nums[tail] >= s:
                if nums[head] < nums[tail]:
                    sums -= nums[head]
                    head += 1
                else:
                    sums -= nums[tail]
                    tail -= 1
            elif sums - nums[head] >= s:
                head += 1
                sums -= nums[head]
            elif sums - nums[tail] >= s:
                tail -= 1
                sums -= nums[tail]
            else:
                break
        print(tail, head)
        if tail == head:
            return 1
        return tail - head + 1


# n = [2, 3, 1, 2, 4, 3]    # when s = 7, correct: 2
# n = [1, 2, 3, 4, 5]     # when s = 11, correct: 3
n = [1, 4, 4]   # when s = 4, correct: 1
# n = [1, 1]
s = Solution()
print('my ans:', s.minSubArrayLen2(4, n))
