"""
78. 子集

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：

输入：nums = [0]
输出：[[],[0]]



提示：

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    nums 中的所有元素 互不相同

通过次数201,014
提交次数252,615

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
"""

from typing import List
from cleetcode.ctest.utils import decorator_default, equal_list_random_no_reply


@decorator_default("subsets")
def ctest(method_name, class_name):
    return f"""
    >>> nums = [1,2,3]
    >>> res = {class_name}().{method_name}(nums)
    >>> res_true = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    >>> equal_list_random_no_reply(res, res_true)
    True

    >>> nums = [0]
    >>> res = {class_name}().{method_name}(nums)
    >>> res_true = [[],[0]]
    >>> equal_list_random_no_reply(res, res_true)
    True
    """


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        t = list()
        ans = list()

        def dfs(cur, ns):
            if cur == len(ns):
                ans.append(t[:])
                return

            t.append(ns[cur])
            dfs(cur + 1, ns)

            t.pop()
            dfs(cur + 1, ns)

        dfs(0, nums)
        return ans


Solution.__doc__ = ctest()

if __name__ == '__main__':
    import doctest

    doctest.testmod()
