"""
归并排序

###############

class Solution:
    def merge_sort(self, nums):


"""

__ctest__ = """
    >>> nums = [2,3,1]
    >>> Solution().merge_sort(nums)
    [1, 2, 3]

    >>> import random
    >>> nums = [random.randint(0, 10) for _ in range(10)]
    >>> res_true = sorted(nums)
    >>> res = Solution().merge_sort(nums)
    >>> assert res == res_true, f"error res: {res}"

    >>> import random
    >>> nums = [random.randint(0, 100000) for _ in range(99999)]
    >>> res_true = sorted(nums)
    >>> res = Solution().merge_sort(nums)
    >>> assert res == res_true, f"error res: {res}"
"""


class Solution:
    __doc__ = __ctest__

    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums

        def merge(a, b):
            def merge_():
                while a and b:
                    yield (a if a[0] < b[0] else b).pop(0)
                yield from a
                yield from b

            return list(merge_())

        mid = len(nums) // 2
        return merge(self.merge_sort(nums[:mid]), self.merge_sort(nums[mid:]))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
