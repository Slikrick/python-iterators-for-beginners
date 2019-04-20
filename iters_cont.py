import itertools as it

def get_len_of_items(iterable):
    # Map the function len() (note the lack of parens in the code)
    # to each of the items given in iterable, return the list of
    # those lengths
    return list(map(len, iterable))

def bill_combinations():
    # Let's imagine our wallet as an array of bills
    # How many ways can we combine 3 of those bills?
    # what are those sums?
    bills = [20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1]
    # The combinations tool from itertools allows you to group
    # all items in the iterable with all other combination of items
    # in the iterable. In this case giving us our bills
    bill_combos = it.combinations(bills, 3)
    # bill_combos_sum = list(map(sum, bill_combos))
    # Make this return a random bill combo from bill_combos, what's
    # the average amount of money you expect to pull from the 
    # wallet
    return list(bill_combos)


def bill_combinations_no_dupes():
    return set(bill_combinations())

# INFINITE ITERATORS
# Itertools offers a couple ways to create infinite iterators 
# from finite iterators, these iterators need to be bounded
# otherwise they will run forever
# Iterators:
#   count()
#   cycle()
#   repeat()

def count_up():
    print("Let's count to ten!")
    for number in it.count(1):
        if number > 10: break
        print(number)

def cycle_example():
    nums = [3, 2, 1, 0]
    seen_0 = False
    for item in it.cycle(nums):
        # Break after the second cycle
        if seen_0 and item == 0:
            break
        elif item == 0:
            seen_0 = True
        print(item)

def repeat_example():
    # it.repeat(1, 100) will repeat 100 times
    # without a bound it will repeat forever
    for i in it.repeat(1):
        print(i)

# TERMINATING ITERATORS
# These iterators will eventually terminate on a shortest 
# input sequence, these are very useful if you run into them.
# As always the full docs are online:
# https://docs.python.org/3/library/itertools.html
# 
# Iterators:
#   chain() or chain.from_iterable()
#   islice()
#   takewhile()
#   tee()
#   zip_longest()
def chain_example():
    one = [1, 2, 3]
    two = [11, 12, 13]
    three = [101, 102, 103]
    for i in it.chain(one, two, three):
        print(i)

def islice_example():
    hello = "HELLO WORLD!"
    print(str(it.islice(hello, 2)))

def takewhile_example():
    test = [1, 2, 3, 50, 100, 200, 1000]
    for i in it.takewhile(lambda x: x >= 50, test):
        print(i)

# ITERATOR RECIPES
# If you want to see what other types of iterators can be created
# you can see an example list of 'recipes' in the itertools docs
# here: 
# https://docs.python.org/3/library/itertools.html#itertools-recipes
