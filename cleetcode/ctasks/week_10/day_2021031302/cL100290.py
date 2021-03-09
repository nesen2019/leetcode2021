'''
100290.表示数值的字符串 LCOF
剑指 Offer 20.表示数值的字符串 LCOF
<p>请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串&quot;+100&quot;、&quot;5e2&quot;、&quot;-123&quot;、&quot;3.1416&quot;、&quot;-1E-16&quot;、&quot;0123&quot;都表示数值，但&quot;12e&quot;、&quot;1a3.14&quot;、&quot;1.2.3&quot;、&quot;+-5&quot;及&quot;12e+5.4&quot;都不是。</p>

<p>&nbsp;</p>

class Solution:
    def isNumber(self, s: str) -> bool:
'''

from cleetcode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):  
    return f"""
    
    >>> 
    >>> res = {class_name}().{method_name}()
    """


class Solution:
    def isNumber(self, s: str) -> bool:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()