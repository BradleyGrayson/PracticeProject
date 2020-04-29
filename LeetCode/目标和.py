class Solution:
    # 超时
    def findTargetSumWays1(self, nums: list, S: int) -> int:
        visited = {}

        def dfs(index, total):
            if index < len(nums):
                for num in (nums[index], -nums[index]):
                    new_index = index + 1
                    new_total = total + num
                    if (new_index, new_total) not in visited:
                        visited[(new_index, new_total)] = 0
                    if (new_index, new_total) in visited:
                        visited[(new_index, new_total)] += 1
                    dfs(new_index, new_total)

        dfs(0, 0)

        return visited[(len(nums), S)]

    def findTargetSumWays2(self, nums: list, S: int) -> int:
        visited = {}

        def dfs(index, sum):
            if index < len(nums) and (index, sum) not in visited:
                visited[(index, sum)] = dfs(index + 1, sum + nums[index]) + dfs(index + 1, sum - nums[index])
            return visited.get((index, sum), sum == S)

        return dfs(0, 0)


nu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
S = 0
# nu = [1, 1, 1, 1, 1]
# S = 3
s = Solution()
ans = s.findTargetSumWays2(nu, S)
print('correct: 5, my ans: {}'.format(ans))
