'''
16.3Sum Closest
16.3Sum Closest
<p>给定一个包括&nbsp;<em>n</em> 个整数的数组&nbsp;<code>nums</code><em>&nbsp;</em>和 一个目标值&nbsp;<code>target</code>。找出&nbsp;<code>nums</code><em>&nbsp;</em>中的三个整数，使得它们的和与&nbsp;<code>target</code>&nbsp;最接近。返回这三个数的和。假定每组输入只存在唯一答案。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>nums = [-1,2,1,-4], target = 1
<strong>输出：</strong>2
<strong>解释：</strong>与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10^3</code></li>
	<li><code>-10^3&nbsp;&lt;= nums[i]&nbsp;&lt;= 10^3</code></li>
	<li><code>-10^4&nbsp;&lt;= target&nbsp;&lt;= 10^4</code></li>
</ul>

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
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
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()