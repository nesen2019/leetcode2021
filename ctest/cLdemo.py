"""
# 题目描述

# 程序标准结构
class Solution:
    def add(self, a, b):


"""

__ctest__ = """
# 通过的示例
    >>> a = 2
    >>> b = 3
    >>> res = Solution().add(a, b)
    >>> assert res == a+b, f"error res: {res}"
"""


class Solution:
    __doc__ = __ctest__

    def add(self, a, b):
        return a + b


if __name__ == '__main__':
    import doctest

    doctest.testmod()
