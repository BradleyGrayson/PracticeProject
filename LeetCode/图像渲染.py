import copy
from collections import deque


class Solution:
    # 基于递归的深度优先搜索
    def floodFill1(self, image: list, sr: int, sc: int, newColor: int) -> list:
        visited = []
        image = copy.deepcopy(image)
        ori = image[sr][sc]

        def dfs(sr, sc):
            for new_sr, new_sc in ((sr + 1, sc), (sr - 1, sc), (sr, sc - 1), (sr, sc + 1)):
                if 0 <= new_sr < len(image) and 0 <= new_sc < len(image[0]) and image[new_sr][new_sc] == ori and (
                        new_sr, new_sc) not in visited:
                    visited.append((new_sr, new_sc))
                    image[new_sr][new_sc] = newColor
                    dfs(new_sr, new_sc)

        image[sr][sc] = newColor
        dfs(sr, sc)
        return image

    # 基于栈的深度优先搜索
    def floodFill2(self, image: list, sr: int, sc: int, newColor: int) -> list:
        visited = []
        stack = []
        image = copy.deepcopy(image)
        ori = image[sr][sc]
        stack.append((sr, sc))

        while stack:
            r, c = stack.pop()
            image[r][c] = newColor
            for newr, newc in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
                if 0 <= newr < len(image) and 0 <= newc < len(image[0]) and image[newr][newc] == ori and (
                        newr, newc) not in visited:
                    stack.append((newr, newc))
                    visited.append((newr, newc))
        return image

    # 基于队列的广度优先搜索，广度优先搜索不能用递归实现
    def floodFill3(self, image: list, sr: int, sc: int, newColor: int) -> list:
        image = copy.deepcopy(image)
        visited = []
        ori = image[sr][sc]
        q = deque()
        q.append((sr, sc))
        visited.append((sr, sc))
        while q:
            r, c = q.popleft()
            image[r][c] = newColor
            for newr, newc in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
                if 0 <= newr < len(image) and 0 <= newc < len(image[0]) and image[newr][newc] == ori and (
                        newr, newc) not in visited:
                    q.append((newr, newc))
                    visited.append((newr, newc))
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
s = Solution()
new = s.floodFill3(image, sr, sc, newColor)
print('origin image:')
for i in image:
    print(i)
print('-' * 10)
print('new image:')
for i in new:
    print(i)
