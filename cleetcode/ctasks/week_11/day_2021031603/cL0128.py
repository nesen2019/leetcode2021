'''
128.Longest Consecutive Sequence
128.Longest Consecutive Sequence
<p>给定一个未排序的整数数组 <code>nums</code> ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。</p>

<p> </p>

<p><strong>进阶：</strong>你可以设计并实现时间复杂度为 <code>O(n)</code><em> </em>的解决方案吗？</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [100,4,200,1,3,2]
<strong>输出：</strong>4
<strong>解释：</strong>最长数字连续序列是 <code>[1, 2, 3, 4]。它的长度为 4。</code></pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,3,7,2,5,8,4,6,0,1]
<strong>输出：</strong>9
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= nums.length <= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
</ul>

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
    def longestConsecutive(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()