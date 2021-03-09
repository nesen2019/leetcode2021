'''
3.Longest Substring Without Repeating Characters
description
class Solution: pass

'''

from cleetcode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):  
    return f"""
    
    >>> 
    >>> res = {class_name}().{method_name}()
    """


class Solution: pass

if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()