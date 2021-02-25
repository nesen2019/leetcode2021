"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]


提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
通过次数223,968提交次数400,240

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


"""

from typing import List
from cleetcode.ctest.utils import decorator_default, equal_list_random_no_reply


@decorator_default("letterCombinations")
def ctest(method_name, class_name):
    return f"""
    >>> digits = "23"
    >>> res = {class_name}().{method_name}(digits)
    >>> res_true = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    >>> assert len(res_true) == len(set(res))
    >>> for i in set(res):
    ...     if i not in res_true:
    ...         print("False")
    ...

    >>> digits = ""
    >>> {class_name}().{method_name}(digits)
    []

    >>> digits = "2"
    >>> res = {class_name}().{method_name}(digits)
    >>> res_true = ["a","b","c"]
    >>> equal_list_random_no_reply(res, res_true)
    True
    """


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = list()
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(conbination, nextdigit):
            if nextdigit:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter, nextdigit[1:])
            else:
                res.append(conbination)

        backtrack("", digits)
        return res


Solution.__doc__ = ctest()

if __name__ == '__main__':
    import doctest

    doctest.testmod()
