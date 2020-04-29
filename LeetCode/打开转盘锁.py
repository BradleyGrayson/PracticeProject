from queue import Queue


class Solution:
    def openLock(self, deadends: list, target: str) -> int:
        deadends = set(deadends)
        used = set()

        if '0000' in deadends:
            return -1

        used.add('0000')
        q = Queue()
        q.put(('0000', 0))

        while not q.empty():
            curr, cnt = q.get()

            for i in range(4):
                for add in (-1, 1):
                    curr = curr[:i] + str((int(curr[i]) + add) % 10) + curr[i + 1:]
                    if curr == target:
                        return cnt + 1
                    if curr not in deadends and curr not in used:
                        q.put((curr, cnt + 1))
                        used.add(curr)
        return -1


d = ["0201", "0101", "0102", "1212", "2002"]
t = "0202"
s = Solution()
ans = s.openLock(d, t)
print('right answer is 6')
print('my answer is', ans)
