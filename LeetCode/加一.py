class Solution:
    def plusOne(self, digits: list) -> list:
        new_digits = [0] * (len(digits) + 1)
        total = len(digits)
        for index, num in enumerate(digits[::-1]):
            new_index = total - index
            if index == 0:
                tmp = new_digits[new_index] + num + 1
            else:
                tmp = new_digits[new_index] + num
            new_digits[new_index] = tmp % 10
            new_digits[new_index - 1] = tmp // 10

        if new_digits[0] == 0:
            return new_digits[1:]
        return new_digits


s = Solution()
nums = [9, 9, 9]
print('nums:', nums, '  new nums:', s.plusOne(nums))
nums = [1, 2, 9, 8]
print('nums:', nums, '  new nums:', s.plusOne(nums))