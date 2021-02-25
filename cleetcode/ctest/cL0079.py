"""
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false


提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
通过次数140,717提交次数319,061
在真实的面试中遇到过这道题？

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
"""

from typing import List
from cleetcode.ctest.utils import decorator_default


@decorator_default("exist")
def ctest(method_name, class_name):
    return f"""
    >>> board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    >>> res = {class_name}().{method_name}(board, "ABCCED")
    >>> res 
    True
    >>> {class_name}().{method_name}(board, "SEE")
    True
    >>> {class_name}().{method_name}(board, "ABCB")
    False
    
    """


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):

        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        temp = board[i][j]
        board[i][j] = "0"
        res = (self.dfs(board, i + 1, j, word[1:])
               or self.dfs(board, i - 1, j, word[1:])
               or self.dfs(board, i, j + 1, word[1:])
               or self.dfs(board, i, j - 1, word[1:]))

        board[i][j] = temp
        return res


Solution.__doc__ = ctest()

if __name__ == '__main__':
    import doctest

    doctest.testmod()
