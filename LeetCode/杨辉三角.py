class Solution:
    def generate(self, numRows: int) -> list:
        triangle = []
        if not numRows:
            return triangle

        for num in range(numRows):
            triangle.append([1] * (num + 1))
            if num >= 2:
                for i in range(1, num):
                    triangle[num][i] = triangle[num - 1][i - 1] + triangle[num - 1][i]
        return triangle


nums = 5
s = Solution()
for i in s.generate(nums):
    print(i)
