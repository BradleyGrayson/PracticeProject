class Solution:
    def strStr1(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1

        flag = False
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i] == needle[0]:
                for j in range(1, len(needle)):
                    if haystack[i+j] == needle[j]:
                        flag = True
                    else:
                        flag = False
                        break
                if flag == True:
                    return i
        return -1


s = Solution()
h = "mississippi"
n = "issipi"
print('haystack={}, n={}, match:{}'.format(h, n, s.strStr2(h, n)))