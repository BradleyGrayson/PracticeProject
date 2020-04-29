class Solution:
    def getRow1(self, rowIndex: int) -> list:
        if not rowIndex: return [1]
        matrix = [1, 1]
        for i in range(1, rowIndex + 1):
            new_matrix = [1] * (i + 1)
            if i >= 2:
                for j in range(1, len(new_matrix) - 1):
                    new_matrix[j] = matrix[j-1] + matrix[j]
                matrix = new_matrix
        return new_matrix

    def getRow2(self, rowIndex: int) -> list:
        matrix = [1]
        for i in range(rowIndex):
            matrix.insert(0, 0)
            for j in range(i+1):
                matrix[j] = matrix[j] + matrix[j + 1]
        return matrix

s = Solution()
print('correct: [1, 1], my ans:', s.getRow2(1))
print('correct: [1, 2, 1], my ans:', s.getRow2(2))
print('correct: [1, 3, 3, 1], my ans:', s.getRow2(3))
print('correct: [1, 4, 6, 4, 1], my ans:', s.getRow2(4))
