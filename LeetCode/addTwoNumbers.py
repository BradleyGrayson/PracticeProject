# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        value = l1.val + l2.val
        l3 = ListNode(value % 10)
        l3.next = ListNode(value // 10)

        p1 = l1.next
        p2 = l2.next
        p3 = l3

        while True:
            if p1 and p2:
                value = p1.val + p2.val + p3.next.val
                p3.next.val = value % 10
                p3.next.next = ListNode(value // 10)
                p3 = p3.next
                p1 = p1.next
                p2 = p2.next
            elif p1 and not p2:
                value = p1.val + p3.next.val
                p3.next.val = value % 10
                p3.next.next = ListNode(value // 10)
                p3 = p3.next
                p1 = p1.next
            elif not p1 and p2:
                value = p2.val + p3.next.val
                p3.next.val = value % 10
                p3.next.next = ListNode(value // 10)
                p3 = p3.next
                p2 = p2.next
            else:
                if p3.next.val == 0:
                    p3.next = None
                break
        return l3

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        l3 = result
        add = 0
        while l1 and l2:
            value = l1.val + l2.val + add
            l3.next = ListNode(value % 10)
            add = value // 10
            l3, l1, l2 = l3.next, l1.next, l2.next
        l1 = l1 if l1 else l2
        while add:
            if l1:
                value = l1.val + add
                add = value // 10
                l3.next = ListNode(value % 10)
                l3, l1 = l3.next, l1.next
            else:
                l3.next = ListNode(add)
                l3 = l3.next
                break
        l3.next = l1
        return result.next



s = Solution()
l1 = ListNode(0)
l1.next = ListNode(6)
l1.next.next = ListNode(7)

l2 = ListNode(8)
l2.next = ListNode(5)
l2.next.next = ListNode(2)
# l2.next.next.next = ListNode(9)
# l2.next.next.next.next = ListNode(1)

res = s.addTwoNumbers2(l1, l2)
while res != None:
    print(res.val)
    res = res.next