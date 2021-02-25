"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

通过次数352,475提交次数465,180

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

"""

from cleetcode.ctest.utils import decorator_default
from cleetcode.structures import TreeNode, HandleTreeTwo


@decorator_default("maxDepth")
def ctest(method_name, class_name):
    return f"""
    >>> root = HandleTreeTwo([3,9,20,"#","#",15,7]).data_root
    >>> {class_name}().{method_name}(root)
    3
    """


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0

    def maxDepth01(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(rot, k):
            if rot:
                dfs(rot.left, k + 1)
                dfs(rot.right, k + 1)
            else:
                self.res = max(self.res, k)

        dfs(root, 0)
        return self.res

    def maxDepth02(self, root: TreeNode) -> int:
        if root:
            return max(self.maxDepth02(root.left), self.maxDepth02(root.right)) + 1
        else:
            return 0


Solution.__doc__ = ctest()
Solution.maxDepth01.__doc__ = ctest("maxDepth01")
Solution.maxDepth02.__doc__ = ctest("maxDepth02")

if __name__ == '__main__':
    import doctest

    doctest.testmod()
