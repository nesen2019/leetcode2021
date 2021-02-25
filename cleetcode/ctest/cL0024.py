"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]


提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100


进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

"""

from cleetcode.structures import ListNode, HandleLink
from cleetcode.ctest.utils import decorator_default

@decorator_default("swapPairs")
def ctest(method_name, class_name):
    return f"""
    >>> head = HandleLink([1,2,3,4]).data_root
    >>> res_true = HandleLink([2,1,4,3]).data_root 
    >>> res = {class_name}().{method_name}(head) 
    >>> HandleLink.equal_root(res, res_true) 
    True

    >>> head = HandleLink([1,2,3]).data_root
    >>> res_true = HandleLink([2,1,3]).data_root 
    >>> res = {class_name}().{method_name}(head) 
    >>> HandleLink.equal_root(res, res_true) 
    True


    """


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            temp = head.next
            head.next = self.swapPairs(temp.next)
            temp.next = head
            return temp
        else:
            return head

    def swapPairs01(self, head):
        return self.swapPairs(head)


Solution.__doc__ = ctest()

Solution.swapPairs01.__doc__ = ctest("swapPairs01")

if __name__ == '__main__':
    import doctest

    doctest.testmod()



