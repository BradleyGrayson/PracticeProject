class Solution:
    # 基于递归
    def canVisitAllRooms1(self, rooms: list) -> bool:
        visited = set()

        def dfs(i):
            visited.add(i)
            for key in rooms[i]:
                if key not in visited:
                    dfs(key)

        dfs(0)
        if len(visited) == len(rooms):
            return True
        return False

    # 基于栈
    def canVisitAllRooms2(self, rooms: list) -> bool:
        stack, visited = [0], {0}

        while stack:
            curr_key = stack.pop()
            for key in rooms[curr_key]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)

        if len(visited) == len(rooms):
            return True
        return False

s = Solution()
r = [[1], [2], [3], []]
print('correct: True, my answer:', s.canVisitAllRooms2(r))
r = [[1, 3], [3, 0, 1], [2], [0]]
print('correct: False, my answer:', s.canVisitAllRooms2(r))
r = [[1, 3], [1, 4], [2, 3, 2, 4, 1], [], [4, 3, 2]]
print('correct: True, my answer:', s.canVisitAllRooms2(r))
