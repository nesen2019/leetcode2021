"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
通过次数833,084提交次数2,287,908

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

"""

__ctest__ = """
>>> s = "abcabcbb"
>>> res = Solution().lengthOfLongestSubstring(s)
>>> assert res == 3, f"error res: {res}"

>>> s = "bbbbb"
>>> res = Solution().lengthOfLongestSubstring(s)
>>> assert res == 1, f"error res: {res}"

>>> s = "pwwkew"
>>> res = Solution().lengthOfLongestSubstring(s)
>>> assert res == 3, f"error res: {res}"

>>> s = ""
>>> res = Solution().lengthOfLongestSubstring(s)
>>> assert res == 0, f"error res: {res}"


"""


class Solution:
    __doc__ = __ctest__

    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, length, result = [0] * 4
        len_s = len(s)
        while end < len_s:
            temp = s[end]
            for i in range(start, end):
                if temp == s[i]:
                    start = i + 1
                    length = end - start
                    break
            end += 1
            length += 1
            result = max(result, length)
        return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
