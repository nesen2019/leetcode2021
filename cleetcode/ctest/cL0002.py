"""
2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。



示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]


提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
通过次数715,143提交次数1,808,199


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:


"""

from cleetcode import structures
from cleetcode.ctest.utils import decorator_default

ListNode = structures.ListNode
HandleLink = structures.HandleLink


@decorator_default("addTwoNumbers")
def ctest(method_name, class_name):
    return f"""
    >>> l1 = HandleLink([2,4,3]).data_root 
    >>> l2 = HandleLink([5,6,4]).data_root 
    >>> res = {class_name}().{method_name}(l1, l2) 
    >>> assert HandleLink.equal_root(res, HandleLink([7,0,8]).data_root), f"error res: {{res}}"

    """


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = self.dfs(l1, l2, 0)
        return root

    def dfs(self, l, r, i):
        if l is None and r is None and i == 0:
            return None
        sum = (l.val if l else 0) + (r.val if r else 0) + i
        node = ListNode(sum % 10)
        node.next = self.dfs(l.next if l else None, r.next if r else None, sum // 10)
        return node


Solution.__doc__ = ctest()

if __name__ == '__main__':
    import doctest

    doctest.testmod()

if __name__ == '__main__asd':
    l1 = HandleLink([2, 4, 3]).data_root
    l2 = HandleLink([5, 6, 4]).data_root
    res = Solution().addTwoNumbers(l1, l2)
