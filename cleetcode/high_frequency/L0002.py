'''
2.Add Two Numbers
2.Add Two Numbers
<p>给你两个 <strong>非空</strong> 的链表，表示两个非负的整数。它们每位数字都是按照 <strong>逆序</strong> 的方式存储的，并且每个节点只能存储 <strong>一位</strong> 数字。</p>

<p>请你将两个数相加，并以相同形式返回一个表示和的链表。</p>

<p>你可以假设除了数字 0 之外，这两个数都不会以 0 开头。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>输入：</strong>l1 = [2,4,3], l2 = [5,6,4]
<strong>输出：</strong>[7,0,8]
<strong>解释：</strong>342 + 465 = 807.
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>l1 = [0], l2 = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>输出：</strong>[8,9,9,9,0,0,0,1]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>每个链表中的节点数在范围 <code>[1, 100]</code> 内</li>
	<li><code>0 <= Node.val <= 9</code></li>
	<li>题目数据保证列表表示的数字不含前导零</li>
</ul>

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
'''

from typing import List
from cleetcode.structures import ListNode, HandleLink
from cleetcode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""

    >>> l1 = HandleLink([1,4,2]).data_root
    >>> l2 = HandleLink([5,2,3]).data_root
    >>> res = {class_name}().{method_name}(l1, l2)
    >>> HandleLink(res).data_list
    [6, 6, 5]
    
    >>> l1 = HandleLink([0]).data_root
    >>> l2 = HandleLink([0]).data_root
    >>> res = {class_name}().{method_name}(l1, l2)
    >>> HandleLink(res).data_list
    [0]

    >>> l1 = HandleLink([9,9,9,9,9,9,9]).data_root
    >>> l2 = HandleLink([9,9,9,9]).data_root
    >>> res = {class_name}().{method_name}(l1, l2)
    >>> HandleLink(res).data_list
    [8, 9, 9, 9, 0, 0, 0, 1]

    """


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = None
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + carry

            if head:
                tail.next = ListNode(sum % 10)
                tail = tail.next
            else:
                head = tail = ListNode(sum % 10)
            carry = sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            tail.next = ListNode(carry)
        return head


Solution.addTwoNumbers.__doc__ = ctest("addTwoNumbers")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
