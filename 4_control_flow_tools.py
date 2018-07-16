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
In many ways the object returned by range() behaves as if it is a list,
but in fact it isn’t. It is an object which returns the successive
items of the desired sequence when you iterate over it, but it doesn’t
really make the list, thus saving space.

We say such an object is iterable, that is, suitable as a target for
functions and constructs that expect something from which they can
obtain successive items until the supply is exhausted. We have seen
that the for statement is such an iterator. The function list() is
another; it creates lists from iterables:
"""
list(range(5))


"""
4.4. break and continue Statements, and else Clauses on Loops

The break statement breaks out of the innermost enclosing for or while
loop

Loop statements may have an else clause; it is executed when the loop
terminates through exhaustion of the list (with for) or when the
condition becomes false (with while), but NOT when the loop is
terminated by a break statement. This is exemplified by the following
loop, which searches for prime numbers:
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

The pass statement does nothing. It can be used when a statement is
required syntactically but the program requires no action.
"""
# DONT RUN
while True:
    pass


"""
4.6. Defining Functions

The execution of a function introduces a new symbol table used for the
local variables of the function. More precisely, all variable
assignments in a function store the value in the local symbol table;
whereas variable references first look in the local symbol table, then
in the local symbol tables of enclosing functions, then in the global
symbol table, and finally in the table of built-in names. Thus, global
variables cannot be directly assigned a value within a function (unless
named in a global statement), although they may be referenced.

The actual parameters (arguments) to a function call are introduced in
the local symbol table of the called function when it is called; thus,
arguments are passed using call by value (where the value is always an
object reference, not the value of the object). [1] When a function
calls another function, a new local symbol table is created for that
call.

A function definition introduces the function name in the current
symbol table. The value of the function name has a type that is
recognized by the interpreter as a user-defined function. This value
can be assigned to another name which can then also be used as a
function. This serves as a general renaming mechanism:
"""
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1

    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(300)

"""
Coming from other languages, you might object that fib is not a
function but a procedure since it doesn’t return a value. In fact, even
functions without a return statement do return a value, albeit a rather
boring one. This value is called None (it’s a built-in name). Writing
the value None is normally suppressed by the interpreter if it would be
the only value written. You can see it if you really want to using
print():
"""

fib(0)
print(fib(0))

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)    # see below
        a, b = b, a + b

    return result

fib2(100)


"""
4.7. More on Defining Functions
"""


"""
4.7.1. Default Argument Values
"""
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok("Are you okay?")
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# The default values are evaluated at the point of function definition in the defining scope

i = 5
def f(arg=i):
    print(arg)

i = 6
f()

"""
Important warning: The default value is evaluated only once. This
makes a difference when the default is a mutable object such as a list,
dictionary, or instances of most classes. For example, the following
function accumulates the arguments passed to it on subsequent calls:
"""
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# Fix it like this: None is mutable
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(5))
print(f(6))


"""
4.2.7. Keyword Arguments
"""
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# 1 positional argument
parrot(1000)

# 1 keyword argument
parrot(voltage=1000)

 # 2 keyword arguments
parrot(voltage=1000000, action='VOOOOOM')

# 3 positional
parrot('a million', 'bereft of life', 'jump')

# 1 positional, 1 keyword
parrot('a thousand', state='pushing up the daisies')

# Invalid calls
# Required argument missing
parrot()

# Non-keyword argument after a keyword argument
parrot(voltage=5.0, 'dead')

# Duplicate value for the same argument
parrot(110, voltage=220)

# Unknown keyword argument
parrot(actor='John Cleese')

"""
In a function call, keyword arguments must follow positional arguments.
All the keyword arguments passed must match one of the arguments
accepted by the function (e.g. actor is not a valid argument for the
parrot function), and their order is not important. This also includes
non-optional arguments (e.g. parrot(voltage=1000) is valid too). No
argument may receive a value more than once. Here’s an example that
fails due to this restriction:
"""
def function(a):
    pass

function(0, a=0)

"""
When a final formal parameter of the form **name is present, it
receives a dictionary containing all keyword arguments except for those
corresponding to a formal parameter. This may be combined with a formal
parameter of the form *name which receives a tuple containing the
positional arguments beyond the formal parameter list. (*name must
occur before **name.) For example, if we define a function like this:
"""
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for k, v in keywords.items():
        print(k, ":", v)

cheeseshop("salty", "argument 1", "argument 2", "argument 3", kw1="sc1", kw2="sc2")

# Keywords will be printed in the same order provided


"""
4.7.3. Arbitrary Argument Lists

These arguments will be wrapped into a tuple
"""
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

"""
Normally, these variadic arguments will be last in the list of formal
parameters, because they scoop up all remaining input arguments that
are passed to the function. Any formal parameters which occur after the
*args parameter are ‘keyword-only’ arguments, meaning that they can
only be used as keywords rather than positional arguments.
"""
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
concat("earth", sep="-", "mars")
concat("earth", "mars", "venus", sep="=")


"""
4.7.4. Unpacking Argument Lists
"""
# Normal call
list(range(3, 6))

# Unpacking to call
x = (3, 10)
list(range(*x))


"""
4.7.5. Lambda Expressions

Lambda functions can be used wherever function objects are required.
They are syntactically restricted to a single expression. Like nested
function definitions, lambda functions can reference variables from the
containing scope.
"""
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(10)
f(0)
f(111)
f(1)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


"""
4.7.6. Documentation Strings

The first line should always be a short, concise summary of the
object’s purpose. For brevity, it should not explicitly state the
object’s name or type, since these are available by other means (except
if the name happens to be a verb describing a function’s operation).
This line should begin with a capital letter and end with a period.

If there are more lines in the documentation string, the second line
should be blank, visually separating the summary from the rest of the
description. The following lines should be one or more paragraphs
describing the object’s calling conventions, its side effects, etc.

The Python parser does not strip indentation from multi-line string
literals in Python, so tools that process documentation have to strip
indentation if desired. This is done using the following convention.
The first non-blank line after the first line of the string determines
the amount of indentation for the entire documentation string. (We
can’t use the first line since it is generally adjacent to the string’s
opening quotes so its indentation is not apparent in the string
literal.) Whitespace “equivalent” to this indentation is then stripped
from the start of all lines of the string. Lines that are indented less
should not occur, but if they occur all their leading whitespace should
be stripped. Equivalence of whitespace should be tested after expansion
of tabs (to 8 spaces, normally).
"""
def my_function():
    """Do nothing, but document it.

    No really do nothing.
    """
    pass

print(my_function.__doc__)


"""
4.7.7. Function Annotations

Function annotations are completely optional metadata information about
the types used by user-defined function.

Annotations are stored in the __annotations__ attribute of the function
as a dictionary and have no effect on any other part of the function.
Parameter annotations are defined by a colon after the parameter name,
followed by an expression evaluating to the value of the annotation.
Return annotations are defined by a literal ->, followed by an
expression, between the parameter list and the colon denoting the end
of the def statement. The following example has a positional argument,
a keyword argument, and the return value annotated:
"""
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')


"""
4.8 PEP 8 Style Guide for Python
"""
import webbrowser

webbrowser.open("https://www.python.org/dev/peps/pep-0008/")
