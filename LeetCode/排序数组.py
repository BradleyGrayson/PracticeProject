import copy


class Solution:
    """
    冒泡排序
    时间复杂度是O(N²)
    空间复杂度是O(1)，因为不需要额外的存储空间（当然我们在这里使用了deepcopy复制了一个额外的数组）
    """
    def sortArray1(self, nums: list) -> list:
        new_nums = copy.deepcopy(nums)
        i = 1
        for i in range(1, len(new_nums)+1):
            for index in range(len(new_nums) - i):
                if new_nums[index] > new_nums[index + 1]:
                    new_nums[index], new_nums[index + 1] = new_nums[index + 1], new_nums[index]
        return new_nums





inputs = [5, 1, 1, 2, 0, 0, 9, 23, 14, 4, 6, 8, 33, 2, 1, 6]
s = Solution()
print('correct:', sorted(inputs))
print('my ans :', s.sortArray1(inputs))
