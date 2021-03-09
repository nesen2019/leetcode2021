'''
14.Longest Common Prefix
14.Longest Common Prefix
<p>编写一个函数来查找字符串数组中的最长公共前缀。</p>

<p>如果不存在公共前缀，返回空字符串 <code>""</code>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>strs = ["flower","flow","flight"]
<strong>输出：</strong>"fl"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>strs = ["dog","racecar","car"]
<strong>输出：</strong>""
<strong>解释：</strong>输入不存在公共前缀。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= strs.length <= 200</code></li>
	<li><code>0 <= strs[i].length <= 200</code></li>
	<li><code>strs[i]</code> 仅由小写英文字母组成</li>
</ul>

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
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
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()