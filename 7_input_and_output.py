"""
7. Input and Output
"""


"""
7.1. Fancier Output Formatting

Convert values to string format with str() and repr().

The str() function is meant to return representations of values which
are fairly human-readable, while repr() is meant to generate
representations which can be read by the interpreter (or will force a
SyntaxError if there is no equivalent syntax). For objects which don’t
have a particular representation for human consumption, str() will
return the same value as repr(). Many values, such as numbers or
structures like lists and dictionaries, have the same representation
using either function. Strings, in particular, have two distinct
representations.
"""
s = "Hello, world!"
print(s)
repr(s)
repr(1/7)

x = 10 * 3.25
y = 200 * 200
print("The value of x is {} and the value of y is {}...".format(repr(x), repr(y)))

# The repr() of a string adds string quotes and backslashes:
hello = "Hello, world\n"
print(hello)
repr(hello)
print(repr(hello))

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))

# Two ways to make tables:
for x in range(1, 11):
    print(repr(x).ljust(2), repr(x**2).rjust(3), end=" ")
    print(repr(x**3).rjust(4))

for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x**2, x**3))

# str.zfill()
"12".zfill(4)
'-3.14'.zfill(7)
'3.14159265359'.zfill(5)

# str.format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# Positional args
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# Keyword args
print('This {food} is {adjective}.'.format(food='spam', adjective='horrible'))

# Positional and keyword args
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used # to convert the value before it is formatted:
contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

# : format specifier
import math
print("The value of pi is approximately {:.6f}".format(math.pi))

# Passing an integer after the ':' will cause that field to be a minimum number
# of characters wide.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print("{0:10} ==> {1:10d}".format(name, phone))

# To reference values like a variable, reference [keys] and pass the dict
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
    'Dcab: {0[Dcab]:d}'.format(table))

# Or pass table with ** notation
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


"""
7.1.1 Old String Formatting
"""
print('The value of PI is approximately %5.3f.' % math.pi)


"""
7.2. Reading and Writing Files

open() returns a file object, and is most commonly used with two arguments:
open(filename, mode).

The first argument is a string containing the filename. The second argument is
another string containing a few characters describing the way in which the file
will be used. mode can be 'r' when the file will only be read, 'w' for only
writing (an existing file with the same name will be erased), and 'a' opens the
file for appending; any data written to the file is automatically added to the
end. 'r+' opens the file for both reading and writing. The mode argument is
optional; 'r' will be assumed if it’s omitted.

Normally, files are opened in text mode, that means, you read and write strings
from and to the file, which are encoded in a specific encoding. If encoding is
not specified, the default is platform dependent (see open()). 'b' appended to
the mode opens the file in binary mode: now the data is read and written in the
form of bytes objects. This mode should be used for all files that don’t
contain text.

In text mode, the default when reading is to convert platform-specific line
endings (\n on Unix, \r\n on Windows) to just \n. When writing in text mode,
the default is to convert occurrences of \n back to platform-specific line
endings. This behind-the-scenes modification to file data is fine for text
files, but will corrupt binary data like that in JPEG or EXE files. Be very
careful to use binary mode when reading and writing such files.

It is good practice to use the with keyword when dealing with file objects. The
advantage is that the file is properly closed after its suite finishes, even if
an exception is raised at some point. Using with is also much shorter than
writing equivalent try-finally blocks:
"""
# Wont actually run
with open("workfile.txt") as file:
    read_data = file.read()

read_data
file.closed

"""
If you’re not using the with keyword, then you should call f.close() to close
the file and immediately free up any system resources used by it. If you don’t
explicitly close a file, Python’s garbage collector will eventually destroy the
object and close the open file for you, but the file may stay open for a while.
Another risk is that different Python implementations will do this clean-up at
different times.

After a file object is closed, either by a with statement or by calling
f.close(), attempts to use the file object will automatically fail.
"""
file.close()
file.read()

"""
7.2.1. Methods of File Objects
"""
f = open('workfile.txt', 'w')

f.read()
f.read_lines()
for line in file:
    print(line, end=' ')

list(f)
f.write("This is a test\n")

# Must convert other types
value = ('the answer', 42)
s = str(value)
f.write(s)
f.tell()

"""
To change the file object’s position, use f.seek(offset, from_what). The
position is computed from adding offset to a reference point; the reference
point is selected by the from_what argument. A from_what value of 0 measures
from the beginning of the file, 1 uses the current file position, and 2 uses
the end of the file as the reference point. from_what can be omitted and
defaults to 0, using the beginning of the file as the reference point.
"""
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)      # Go to the 6th byte in the file
f.read(1)
f.seek(-3, 2)  # Go to the 3rd byte before the end
f.read(1)

"""
In text files (those opened without a b in the mode string), only seeks
relative to the beginning of the file are allowed (the exception being seeking
to the very file end with seek(0, 2)) and the only valid offset values are
those returned from the f.tell(), or zero. Any other offset value produces
undefined behaviour.

File objects have some additional methods, such as isatty() and truncate()
which are less frequently used; consult the Library Reference for a complete
guide to file objects.
"""


"""
7.2.2. Saving Structure with JSON

Strings can easily be written to and read from a file. Numbers take a bit more
effort, since the read() method only returns strings, which will have to be
passed to a function like int(), which takes a string like '123' and returns
its numeric value 123. When you want to save more complex data types like
nested lists and dictionaries, parsing and serializing by hand becomes
complicated.

Rather than having users constantly writing and debugging code to save
complicated data types to files, Python allows you to use the popular data
interchange format called JSON (JavaScript Object Notation). The standard
module called json can take Python data hierarchies, and convert them to string
representations; this process is called serializing. Reconstructing the data
from the string representation is called deserializing. Between serializing and
deserializing, the string representing the object may have been stored in a
file or data, or sent over a network connection to some distant machine.
"""
import json

# View JSON string representation
json.dumps([1, "simple", "list"])

# Serialize object to text file
json.dump(x, f)

# Decode object again
json.load(f)

"""
This simple serialization technique can handle lists and dictionaries, but
serializing arbitrary class instances in JSON requires a bit of extra effort.
The reference for the json module contains an explanation of this.

Also see the pickle module
"""
