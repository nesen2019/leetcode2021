"""
堆排序

######################

class Solution:
    def heap_sort(self, nums):


"""

from cleetcode.ctest.utils import decorator_default


@decorator_default("heap_sort")
def ctest(method_name, class_name):
    return f"""
    >>> nums = [2,3,1]
    >>> {class_name}().{method_name}(nums)
    [1, 2, 3]

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

    def heapify(self, nums, index, heap_size):
        greater = index
        left = index * 2 + 1
        right = index * 2 + 2

        if left < heap_size and nums[left] > nums[greater]:
            greater = left

        if right < heap_size and nums[right] > nums[greater]:
            greater = right

        if greater != index:
            nums[index], nums[greater] = nums[greater], nums[index]
            self.heapify(nums, greater, heap_size)

    def heap_sort(self, nums):
        n = len(nums)
        if n < 2:
            return nums
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, i, n)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i)
        return nums


Solution.__doc__ = ctest()

if __name__ == '__main__':
    import doctest

    doctest.testmod()
