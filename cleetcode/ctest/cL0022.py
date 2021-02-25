"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]


提示：

1 <= n <= 8
通过次数230,730提交次数300,142

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

"""

from typing import List
from cleetcode.ctest.utils import decorator_default
import functools

@decorator_default("generateParenthesis")
def ctest(method_name, class_name):
    return f"""
    >>> n = 3
    >>> res = {class_name}().{method_name}(n)
    >>> res_true = ["((()))","(()())","(())()","()(())","()()()"]
    >>> sorted(res) == sorted(res_true) 
    True

    >>> res = {class_name}().{method_name}(1)
    >>> res_true = ["()"]
    >>> res == res_true 
    True

    """


class Solution:
    def generateParenthesis01(self, n: int) -> List[str]:

        ans = list()

        def valid(A):
            bal = 0
            for c in A:
                bal += (1 if c == "(" else -1)
                if bal < 0:
                    return False
            return bal == 0

        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))

            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()

        generate([])
        return ans

    def generateParenthesis02(self, n):
        ans = list()

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans

    @functools.lru_cache()
    def generateParenthesis(self, n):

        if n == 0:
            return [""]

        ans = list()
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-c-1):
                    ans.append(f"({left}){right}")
        return ans


Solution.generateParenthesis01.__doc__ = ctest("generateParenthesis01")
Solution.generateParenthesis02.__doc__ = ctest("generateParenthesis02")
Solution.generateParenthesis.__doc__ = ctest("generateParenthesis")

if __name__ == '__main__as':
    c = Solution()
    print(c.generateParenthesis01(3))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
