'''
18.4Sum
18.4Sum
<p>给定一个包含 <em>n</em> 个整数的数组 <code>nums</code> 和一个目标值 <code>target</code>，判断 <code>nums</code> 中是否存在四个元素 <em>a，</em><em>b，c</em> 和 <em>d</em> ，使得 <em>a</em> + <em>b</em> + <em>c</em> + <em>d</em> 的值与 <code>target</code> 相等？找出所有满足条件且不重复的四元组。</p>

<p><strong>注意：</strong>答案中不可以包含重复的四元组。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,-1,0,-2,2], target = 0
<strong>输出：</strong>[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [], target = 0
<strong>输出：</strong>[]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= nums.length <= 200</code></li>
	<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code></li>
</ul>

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()