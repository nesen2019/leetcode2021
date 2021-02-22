"""
# 题目描述

# 程序标准结构
class Solution:
    def add(self, a, b):


"""

from cleetcode.ctest.utils import decorator_default

@decorator_default("add")
def ctest(method_name, class_name):
    return f"""
    >>> a = 2
    >>> b = 3
    >>> res = {class_name}().{method_name}(a, b) 
    >>> assert res == a+b, f"error res : {{res}}"
    """


class Solution:

    def add(self, a, b):
        return a + b

    def add01(self, a, c):
        return a+c

# Solution.__doc__ = ctest()
Solution.__doc__ = ctest("add01")
Solution.add.__doc__ = ctest("add")
Solution.add01.__doc__ = ctest("add01")

if __name__ == '__main__':
    print(__doc__)
    import doctest

    doctest.testmod()

