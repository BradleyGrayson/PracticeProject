class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class PostorderTraversal:
    def __init__(self):
        self.test = TreeNode(1)
        self.test.left = TreeNode(5)
        self.test.left.left = TreeNode(6)
        self.test.left.right = TreeNode(7)
        self.test.left.right.left = TreeNode(9)
        self.test.right = TreeNode(2)
        self.test.right.left = TreeNode(3)
        self.test.right.right = TreeNode(4)
        self.test.right.right.right = TreeNode(8)
        print('Correct Result is\n[6, 9, 7, 5, 3, 8, 4, 2, 1]\n')

    def basedOnRecurrence(self):
        root = self.test

        def recurrent(node: TreeNode, _output: list):
            if not node:
                return
            recurrent(node.left, _output)
            recurrent(node.right, _output)
            _output.append(node.val)

        output = []
        recurrent(root, output)
        return output

    def basedOnStack(self):
        root = self.test
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return output[::-1]


binary_tree = PostorderTraversal()
output1 = binary_tree.basedOnRecurrence()
print('based on recurrence:\n{}\n'.format(output1))
output2 = binary_tree.basedOnStack()
print('based on stack:\n{}\n'.format(output2))