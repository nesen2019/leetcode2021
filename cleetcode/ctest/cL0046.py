"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
通过次数257,424提交次数331,603


from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

"""

from cleetcode.ctest.utils import decorator_default


@decorator_default("permute")
def ctest(method_name, class_name):
    return f"""
    >>> import itertools 
    >>> nums = [1,2,3] 
    >>> res = {class_name}().{method_name}(nums) 
    >>> assert 
    """


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                print(first, i, nums)
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
                print("    ",first, i, nums)

        n = len(nums)
        res = []
        backtrack()
        return res


if __name__ == '__main__as':
    import doctest

    doctest.testmod()


if __name__ == '__main__':
    res = Solution().permute([1, 2, 3,4])
