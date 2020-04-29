class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class MyLinkedList1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0: return -1
        node = self.head
        for _ in range(index + 1):
            if node.next is not None:
                node = node.next
            else:
                return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        node = self.head
        for _ in range(index):
            if node.next:
                node = node.next
            else:
                return
        if node:
            further = node.next
            node.next = Node(val)
            node.next.next = further

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0: return
        node = self.head
        for _ in range(index):
            if node.next:
                node = node.next
        if node.next:
            node.next = node.next.next


class MyLinkedList2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)

    def size(self):
        cnt = 0
        cur = self.head.next
        while cur:
            cur = cur.next
            cnt += 1
        return cnt

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
            if not cur:
                return -1
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        tmp = self.head.next
        self.head.next = Node(val)
        self.head.next.prev = self.head
        self.head.next.next = tmp
        if tmp:
            tmp.prev = self.head.next

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        tobeadd = Node(val)
        cur = self.head.next
        while cur and cur.next:
            cur = cur.next
        cur.next = tobeadd
        tobeadd.prev = cur
        tobeadd.next = None

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        cur = self.head

        if index > self.size():
            return

        for _ in range(index):
            if not cur:
                return
            cur = cur.next
        new = Node(val)
        new.prev = cur
        new.next = cur.next
        if cur.next:
            cur.next.prev = new
        cur.next = new

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        cur = self.head

        for _ in range(index + 1):
            if not cur:
                return
            cur = cur.next
        cur.prev.next = cur.next


# Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList2()
linkedList.addAtHead(1)
print(linkedList.head.val, linkedList.head.next.val, linkedList.head.next.next)
linkedList.addAtTail(3)
print(linkedList.head.val, linkedList.head.next.val, linkedList.head.next.next.val, linkedList.head.next.next.next)
linkedList.addAtIndex(1, 2)   # 链表变为1-> 2-> 3
print(linkedList.head.val,
      linkedList.head.next.val,
      linkedList.head.next.next.val,
      linkedList.head.next.next.next.val,
      linkedList.head.next.next.next.next)
linkedList.get(1)             # 返回2
linkedList.deleteAtIndex(1)   # 现在链表是1-> 3
linkedList.get(1)             # 返回3
