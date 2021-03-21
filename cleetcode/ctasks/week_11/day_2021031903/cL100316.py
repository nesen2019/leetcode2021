'''
100316.第一个只出现一次的字符  LCOF
剑指 Offer 50.第一个只出现一次的字符  LCOF
<p>在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。</p>

<p><strong>示例:</strong></p>

<pre>s = &quot;abaccdeff&quot;
返回 &quot;b&quot;

s = &quot;&quot; 
返回 &quot; &quot;
</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>0 &lt;= s 的长度 &lt;= 50000</code></p>

class Solution:
    def firstUniqChar(self, s: str) -> str:
'''

from cleetcode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):  
    return f"""
    
    >>> 
    >>> res = {class_name}().{method_name}()
    """


class Solution:
    def firstUniqChar(self, s: str) -> str:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()