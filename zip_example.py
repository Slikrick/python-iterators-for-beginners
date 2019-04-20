import itertools as it
# zip is probably one of my favorite iterators
# zip will take a set of iterators, and return an iterator
# whose item will be the tuple of the iterators items it was given
#
# it should be noted that if you give zip the same iterable it will
# progress both iterators, this actually makes zip viable to
# produce a chain of tuples of the elements in sequence
# e.g. i = iter([1,2,3,4]); zip(i, i) => (1,2), (3,4)
def zip_range_sequence():
    i = iter(range(1, 21))
    for i1, i2, i3, i4 in zip(i, i, i, i):
        print(f"({i1}, {i2}, {i3}, {i4})")

def custom_enumerate(i, start=0):
    """Let's imagine python didn't provide an
    enumerate() function, how might we make our own?
    this is one such implementation"""
    return zip(it.count(start), i)

def zip_two_files(f1, f2):
    """Don't actually do this, as the file objects are never
    properly closed, and will likely only be closed when the
    garbage collector decides to eat them up. Which will only
    happen after the iterator is no longer referenced"""
    file1 = open(f1)
    file2 = open(f2)
    return zip(file1, file2)

def find_duplicates(i1):
    for item1, item2 in zip(i1, i1[1:]):
        if item1 == item2:
            print(f"Found a {item1} next to itself! (dupe)")

if __name__ == "__main__":
    zip_range_sequence()
    for i, item in custom_enumerate(["Hello", "World", "!"]):
        print(f"{i}: {item}")
    
    for item1, item2 in zip_two_files("my_file.txt", "not_my_file.txt"):
        print(f"file1: {item1}file2: {item2}")
    find_duplicates([1,1,2,3,4,4,5,5,6,7,10,10])
    find_duplicates("HEELLOOOOO WORLD!")
