"""
归并排序

###############

class Solution:
    def merge_sort(self, nums):


"""

from cleetcode.ctest.utils import decorator_default


@decorator_default("merge_sort")
def ctest(method_name, class_name):
    return f"""
    >>> nums = [2, 4, 1, 3]
    >>> res = {class_name}().{method_name}(nums)
    >>> assert res == sorted(nums), f"error res: {{res}}"

    >>> import random 
    >>> nums = [random.randint(0, 10) for _ in range(9)] 
    >>> res = {class_name}().{method_name}(nums)
    >>> assert res == sorted(nums), f"error res: {{res}}"

    >>> import random 
    >>> nums = [random.randint(0, 100000) for _ in range(9999)] 
    >>> res = {class_name}().{method_name}(nums)
    >>> assert res == sorted(nums), f"error res: {{res}}"

    """


class Solution:
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


Solution.__doc__ = ctest()

if __name__ == '__main__':
    import doctest

    doctest.testmod()
