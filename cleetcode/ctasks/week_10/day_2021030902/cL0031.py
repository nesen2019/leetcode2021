'''
31.Next Permutation
31.Next Permutation
<p>实现获取 <strong>下一个排列</strong> 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。</p>

<p>如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。</p>

<p>必须<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地 </a></strong>修改，只允许使用额外常数空间。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,1]
<strong>输出：</strong>[1,2,3]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,5]
<strong>输出：</strong>[1,5,1]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>[1]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 100</code></li>
	<li><code>0 <= nums[i] <= 100</code></li>
</ul>

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
'''

from typing import List
from cleetcode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):  
    return f"""
    
    >>> 
    >>> res = {class_name}().{method_name}()
    """


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()