'''
948.Sort an Array
912.Sort an Array
<p>给你一个整数数组&nbsp;<code>nums</code>，请你将该数组升序排列。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [5,2,3,1]
<strong>输出：</strong>[1,2,3,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [5,1,1,2,0,0]
<strong>输出：</strong>[0,0,1,1,2,5]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= nums.length &lt;= 50000</code></li>
	<li><code>-50000 &lt;= nums[i] &lt;= 50000</code></li>
</ol>

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
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
    def sortArray(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()