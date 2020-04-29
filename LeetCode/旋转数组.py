class Solution:
    def rotate1(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr_index = 0
        curr_num = nums[curr_index]
        loop_cnt = 0
        visited = set()
        while loop_cnt < len(nums):
            if curr_index not in visited:
                visited.add(curr_index)
                next_num = nums[(curr_index + k) % len(nums)]
                nums[(curr_index + k) % len(nums)] = curr_num
                curr_index = (curr_index + k) % len(nums)
                curr_num = next_num
                loop_cnt += 1
            else:
                curr_index += 1
                curr_num = nums[curr_index]

    def rotate2(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums[-1])
            del nums[-1]

    def rotate3(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate4(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[::-1]
        k = k % len(nums)
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


s = Solution()
n = [1, 2, 3, 4, 5, 6, 7]
s.rotate4(n, 3)
print('correct: [5, 6, 7, 1, 2, 3, 4]')
print('my ans :', n)
n = [-1, -100, 3, 99]
s.rotate4(n, 6)
print('correct: [3, 99, -1, -100]')
print('my ans :', n)
