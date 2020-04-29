class Solution:
    def decodeString(self, s: str) -> str:
        # stack和nums是同步的，二者元素两两对应
        stack = []
        nums = []
        output = ''
        i = 0

        while i < len(s):
            # 如果碰到了字母，就直接将该字母串加到output里，注意要分栈是否为空的情况
            if s[i].isalpha():
                # 如果栈为空，则说明没有嵌套，可以直接加
                if not stack:
                    tmp_alp = ''
                    while i < len(s) and s[i].isalpha():
                        tmp_alp += s[i]
                        i += 1
                    output += tmp_alp
                # 如果栈不为空，则说明有嵌套，要将栈的最后一个字符串进行更新
                else:
                    tmp_alp = ''
                    while i < len(s) and s[i].isalpha():
                        tmp_alp += s[i]
                        i += 1
                    stack[-1] += tmp_alp

            # 如果碰到了数字，就开始堆栈
            if i < len(s) and s[i].isnumeric():
                tmp_num = ''
                # 一直向下找，直到找完和该数字相连的所有数字
                while i < len(s) and s[i].isnumeric():
                    tmp_num += s[i]
                    i += 1
                nums.append(int(tmp_num))
                # 字母索引+1是'['，再+1一定是字母
                i += 1
                tmp_alp = ''
                # 一直向下找，知道找完和该字母相连的所有字母
                while i < len(s) and s[i].isalpha():
                    tmp_alp += s[i]
                    i += 1
                stack.append(tmp_alp)

            # 如果碰到了']'，就开始出栈
            if i < len(s) and s[i] == ']':
                tmp_alp = stack.pop()
                tmp_num = nums.pop()
                tmp_output = tmp_alp * tmp_num
                if stack:
                    stack[-1] += tmp_output
                else:
                    output += tmp_output
                i += 1

        return output


input = "a2[bc]2[a2[bc]]2[de]f"
s = Solution()
print('Correct answer: abcbcabcbcabcbcdedef'.rjust(45))
print('my answer: {}'.format(s.decodeString(input)).rjust(45))
print('same: ', 'abcbcabcbcabcbcdedef' == s.decodeString(input))
