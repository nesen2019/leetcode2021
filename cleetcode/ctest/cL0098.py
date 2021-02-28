"""
98. 验证二叉搜索树

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。

示例 1:

输入:
    2
   / \
  1   3
输出: true

示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

通过次数225,836
提交次数671,948


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

"""

from cleetcode.structures import TreeNode, HandleTreeTwo
from cleetcode.ctest.utils import decorator_default


@decorator_default("isValidBST")
def ctest(method_name, class_name):
    return f"""
    >>> root = HandleTreeTwo([2,1,3]).data_root
    >>> {class_name}().{method_name}(root)
    True
    >>> root = HandleTreeTwo([5,4,6,"#","#",3,7]).data_root
    >>> {class_name}().{method_name}(root)
    False
    """

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def heaper(root, lower, upper):

            if root:
                if root.val <= lower or root.val >= upper:
                    return False

                if not heaper(root.left, lower, root.val):
                    return False

                if not heaper(root.right, root.val, upper):
                    return False


            return True
        return heaper(root, float("-inf"), float("inf"))


Solution.__doc__ = ctest()


if __name__ == '__main__':
    import doctest

    doctest.testmod()


