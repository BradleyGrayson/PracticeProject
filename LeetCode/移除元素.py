class Solution:
    # 自己实现
    def removeElement1(self, nums: list, val: int) -> int:
        head = 0
        tail = len(nums)-1
        cnt = 0

        while tail + 1 != head:
            if nums[head] != val:
                cnt += 1
                head += 1
            else:
                if nums[tail] == val:
                    tail -= 1
                else:
                    nums[head], nums[tail] = nums[tail], nums[head]

        return cnt
    # 别人解法
    def removeElement2(self, nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
    # 官方双指针之一；之二是将匹配元素移到对位并将队长-1
    def removeElement3(self, nums, val):
        fast, slow = 0, 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


n = [0, 1, 2, 2, 3, 0, 4, 2]
# n = [2]
# n = [3, 3]
s = Solution()
r = s.removeElement3(n, 2)
print('correct: [0, 1, 3, 0, 4]')
print('my ans :', n[:r])