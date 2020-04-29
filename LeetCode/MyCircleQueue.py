# 使用字典存储
# class MyCircularQueue:
#
#     def __init__(self, k: int):
#         """
#         Initialize your data structure here. Set the size of the queue to be k.
#         """
#         self.max_size = k
#         self.curr_size = 0
#         self.head = None
#         self.tail = None
#         self.__queue = {}
#         for index in range(self.max_size):
#             self.__queue[index] = None
#
#     def enQueue(self, value: int) -> bool:
#         """
#         Insert an element into the circular queue. Return true if the operation is successful.
#         """
#         if self.isEmpty():
#             self.head = self.tail = 0
#             self.__queue[self.tail] = value
#             return True
#         elif self.isFull():
#             return False
#         else:
#             self.tail = (self.tail + 1) % self.max_size
#             self.__queue[self.tail] = value
#             return True
#
#     def deQueue(self) -> bool:
#         """
#         Delete an element from the circular queue. Return true if the operation is successful.
#         """
#         if self.isEmpty():
#             return False
#         if self.head == self.tail:
#             self.__queue[self.head] = None
#             self.head = self.tail = None
#         else:
#             self.__queue[self.head] = None
#             self.head = (self.head + 1) % self.max_size
#         return True
#
#     def Front(self) -> int:
#         """
#         Get the front item from the queue.
#         """
#         if self.isEmpty():
#             return -1
#         return self.__queue[self.head]
#
#     def Rear(self) -> int:
#         """
#         Get the last item from the queue.
#         """
#         if self.isEmpty():
#             return -1
#         return self.__queue[self.tail]
#
#     def isEmpty(self) -> bool:
#         """
#         Checks whether the circular queue is empty or not.
#         """
#         if self.head is None and self.tail is None:
#             return True
#         return False
#
#     def isFull(self) -> bool:
#         """
#         Checks whether the circular queue is full or not.
#         """
#         if self.head is None and self.tail is None:
#             return False
#         else:
#             if self.head - self.tail == 1 or self.tail - self.head == self.max_size - 1:
#                 return True
#         return False


# 使用列表存储
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.max = k + 1
        self.head = 0
        self.tail = 0
        self.queue = [None] * self.max

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == self.tail

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.tail + 1) % self.max == self.head

# obj = MyCircularQueue(3)
# param_1 = obj.enQueue(1)
# print(param_1)
# print(obj.head)
# param_1 = obj.enQueue(2)
# print(param_1)
# print(obj.head)
# param_1 = obj.enQueue(3)
# print(param_1)
# param_1 = obj.enQueue(4)
# print(param_1)
# param_2 = obj.deQueue()
# print(param_2)
# param_3 = obj.Front()
# print(param_3)
# param_4 = obj.Rear()
# print(param_4)
# param_5 = obj.isEmpty()
# print(param_5)
# param_6 = obj.isFull()
# print(param_6)
