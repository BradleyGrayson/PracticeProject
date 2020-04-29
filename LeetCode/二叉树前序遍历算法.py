class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class PreorderTraversal:
    def __init__(self):
        # 用于测试的二叉树
        # 该树的前序遍历结果应为: [1, 5, 6, 7, 9, 2, 3, 4, 8]
        self.test = TreeNode(1)
        self.test.left = TreeNode(5)
        self.test.left.left = TreeNode(6)
        self.test.left.right = TreeNode(7)
        self.test.left.right.left = TreeNode(9)
        self.test.right = TreeNode(2)
        self.test.right.left = TreeNode(3)
        self.test.right.right = TreeNode(4)
        self.test.right.right.right = TreeNode(8)
        print('Correct Result is\n[1, 5, 6, 7, 9, 2, 3, 4, 8]\n')

    def basedOnStack(self) -> list:
        """
        基于栈的方法，也可看作是基于迭代的方法
        时间复杂度：每个节点访问一次，O(N)，其中N为节点的个数，也就是树的大小
        空间复杂度：取决于树的结构，最坏情况下将储存整棵树，为O(N)
        :return: 前序遍历的结果列表
        """
        root = self.test
        # 用于存储叶子结点的栈
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            # 右叶子结点先入栈，左叶子结点后入栈
            # 使得左叶子结点先出栈，右叶子结点后出栈
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return output

    def basedOnRecurrence(self) -> list:
        """
        基于递归的方法
        时间复杂度：每个节点访问一次，O(N)
        空间复杂度：O(N)
        :return: 前序遍历的结果列表
        """
        def recurrent(root, _output):
            """
            递归体，需声明于调用前。
            这里没有return _output是因为_output作为list传入参数时相当于引用，
            对_output改变，原本的output也会改变。
            :param root: 当前节点
            :param _output: output可作全局变量置函数外，但调用局部变量似更高效，故设此形参
            :return:
            """
            # 如果该节点为None，则终止该节点的递归循环，否则将该节点添加至输出
            if not root:
                return
            _output.append(root.val)
            # 由于是前序遍历，所以先走左叶子结点，再走右叶子结点
            recurrent(root.left, _output)
            recurrent(root.right, _output)

        output = []
        recurrent(self.test, output)
        return output

    def basedOnMorris(self) -> list:
        """
        莫里斯遍历法较为复杂，算法的思路是从当前节点向下访问先序遍历的前驱节点，每个前驱节点都恰好被访问两次。
        时间复杂度：使用莫里斯遍历时，每个节点访问两次，所以时间复杂度为O(2N)=O(N)
        空间复杂度：莫里斯遍历如果实时输出结果，则空间复杂度是O(1)（我的理解：因为某一时刻仅存储2个节点）
                  而本例中因为需要在output中存储所有节点，所以空间复杂度是O(N)
        :return: 莫里斯遍历的结果列表
        """
        root = self.test
        output = []

        while root:
            if not root.left:
                output.append(root.val)
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(root.val)
                    predecessor.right = root
                    root = root.left
                elif predecessor.right is root:
                    predecessor.right = None
                    root = root.right

        return output


binary_tree = PreorderTraversal()

output1 = binary_tree.basedOnStack()
print('based on stack(iteration):\n{}\n'.format(output1))
output2 = binary_tree.basedOnRecurrence()
print('based on recurrence:\n{}\n'.format(output2))
output3 = binary_tree.basedOnMorris()
print('based on Morris:\n{}'.format(output3))
