'''
46.Permutations
46.Permutations
<p>给定一个<strong> 没有重复</strong> 数字的序列，返回其所有可能的全排列。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [1,2,3]
<strong>输出:</strong>
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]</pre>

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()