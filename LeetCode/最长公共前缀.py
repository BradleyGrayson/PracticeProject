class Solution:
    # 自己实现的解法
    def longestCommonPrefix1(self, strs: list) -> str:
        strs_length = [len(i) for i in strs]
        least = strs[strs_length.index(min(strs_length))]
        # if not least:
        #     return ''

        public = ''
        for char in least:
            public += char
            for i, s in enumerate(strs):
                if not s.startswith(public):
                    return public[:-1]
                if i == len(strs)-1 and public == least and s.startswith(public):
                    return public
        return ''

    # 利用字符串排序的方法
    def longestCommonPrefix2(self, strs: list) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        public = ''
        strs.sort()
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                public += x
            else:
                break
        return public


s = Solution()
print('correct: fl, my answer:', s.longestCommonPrefix2(["flower", "flow", "flight", 'flows']))
print('correct: \'\', my answer:', s.longestCommonPrefix2(["dog", "racecar", "car"]))
print('correct: a , my answer:', s.longestCommonPrefix2(['a']))
