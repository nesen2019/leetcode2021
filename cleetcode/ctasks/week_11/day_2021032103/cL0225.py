'''
225.Implement Stack using Queues
225.Implement Stack using Queues
<p>请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通队列的全部四种操作（<code>push</code>、<code>top</code>、<code>pop</code> 和 <code>empty</code>）。</p>

<p>实现 <code>MyStack</code> 类：</p>

<ul>
	<li><code>void push(int x)</code> 将元素 x 压入栈顶。</li>
	<li><code>int pop()</code> 移除并返回栈顶元素。</li>
	<li><code>int top()</code> 返回栈顶元素。</li>
	<li><code>boolean empty()</code> 如果栈是空的，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
</ul>

<p> </p>

<p><strong>注意：</strong></p>

<ul>
	<li>你只能使用队列的基本操作 —— 也就是 <code>push to back</code>、<code>peek/pop from front</code>、<code>size</code> 和 <code>is empty</code> 这些操作。</li>
	<li>你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。</li>
</ul>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>输出：</strong>
[null, null, null, 2, 2, false]

<strong>解释：</strong>
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= x <= 9</code></li>
	<li>最多调用<code>100</code> 次 <code>push</code>、<code>pop</code>、<code>top</code> 和 <code>empty</code></li>
	<li>每次调用 <code>pop</code> 和 <code>top</code> 都保证栈不为空</li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你能否实现每种操作的均摊时间复杂度为 <code>O(1)</code> 的栈？换句话说，执行 <code>n</code> 个操作的总时间复杂度 <code>O(n)</code> ，尽管其中某个操作可能需要比其他操作更长的时间。你可以使用两个以上的队列。</p>

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """


    def top(self) -> int:
        """
        Get the top element.
        """


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
'''

from cleetcode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):  
    return f"""
    
    >>> 
    >>> res = {class_name}().{method_name}()
    """


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """


    def top(self) -> int:
        """
        Get the top element.
        """


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()