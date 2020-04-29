class Solution:
    # 使用内置函数
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


s = Solution()
print('correct: 100, my answer:', s.addBinary('11', '1'))
print('correct: 10101, my answer:', s.addBinary('1010', '1011'))