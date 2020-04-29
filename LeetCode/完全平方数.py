import math
from queue import Queue

class Solution:
    # 超时
    def numSquares1(self, n: int) -> int:
        if int(math.sqrt(n))**2 == n:
            return 1
        graph = [i**2 for i in range(1, int(math.sqrt(n)) + 1)][::-1]
        q = Queue()
        [q.put((g, g, 1)) for g in graph]
        used = []
        while not q.empty():
            cur, total, cnt = q.get()
            for g in graph:
                if total + g == n:
                    return cnt + 1
                if total + g < n and (g, cnt) not in used:
                    q.put((g, total + g, cnt + 1))
                    used.append((g, cnt + 1))

    # 超时
    def numSquares2(self, n: int) -> int:
        def get_nodes(input: int):
            return [input - i**2 for i in range(1, int(math.sqrt(input)+1))]

        init_graph = get_nodes(n)
        if 0 in init_graph: return 1
        used = []
        q = Queue()
        for i in init_graph:
            q.put((i, 1))

        while not q.empty():
            cur, cnt = q.get()

            next_graph = get_nodes(cur)
            if 0 in next_graph:
                return cnt + 1
            for i in next_graph:
                if (i, cnt+1) not in used:
                    q.put((i, cnt + 1))
                    used.append((i, cnt+1))

    # 未超时，执行用时1336ms，消耗17MB内存
    # 这个是从n向下减的，也可以做一个从0向上加的
    def numSquares3(self, n: int) -> int:
        int_n = int(math.sqrt(n))
        if int_n ** 2 == n: return 1

        graph = tuple(map(lambda x: x ** 2, range(1, int_n + 1)))
        used = set()

        q = Queue()
        q.put((n, 0))

        while not q.empty():
            cur, cnt = q.get()
            cnt += 1
            for node in graph:
                if cur - node == 0:
                    return cnt
                if node < cur and (cur-node, cnt) not in used:
                    q.put((cur-node, cnt))
                    used.add((cur-node, cnt))



    def numSquares4(self, n: int) -> int:
        int_n = int(math.sqrt(n))
        if int_n ** 2 == n: return 1

        graph = tuple(map(lambda x: x ** 2, range(1, int_n + 1)))
        used = [False for _ in range(n + 1)]

        q = Queue()
        q.put((n, 0))
        used[n] = True

        while not q.empty():
            cur, cnt = q.get()
            sub = 1
            tcur = cur - 1
            while tcur >= 0:
                if tcur == 0:
                    return cnt + 1
                if not used[tcur]:
                    q.put((tcur, cnt + 1))
                    used[tcur] = True
                sub += 1
                tcur = cur - sub ** 2


# num = 7168
num = 10
s = Solution()
print(s.numSquares3(num))
