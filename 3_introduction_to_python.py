"""
3. An Informal Introduction to Python
"""


"""
3.1. Using Python as a Calculator
"""


"""
3.1.1. Numbers
"""
2 + 2
50 - 5*6
(50 - 5*6)/4
8/5  # Division always returns float

# To do floor division use //
17/3
17//3

# For remainder use %
17%3
# Result * divisor + remainder
5*3 + 2

# Powers
5**2
2**7

# = sign used to assign a value to a variable
width = 20
height = 5*9
width*height

# Trying to use an undefined variable
n

# Mixed type operands will convert to float
4*3.75 - 1

# The last printed expression assigned to variable _
tax = 12.5/100
price = 100.50
price * tax

price + _
round(_, 2)


"""
3.1.2. Strings
"""
# Single quotes
'spam eggs'

# Use \' to escape the single quote...
'doesn\'t'

# Or use double quotes instead
"doesn't"

'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'


"""In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes. While this might sometimes look different from the input (the enclosing quotes could change), the two strings are equivalent. The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes. The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:"""

'"Isn\'t," they said.'
print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'
s
print(s)

"""If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:"""

# \n means new line
print('C:\some\name')

print(r'C:\some\name')

# String literals spanning multiple lines
print("""\
    Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
""")

# Some string operations
3 * 'un' + 'ium'

# String literals next to each other automatically concatenated
'Py' 'thon'

text = ('Put several strings within parentheses '
    'to have them joined together.')
text

# Only works with literals though
prefix = "Py"
prefix "thon"

('un' * 3) 'ium'

# To concatenate variables use +
prefix + "thon"

# String indexes
word = "Python"
word[0]
word[5]

# Negative indices
word[-1]
word[-2]
word[-6]
# 0 is the same as -0, so negative indices start at -1

# Slicing
word[0:2]
word[2:5]

# Start always included and end excluded, this is so that s[:i] +
# s[i:] always = i
word[:2] + word[2:]
word[:4] + word[4:]

# Omitted first index defaults to zero
word[:2]

# Omitted last index defaults to length
word[4:]
len(word)

word[-2:]

"""
One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.

For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.
"""

# Index too large
word[10]

# Slice too large is fine though
word[4:42]
word[42:]

"""Python strings are immutable. Assigning to an indexed position results in error."""
word[0] = "J"

word[2:] = 'py'

# Just create a new string
"J" + word[1:]
word[:2] + "py"

# len
s = 'supercalifragilisticexpialidocious'
len(s)


"""
3.1.3. Lists

Comma-separated values between square brackets. Can have different types, but usually are the same type.
"""
squares = [1, 4, 9, 16, 25]
squares

# Can be indexed and sliced
squares[0]
squares[-1]
squares[-3:]

"""All slicing operations create a NEW list object"""
squares[:]

# Also support concatenation
squares + [36, 49, 64, 81, 100]

"""Lists are mutable"""
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
cubes

# The append() method
cubes.append(216)
cubes.append(7**3)
cubes

# Assignment to lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

# Replace some values
letters[2:5] = ['C', 'D', 'E']
letters

# Remove letters
letters[2:5] = []
letters
len(letters)

# Nesting lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]


"""3.2. First Steps Toward Programming"""
# Fibonacci Series
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

i = 256*256
print('The value of i is', i)

# kwarg end can make a new line not get printed
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
