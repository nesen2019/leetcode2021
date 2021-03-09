'''
175.Combine Two Tables
175.Combine Two Tables
<p>表1: <code>Person</code></p>

<pre>+-------------+---------+
| 列名         | 类型     |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId 是上表主键
</pre>

<p>表2: <code>Address</code></p>

<pre>+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId 是上表主键
</pre>

<p>&nbsp;</p>

<p>编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供&nbsp;person 的以下信息：</p>

<p>&nbsp;</p>

<pre>FirstName, LastName, City, State
</pre>

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