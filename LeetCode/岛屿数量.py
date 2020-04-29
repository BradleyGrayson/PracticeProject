class Solution:
    # 深度优先搜索
    # 时间复杂度为O(M*N), M和N分别为行数和列数
    # 空间复杂度为O(M*N)
    # 在该题使用深度优先搜索时没有使用栈，实际上，使用的是系统提供的隐性栈。
    # 隐性栈使用的内存是图的最大深度，在该题中，最坏情况是全为陆地，
    # 此时我们使用DFS的深度是M*N，因此空间复杂度是O(M*N)
    def numIslands1(self, grid: list):
        def dfs(grid, i, j, cols, rows):
            grid[i][j] = '0'
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for x, y in directions:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < rows and 0 <= tmp_j < cols and grid[tmp_i][tmp_j] == '1':
                    dfs(grid, tmp_i, tmp_j, cols, rows)

        island_cnt = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    island_cnt += 1
                    dfs(grid, i, j, cols, rows)
        return island_cnt

    # 广度优先搜索
    # 时间复杂度为O(M*N), M和N分别为行数和列数
    # 空间复杂度为O(min(M,N))，最坏的情况下全部为陆地，此时队列的大小为min(M, N)
    def numIslands2(self, grid: list):
        if not grid:
            return 0
        cnt = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(i, j):
            queue = [(i, j)]
            grid[i][j] = '0'
            while queue:
                i, j = queue.pop(0)
                for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < rows and 0 <= tmp_j < cols and grid[tmp_i][tmp_j] == '1':
                        grid[tmp_i][tmp_j] = '0'
                        queue.append((tmp_i, tmp_j))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    cnt += 1
                    bfs(i, j)
        return cnt
        # if not grid: return 0
        # island_cnt = 0
        # rows = len(grid)
        # cols = len(grid[0])
        #
        # def bfs(grid, i, j):
        #     queue = [(i, j)]
        #     grid[i][j] = '0'
        #     while queue:
        #         i, j = queue.pop(0)
        #         for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        #             tmp_i = i + x
        #             tmp_j = j + y
        #             if 0 <= tmp_i < rows and 0 <= tmp_j < cols and grid[tmp_i][tmp_j] == '1':
        #                 grid[tmp_i][tmp_j] = '0'
        #                 queue.append((tmp_i, tmp_j))
        #
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == '1':
        #             island_cnt += 1
        #             bfs(grid, i, j)
        # return island_cnt


island_grid = [['1', '1', '1', '0', '0'],
               ['1', '0', '0', '1', '0'],
               ['1', '0', '0', '1', '0'],
               ['0', '1', '1', '0', '1']]

a = Solution()
# print(a.numIslands1(island_grid))
print(a.numIslands2(island_grid))