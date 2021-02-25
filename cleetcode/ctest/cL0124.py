"""
124. 二叉树中的最大路径和
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。



示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000
通过次数98,421提交次数227,232

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:


"""

from cleetcode.structures import TreeNode, HandleTreeTwo
from cleetcode.ctest.utils import decorator_default


@decorator_default("maxPathSum")
def ctest(method_name, class_name):
    return f"""
    >>> root = HandleTreeTwo([1,2,3]).data_root
    >>> {class_name}().{method_name}(root)
    6

    >>> root = HandleTreeTwo([-10,9,20,"#","#",15,7]).data_root
    >>> {class_name}().{method_name}(root)
    42

    """



class Solution:


    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")

        def calc_max(root):
            if root is None:
                return 0
            l_max = max(calc_max(root.left), 0)
            r_max = max(calc_max(root.right), 0)
            self.res = max(self.res, root.val + l_max + r_max)
            return max(l_max, r_max) + root.val

        calc_max(root)
        return self.res


Solution.__doc__ = ctest()

if __name__ == '__main__':
    import doctest

    doctest.testmod()
