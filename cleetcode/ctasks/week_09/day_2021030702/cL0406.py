'''
406.Queue Reconstruction by Height
406.Queue Reconstruction by Height
<p>假设有打乱顺序的一群人站成一个队列，数组 <code>people</code> 表示队列中一些人的属性（不一定按顺序）。每个 <code>people[i] = [h<sub>i</sub>, k<sub>i</sub>]</code> 表示第 <code>i</code> 个人的身高为 <code>h<sub>i</sub></code> ，前面 <strong>正好</strong> 有 <code>k<sub>i</sub></code><sub> </sub>个身高大于或等于 <code>h<sub>i</sub></code> 的人。</p>

<p>请你重新构造并返回输入数组 <code>people</code> 所表示的队列。返回的队列应该格式化为数组 <code>queue</code> ，其中 <code>queue[j] = [h<sub>j</sub>, k<sub>j</sub>]</code> 是队列中第 <code>j</code> 个人的属性（<code>queue[0]</code> 是排在队列前面的人）。</p>

<p> </p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
<strong>输出：</strong>[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
<strong>解释：</strong>
编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
<strong>输出：</strong>[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= people.length <= 2000</code></li>
	<li><code>0 <= h<sub>i</sub> <= 10<sup>6</sup></code></li>
	<li><code>0 <= k<sub>i</sub> < people.length</code></li>
	<li>题目数据确保队列可以被重建</li>
</ul>

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
'''

from typing import List
from cleetcode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):  
    return f"""
    
    >>> 
    >>> res = {class_name}().{method_name}()
    """


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()