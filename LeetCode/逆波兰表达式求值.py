class Solution:
    def evalRPN(self, tokens: list) -> int:
        num_stack = []

        for i in tokens:
            try:
                num_stack.append(int(i))
            except ValueError:
                n1 = num_stack.pop()
                n2 = num_stack.pop()
                if i == '+':
                    num_stack.append(n2 + n1)
                elif i == '*':
                    num_stack.append(n2 * n1)
                elif i == '/':
                    num_stack.append(int(n2 / n1))
                elif i == '-':
                    num_stack.append(n2 - n1)

        return num_stack[0]


expression1 = ["2", "1", "+", "3", "*"]
expression2 = ["4", "13", "5", "/", "+"]
expression3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
s = Solution()
print('correct answer = 9 , my answer =', s.evalRPN(expression1))
print('correct answer = 6 , my answer =', s.evalRPN(expression2))
print('correct answer = 22, my answer =', s.evalRPN(expression3))