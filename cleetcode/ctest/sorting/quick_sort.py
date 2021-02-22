"""
快速排序

#################3

class Solution:
    def quick_sort(self, nums):


"""

from cleetcode.ctest.utils import decorator_default


@decorator_default("quick_sort")
def ctest(method_name, class_name):
    return f"""
    >>> nums = [2,3,1,4]
    >>> res_true = sorted(nums)
    >>> res = {class_name}().{method_name}(nums)
    >>> assert res == res_true, f"error res: {{res}}"

    >>> import random
    >>> nums = [random.randint(0, 10) for _ in range(10)]
    >>> res_true = sorted(nums)
    >>> res = {class_name}().{method_name}(nums)
    >>> assert res == res_true, f"error res: {{res}}"

    >>> import random
    >>> nums = [random.randint(0, 100000) for _ in range(99999)]
    >>> res_true = sorted(nums)
    >>> res = {class_name}().{method_name}(nums)
    >>> assert res == res_true, f"error res: {{res}}"
    """


class Solution:

    def quick_sort(self, nums):

        if len(nums) < 2:
            return nums

        pivot = nums.pop()
        greater = list()
        lesser = list()

        for element in nums:
            (greater if element > pivot else lesser).append(element)

        return self.quick_sort(lesser) + [pivot] + self.quick_sort(greater)


Solution.__doc__ = ctest()

if __name__ == '__main__':
    import doctest

    doctest.testmod()
