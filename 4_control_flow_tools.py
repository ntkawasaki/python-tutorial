"""
4. More Control Flow Tools
"""


"""
4.1. if Statements
"""
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


"""
4.2. for Statement
"""
# Iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Looping over a copy of the list
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
words


"""
4.3. range Function
"""
for i in range(5):
    print(i)

# Endpoint is never in the list
x = range(5, 10)
range(0, 10, 3)
range(-10, -100, -30)

# To iterate over the indices of a sequence
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for i, word in enumerate(a):
    print(i, word)

# Note how print(range) acts
print(range(0, 20))

"""
In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.

We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. We have seen that the for statement is such an iterator. The function list() is another; it creates lists from iterables:
"""
list(range(5))


"""
4.4. break and continue Statements, and else Clauses on Loops

The break statement breaks out of the innermost enclosing for or while loop

Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but NOT when the loop is terminated by a break statement. This is exemplified by the following loop, which searches for prime numbers:
"""

for n in range(2, 10):
    for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
# Note: the else clause belongs to for, not if
# The loop else clause executes when no break occurs

# continue continues to the next interation of the loop
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

"""
4.5. pass statements

The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
"""
# DONT RUN
while True:
    pass

"""
4.6. Defining Functions

The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables cannot be directly assigned a value within a function (unless named in a global statement), although they may be referenced.

The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; thus, arguments are passed using call by value (where the value is always an object reference, not the value of the object). [1] When a function calls another function, a new local symbol table is created for that call.

A function definition introduces the function name in the current symbol table. The value of the function name has a type that is recognized by the interpreter as a user-defined function. This value can be assigned to another name which can then also be used as a function. This serves as a general renaming mechanism:
"""

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(300)
