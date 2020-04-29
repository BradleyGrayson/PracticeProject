class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class InorderTraversal:
    def __init__(self):
        # 用于测试的二叉树
        # 该树的前序遍历结果应为: [6, 5, 9, 7, 1, 3, 2, 4, 8]
        self.test = TreeNode(1)
        self.test.left = TreeNode(5)
        self.test.left.left = TreeNode(6)
        self.test.left.right = TreeNode(7)
        self.test.left.right.left = TreeNode(9)
        self.test.right = TreeNode(2)
        self.test.right.left = TreeNode(3)
        self.test.right.right = TreeNode(4)
        self.test.right.right.right = TreeNode(8)
        print('Correct Result is\n[6, 5, 9, 7, 1, 3, 2, 4, 8]\n')

    def basedOnRecurrence(self) -> list:
        root = self.test

        def recurrent(node: TreeNode, _output: list):
            if not node:
                return
            recurrent(node.left, _output)
            _output.append(node.val)
            recurrent(node.right, _output)

        output = []
        recurrent(root, output)
        return output

    def mybasedOnStack(self) -> list:
        root = self.test
        if not root: return []
        stack, output, visited = [], [], []
        stack.append(root)
        visited.append(root)
        while stack:
            if root.left and root.left not in visited:
                root = root.left
                stack.append(root)
                visited.append(root)
            else:
                root = stack.pop()
                output.append(root.val)
                if root.right and root.right not in visited:
                    root = root.right
                    stack.append(root)
                    visited.append(root)
        return output

    def othersbasedonStack(self):
        root = self.test
        stack, output = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return output
            root = stack.pop()
            output.append(root.val)
            root = root.right

    def basedOnMorris(self) -> list:
        root = self.test
        curr, output = root, []
        while curr:
            if not curr.left:
                output.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                tmp = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr
                curr.left = None
                curr = tmp
        return output


binary_tree = InorderTraversal()
output1 = binary_tree.basedOnRecurrence()
print('based on recurrence:\n{}\n'.format(output1))
output2 = binary_tree.mybasedOnStack()
print('my based on stack(iteration):\n{}\n'.format(output2))
output3 = binary_tree.othersbasedonStack()
print('others based on stack(iteration):\n{}\n'.format(output3))
output4 = binary_tree.basedOnMorris()
print('based on Morris:\n{}'.format(output4))
