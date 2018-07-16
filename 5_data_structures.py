"""
5. Data Structures
"""


"""
5.1. More on Lists


Methods of lists

list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable.
Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of
the element before which to insert, so a.insert(0, x) inserts at the
front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is x. It is an error if
there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no
index is specified, a.pop() removes and returns the last item in the
list.

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is x.
Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice
notation and are used to limit the search to a particular subsequence of
the list. The returned index is computed relative to the beginning of
the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
"""
# Remember, lists are mutable!
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count("apple")
fruits.index("banana")
# Find next banana after index 4
fruits.index("banana", 4)

# Changes list object
fruits.reverse()
fruits

fruits.append("grape")
fruits

fruits.pop()
fruits


"""
5.1.1. Using Lists as Stacks

Last in, first out.
"""
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack

stack.pop(); stack
stack.pop(); stack
stack.pop(); stack


"""
5.1.2. Using Lists as Queues

First in, first out

While appends and pops from the end of list are fast, doing inserts or
pops from the beginning of a list is slow (because all of the other
elements have to be shifted by one).
"""
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue

queue.append("Terry")
queue.append("Graham")
queue

queue.popleft()
queue


"""
5.1.3. List Comprehensions

Make new lists where each element is the result of some operations
applied to each member of another sequence or iterable, or to create a
subsequence of those elements that satisfy a certain condition.
"""
# For loop version
squares = []
for x in range(0, 11):
    squares.append(x**2)

squares

# Lambda expression version
squares = list(map(lambda x: x**2, range(0, 12)))
squares

# List comprehension version
squares = [x**2 for x in range(1, 13)]
squares
# More concise and readable

## Another example
# For loop version
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

my_prediction = [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
combs == my_prediction

# List comprehension
lc = [(x, y) for x in [1,2,3] for y in [3,1,4] if x!=y]
lc == my_prediction

## More examples
vec = [-4, -2, 0, 2, 4]
# New list with doubled values
[2*x for x in vec]
# Filter
[x for x in vec if x>=0]
# Apply a function
[abs(x) for x in vec]

# Calling methods
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[f.strip() for f in freshfruit]

# Create a tuple
[(x, x**2) for x in range(6)]

# Flatten a list
vec = [[1,2,3], [4,5,6], [7,8,9]]
[i for j in vec for i in j]
# [num for elem in vec for num in elem]

# Using expressions and nested functions
from math import pi
[str(round(pi,i)) for i in range(6)]


"""
5.1.4. Nested List Comprehensions
"""
