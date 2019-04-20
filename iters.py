import time
def what_is_an_iterator():
    print("At it's core, an iterator is an object with 2 specific methods: \
            `__next__` and `__iter__`")
    input()
    print("An iterator is an object which will give you one item at a time, \
            and stop when there are no items left to give")
    input()
    print("An example of an iterator is a list")
    input()
    my_list = [1, 2, 3, 5, 4]
    print(f"My List: {my_list}")
    for item in my_list:
        print(f"item: {item}")
    print("End of iteration")
    input()
    print("Notice how `item` is each element in the list one at a time")
    print("When you use a for loop you use an iterator")

class MyIterator:
    """This class takes an iterator and filters out any
    0 items inside it. If the item cannot be compared with 0 it will
    raise an exception.

    No further modifications to the iterator are made.
    Will not properly clean up the iterator or stream, or
    attempt to stop a stream of 0s. It will block forever.

    Don't actually use this
    """
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.iterable:
            if item == 0:
                pass
            else: 
                return item
        
        raise StopIteration

class Fibonaccirator:
    """An iterator that produces the fibonacci sequence"""
    def __init__(self, max):                      
        self.max = max

    def __iter__(self):                           
        self.a = 0
        self.b = 1
        return self

    def __next__(self):                           
        fib = self.a
        if fib > self.max:
            raise StopIteration                   
        self.a, self.b = self.b, self.a + self.b
        return fib

def fibonacci(max):
    """This is a `generator` function, a generator is a generalized
    iterator. Instead of returning a single value it will `yield`
    values. On it's first iteration it will run up to the yield
    point. After that it will continue after the last yield point
    and keep going. In this case, it stays inside the while loop, 
    also the local variables will stay defined
    """
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    s = MyIterator([1, 0, 2, 0, 5, 0, 3, 0, 0, 6])
    for item in s:
        print(item)
    print("End iteration")
