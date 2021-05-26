'''
9.Palindrome Number
9.Palindrome Number
<p>给你一个整数 <code>x</code> ，如果 <code>x</code> 是一个回文整数，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，<code>121</code> 是回文，而 <code>123</code> 不是。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 121
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>x = -121
<strong>输出：</strong>false
<strong>解释：</strong>从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>x = 10
<strong>输出：</strong>false
<strong>解释：</strong>从右向左读, 为 01 。因此它不是一个回文数。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>x = -101
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你能不将整数转为字符串来解决这个问题吗？</p>

class Solution:
    def isPalindrome(self, x: int) -> bool:
'''

from cleetcode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    >>> res = {class_name}().{method_name}(12321)
    >>> res
    True

    >>> res = {class_name}().{method_name}(-1221)
    >>> res
    False

    >>> res = {class_name}().{method_name}(0)
    >>> res
    True


    """


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10
        return x == reverted or (x == reverted // 10)


Solution.isPalindrome.__doc__ = ctest("isPalindrome")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
