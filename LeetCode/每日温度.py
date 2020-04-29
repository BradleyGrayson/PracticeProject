class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []

        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                tmp = stack.pop()
                ans[tmp] = i - tmp
            stack.append(i)

        return ans


t = [73, 74, 75, 71, 69, 72, 76, 73]
s = Solution()
a = s.dailyTemperatures(t)
print('answer = [1, 1, 4, 2, 1, 1, 0, 0]'.rjust(40))
print('my answer ={}'.format(a).rjust(40))
