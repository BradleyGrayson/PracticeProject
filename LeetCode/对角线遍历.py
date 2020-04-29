class Solution:
    def findDiagonalOrder(self, matrix: list) -> list:
        output = []
        m = len(matrix)
        if not m or not len(matrix[0]):
            return output
        n = len(matrix[0]) - 1
        m -= 1

        i, j = 0, 0
        is_up = True

        while True:
            output.append(matrix[i][j])
            if i == m and j == n:
                return output

            if is_up:
                if i == 0 and j < n:
                    j += 1
                    is_up = False
                elif j == n:
                    i += 1
                    is_up = False
                else:
                    i -= 1
                    j += 1
            else:
                if j == 0 and i < m:
                    i += 1
                    is_up = True
                elif i == n:
                    j += 1
                    is_up = True
                else:
                    i += 1
                    j -= 1


s = Solution()
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('correct: [1, 2, 4, 7, 5, 3, 6, 8, 9]'.rjust(40))
print('my answer: {}'.format(s.findDiagonalOrder(nums)).rjust(40))
