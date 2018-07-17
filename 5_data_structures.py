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
Sort the items of the list in place (the arguments can be used for sort
customization, see sorted() for their explanation).

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
# Matrix example
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]

# List comprehension
[[row[i] for row in matrix] for i in range(4)]

# Single for loop
transposed = []
for i in range(len(matrix[1])):
    transposed.append([row[i] for row in matrix])

transposed

# Double for loop
transposed = []
for i in range(len(matrix[1])):
    temp = []
    for row in matrix:
        temp.append(row[i])
    transposed.append(temp)

transposed

# Easier
list(zip(*matrix))


"""
5.2. del Statement

Remove an item by its index, NOT by value. Can also remove slices or
clear a list
"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]; a
del a[2:4]; a
del a[:]; a

# Delete entire variable
del a


"""
5.3. Tuples and Sequences

Tuples are immutable, and usually contain a heterogeneous sequence of
elements that are accessed via unpacking (see later in this section) or
indexing (or even by attribute in the case of namedtuples). Lists are
mutable, and their elements are usually homogeneous and are accessed by
iterating over the list.
"""
# This is also an example of packing
t = (12345, 54321, 'hello!')
t[0]

# Nested tuple
u = (t,  tuple(range(1, 6)))
u

# Can't assign based on index
u[0][1] = 888

# Can contain mutables
m = ([1,2,3], [4,5,6]); m

# Which can be changed
m[0][0] = 10
m

"""
A special problem is the construction of tuples containing 0 or 1
items. Empty tuples are constructed by an empty pair of parentheses; a
tuple with one item is constructed by following a value with a comma.
"""
empty = ()
type(empty)

singleton = ("hi",)
type(singleton)

"""
Sequence unpacking and works for
any sequence on the right-hand side. Sequence unpacking requires that
there are as many variables on the left side of the equals sign as
there are elements in the sequence. Note that multiple assignment is
really just a combination of tuple packing and sequence unpacking.
"""
x, y, z = t
x
y
z


"""
5.4. Sets

A set is an unordered collection with no duplicate elements. Basic uses
include membership testing and eliminating duplicate entries. Set
objects also support mathematical operations like union, intersection,
difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to
create an empty set you have to use set(), not {}; the latter creates
an empty dictionary, a data structure that we discuss in the next
section.
"""
# Note two oranges
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket

# Membership testing
"orange" in basket
"hello" in basket

# Set operations
a = set('abracadabra')
b = set('alacazam')

# In a but not in b
a - b

# In either
a | b

# In a and b
a & b

# In a or b, not both
a ^ b

# Set comprehensions
a = {x for x in 'abracadabra' if x not in "abc"}
a


"""
5.5. Dictionaries

Dictionaries are indexed by keys, which can be any immutable type;
strings and numbers can always be keys. Tuples can be used as keys if
they contain only strings, numbers, or tuples; if a tuple contains any
mutable object either directly or indirectly, it cannot be used as a
key. You can’t use lists as keys, since lists can be modified in place
using index assignments, slice assignments, or methods like append()
and extend()

It is best to think of a dictionary as an unordered set of key: value
pairs, with the requirement that the keys are unique (within one
dictionary). A pair of braces creates an empty dictionary: {}. Placing
a comma-separated list of key:value pairs within the braces adds
initial key:value pairs to the dictionary; this is also the way
dictionaries are written on output.

The main operations on a dictionary are storing a value with some key
and extracting the value given the key. It is also possible to delete a
key:value pair with del. If you store using a key that is already in
use, the old value associated with that key is forgotten. It is an
error to extract a value using a non-existent key.

Performing list(d.keys()) on a dictionary returns a list of all the
keys used in the dictionary, in arbitrary order (if you want it sorted,
just use sorted(d.keys()) instead). [2] To check whether a single key
is in the dictionary, use the in keyword.
"""
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 5555

del tel['sape']
tel

tel['irv'] = 4127
tel

list(tel.keys())
sorted(tel.keys())

"guido" in tel
"jack" not in tel

# dict() constructor
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# dict comprehensions
{x: x**2 for x in range(6)}

# If keys are strings, can just use keyword args
dict(sape=4139, guido=4127, jack=4098)


"""
5.6. Looping Techniques
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

"""
To loop over a sequence in sorted order, use the sorted() function
which returns a new sorted list while leaving the source unaltered.
"""
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

"""
It is sometimes tempting to change a list while you are looping over
it; however, it is often simpler and safer to create a new list instead.
"""
import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data


"""
5.7. More on Conditions

The conditions used in while and if statements can contain any
operators, not just comparisons.

The comparison operators in and not in check whether a value occurs
(does not occur) in a sequence. The operators is and is not compare
whether two objects are really the same object; this only matters for
mutable objects like lists. All comparison operators have the same
priority, which is lower than that of all numerical operators.

Comparisons can be chained. For example, a < b == c tests whether a is
less than b and moreover b equals c.

Comparisons may be combined using the Boolean operators and and or, and
the outcome of a comparison (or of any other Boolean expression) may be
negated with not. These have lower priorities than comparison
operators; between them, not has the highest priority and or the
lowest, so that A and not B or C is equivalent to (A and (not B)) or C.
As always, parentheses can be used to express the desired composition.

The Boolean operators and and or are so-called short-circuit operators:
their arguments are evaluated from left to right, and evaluation stops
as soon as the outcome is determined. For example, if A and C are true
but B is false, A and B and C does not evaluate the expression C. When
used as a general value and not as a Boolean, the return value of a
short-circuit operator is the last evaluated argument.
"""
# You can assign result of comparison to a variable
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null


"""
5.8. Comparing Sequences and Other Types

Sequence objects may be compared to other objects with the same
sequence type. The comparison uses lexicographical ordering: first the
first two items are compared, and if they differ this determines the
outcome of the comparison; if they are equal, the next two items are
compared, and so on, until either sequence is exhausted. If two items
to be compared are themselves sequences of the same type, the
lexicographical comparison is carried out recursively. If all items of
two sequences compare equal, the sequences are considered equal. If one
sequence is an initial sub-sequence of the other, the shorter sequence
is the smaller (lesser) one. Lexicographical ordering for strings uses
the Unicode code point number to order individual characters. Some
examples of comparisons between sequences of the same type:
"""
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
