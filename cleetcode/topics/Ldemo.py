from cleetcode.ctest import cLdemo


class Solution:
    __doc__ = cLdemo.__ctest__

    def add(self, a, b):
        return a + b


if __name__ == '__main__':
    import doctest

    doctest.testmod()
