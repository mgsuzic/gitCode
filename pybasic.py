#coding: utf-8

#列表
#字典
#生成器
def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

for i in fib(10):
    print i
print fib(10)

#遍历
colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors):
    print(i, '-->', color)

list_a = ['a', 'b', 'c', 'd']
list_b = [1, 2, 3]
for letter, number in zip(list_a, list_b):
    print(letter, number)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)

list_example = [i for i in range(5)]
iter_example = (i for i in range(5))
set_example = {i for i in range(5)}
print iter_example
print(set_example)

for i in reversed(list_example):
    print(i)

print "==="
class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    def __resersed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
x1 = Countdown(6)
for i in x1.__resersed__():
    print i

#装饰器:装饰器就是一个能够返回可调用对象（函数）的可调用对象（函数）。
def decorator(F):
    print "I am decorator"
    return F

@decorator
def foo():
    print "hello, world!"
#上面等价于foo = decorator(foo)
#foo()
"""
I'm decorator
Hello World!
"""
#decorator(foo)()
"""
I'm decorator
Hello World!
"""

#上下文管理:在代码执行前，先进行准备工作，执行完成后，再做收尾工作
class ReadFile(object):
    def __init__(self, filename):
        self.file = open(filename, 'r')
    def __enter__(self):
        return self.file
    def __exit__(self, type, value, traceback):
        '''type, value, traceback 分别代表错误的类型、值、追踪栈'''
        self.file.close()
        return True
# with 语句先暂存了 ReadFile 类的 __exit__ 方法
# 然后调用 __enter__ 方法，并将结果返回给 with 语句
# 读取完成后调用之前暂存的 __exit__ 方法，关闭了文件
with ReadFile('pybasic.py') as file_read:
    for line in file_read.readlines():
        print(line)

if __name__ == "__main__":
    foo()
    print "---"
    decorator(foo)()
    pass

