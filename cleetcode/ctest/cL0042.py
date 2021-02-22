"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9


提示：

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
通过次数195,273提交次数359,676

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:


"""

__ctest__ = """
>>> height = [0,1,0,2,1,0,1,3,2,1,2,1]
>>> res = Solution().trap(height) 
>>> assert res == 6, f"error res: {res}"

>>> height = [4,2,0,3,2,5]
>>> res = Solution().trap(height)
>>> assert res == 9, f"error res: {res}"


"""

from typing import List


class Solution:
    __doc__=__ctest__
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        left_max = [height[0]] * len(height)
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [height[-1]] * len(height)
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        ans = 0
        for i in range(len(height)):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


if __name__ == '__main__':
    import doctest

    doctest.testmod()
