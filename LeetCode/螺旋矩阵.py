class Solution:
    def spiralOrder(self, matrix: list) -> list:
        visited = set()
        output = []
        m = len(matrix)
        if not m or not len(matrix[0]):
            return output
        n = len(matrix[0])

        i, j = 0, 0
        direction = 'right'

        while True:
            visited.add((i, j))
            output.append(matrix[i][j])

            if len(output) == m*n:
                return output

            if direction == 'right':
                if j + 1 >= n or (i, j + 1) in visited:
                    i += 1
                    direction = 'down'
                else:
                    j += 1
            elif direction == 'down':
                if i + 1 >= m or (i + 1, j) in visited:
                    j -= 1
                    direction = 'left'
                else:
                    i += 1
            elif direction == 'left':
                if j - 1 < 0 or (i, j - 1) in visited:
                    i -= 1
                    direction = 'up'
                else:
                    j -= 1
            elif direction == 'up':
                if (i-1, j) in visited:
                    j += 1
                    direction = 'right'
                else:
                    i -= 1


s = Solution()
nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print('correct:   [1, 2, 3, 6, 9, 8, 7, 4, 5]')
print('my answer:', s.spiralOrder(nums))
