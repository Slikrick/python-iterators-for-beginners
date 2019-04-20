###########################
#
# What is an iterator?
#
###########################
#
# At it's core, an iterator is an object with state that returns a value
# one at a time when next() is called on it (next internally calls the
# internal __next__() method which iterators must define.
#
# For something to be iterable means that you can create an iterator from it
# Lists, sets, dictionaries are all iterable, but are not directly iterators
# Iterables produce an iterator by calling iter() on them (this calls
# __iter__() on the underlying object.
#
# For completeness sake, all iterators are iterable, and are expected to
# return themselves in their __iter__ implementation.
#
# Iterable -> iter() -> iterator -> next() -> item
#
# Iterators are a powerful concept that are core to a lot of the way python works

class MyIterator:
    """This class takes an iterable and filters out any
    0 items inside it. If the item cannot be compared with 0 it will
    raise an exception.

    No further modifications to the iterator are made.
    Will not properly clean up the iterator or stream, or
    attempt to stop a stream of 0s. It will block forever.

    Don't actually use this
    """
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        self.iterator = iter(self.iterable)
        return self

    def __next__(self):
        for item in self.iterator:
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
    fib = Fibonaccirator(100)
    for i in fib:
        print(i)
    print("End iteration")
    print("Generator fib")
    for i in fibonacci(100):
        print(i)
    print("End iteration")
