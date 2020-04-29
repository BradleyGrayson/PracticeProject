class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s: return
        head = 0
        rear = len(s) - 1
        while head != rear and rear + 1 != head:
            s[head], s[rear] = s[rear], s[head]
            head += 1
            rear -= 1


inputs = ["h", "e", "l", "l", "o"]
s = Solution()
s.reverseString(inputs)
print('correct: ["o", "l", "l", "e", "h"]')
print('my ans :', inputs)