from collections import deque


class Solution:
    def updateMatrix(self, matrix: list) -> list:
        def count(row, col, point):
            q = deque()
            visited = {}
            q.append((row, col))
            visited[(row, col)] = 0
            while q:
                i, j = q.popleft()
                for newi, newj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0<=newi<len(matrix) and 0<=newj<len(matrix[0]) and (newi, newj) not in visited:
                        if matrix[newi][newj] == 1:
                            visited[(newi, newj)] = visited[(i, j)] + 1
                            q.append((newi, newj))
                        else:
                            return visited[(i, j)] + 1

        distance_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for row_index, row in enumerate(matrix):
            for col_index, point in enumerate(row):
                if matrix[row_index][col_index] == 1:
                    distance_matrix[row_index][col_index] = count(row_index, col_index, point)
        return distance_matrix


matrix = [[1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
          [1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
          [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
          [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
          [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
          [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
          [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]

s = Solution().updateMatrix(matrix)
print('origin matrix:')
for i in matrix:
    print(i)
print('-' * 10)
print('new matrix:')
for i in s:
    print(i)
