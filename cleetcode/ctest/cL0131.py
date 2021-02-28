"""
131. 分割回文串

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

通过次数64,758
提交次数91,972


from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:


"""


from typing import List
import copy
from cleetcode.ctest.utils import decorator_default

@decorator_default("partition")
def ctest(method_name, class_name):
    return f"""
    >>> s = "aab"
    >>> res = {class_name}().{method_name}(s)
    >>> res
    
    """


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = list()
        if len(s) == 0:
            return res

        stack = list()
        char_array = list(s)

        self.dfs(char_array, 0, len(s), stack, res)
        return res

    def dfs(self, char_array, index, lens, stack, res):
        if index == lens:
            res.append(copy.deepcopy(stack))

            return

        for i in range(index, lens):
            if not self.check_palindrome(char_array, index, i):
                continue
            stack.append("".join(char_array[index:i+1]))
            self.dfs(char_array, i+1, lens, stack, res)
            stack.pop()


    def check_palindrome(self, char_array, left, right):
        while left < right:
            if char_array[left] != char_array[right]:
                return False
            left += 1
            right -= 1
        return True


Solution.__doc__ = ctest()

if __name__ == '__main__':
    # import doctest
    #
    # doctest.testmod()
    c = Solution()
    print(c.partition("aab"))
    a = 1




