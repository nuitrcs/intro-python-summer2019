# Python Session 1

This is the material we'll cover during the first part of the workshop.  We may deviate a little, but we'll work from this.

We're working interactively with the Python interpreter to start.

On Windows, click Start -> Anaconda3 -> Anaconda Prompt, then type `python` at
the prompt to start the interpreter.

On Mac, open a Terminal window and type `python` at the prompt.  Make sure it says Python 3.6 or 3.7 at the top.  Otherwise, there is a console built into other applications.  Open Spyder from the Anaconda Navigator application and use the Python console that's in the bottom right by default.  Or open PyCharm, and there's a Python console available from the bottom.  


## Python as a Calculator

You can type expressions and get the output immediately

```python
2+2
```

You can combine expressions too using parentheses.  The spaces in the expressions below don't have an effect.  They are all optional.

The text that starts with `#` is a comment.  It is not executed.  The `#` denotes that the rest of the line is a comment to be ignored.

```python
50 - 5*6
(50 - 5*6) / 4
8 / 5
8 / 4  # division always returns a floating point number
```

There are additional special operators.

```python
17 / 3
17 // 3  # floor division discards fractional part
17 % 3  # gives you the remainder of the division
```

What does `**` do?

```python
5 ** 2
4 ** (1/2)
```

We can also use python to compare values.  The result is a boolean, which is True or False.

```python
3 == 3.1
3 != 3.1
3 > 3.1
3 < 3.1
```

The `not` operator reverses a boolean value:

```python
not True
not False
not 3 == 3.1
```


## Variables

Variables hold values.  From single numbers to more complex objects.  They can also hold the result of expressions.  Note that in the console, the assignment statement doesn't return anything.  We can type a variable name to get the value.  In scripts, we'd need to use the  `print()` function to see the value.

```python
width = 20
width
height = 5 * 9
width * height
```

Variables must be assigned a value before they can be used

```python
length
```

We get an error:

```
Traceback (most recent call last):

  File "<ipython-input-4-9cf56f394795>", line 1, in <module>
    length

NameError: name 'length' is not defined
```

You'll see this error if you mistype a variable name too.  

Variable names are case sensitive.  Variable names should start with a letter.  They cannot start with a number.


```python
Width
1990gdp = 3
```

[Exercise](python-exercises1.md#calculator-and-variables)

### Multiple Assignments

Python allows you to assign a value to multiple variables in one line in two different ways.  

First, we can set several variables to all have the same value:

```python
a = b = c = 10
a
print(a)  # could also use the print function
print(a, b, c)  # can print multiple things
```

When evaluated, it starts all the way at the right and works left.

Second, we can set multiple variables with different values in one line:

```python
x, y = 2, 3
```

Here, x is getting the value 2, and y is getting the value 3.

Both the variable names and the values are separated by commas.  The entire right hand side is evaluated before any values are assigned to the variables.

```Python
x, y = y, x  # swaps the values of x and y!
```


## Strings

Strings hold alphanumeric data (letters, numbers, punctuation, etc.) -- text.  You can use single or double quotes, but they need to be matched.

```python
'spam and eggs'
'doesn\'t'
"doesn't"
'"Yes," he said.'
```

You can store values, even emojis!  (in Python 3) 

```python
my_string_variable = 'hi I am a string 😛'
my_string_variable
```

```python
"Python in Korean: 파이썬"
```

New line character, and `print()`.

```python
two_line_string = "This is line 1.\nThis is line2."
two_line_string
print(two_line_string)
```

`print()` is a function.  It's built into Python.  In a script, you'd need to use `print()` to see the output.  Just typing the variable name won't do anything.

You can also use triple quotes for multi-line strings.  They can contain new lines in them.  You can triple either single or double quotes.

```python
long_text = """This is a multiline
  string of text with newline
  characters built in.  Spaces are respected."""
print(long_text)
```

We can join, or concatenate, strings with `+`:

```python
prefix = 'super'
suffix = 'duper'
prefix + suffix
prefix + ' ' + suffix
```

When we print them, we can comma separate values, and they are joined with a space:

```python
print(prefix, suffix)
```

And we can compare strings too based on alphabetical order:

```python
'cat' < 'dog'
'dog' < 'cat'
```

And you can test if a substring is in a string with the `in` operator:

```python
'fox' in 'The quick brown fox'
'dog' in 'The quick brown fox'
```

There are functions that will take a string as an argument:

```python
string_var = 'abcdefg'
len(string_var)
```

But strings also have functions that are called on the string with dot notation.  If you're familiar with other languages, everything in Python is an object.  

Here, the string value itself is implicitly the first argument to the function.  The function is a property of the string object.

```python
string_var.upper()
string_var.count('a')
string_var.replace('ab', 'X')
string_var
```

Note that `replace()` didn't change the value of `string_var`.  Strings are immutable, meaning we can't change them after we make them.  We can only change the value of the variables holding string values, which is a subtle difference.  How could we change the value of `string_var` here?


With dot notation, you can chain function calls together.  `string_var.replace('a', 'X')` returns a string, so we can call `replace()` on the string that is returned too:

```python
string_var.replace('a', 'X').replace('b', 'Y')
```

And if we actually want to change the value of `string_var`:

```python
string_var = string_var.replace('a', 'X').replace('b', 'Y')
```

[Exercise](python-exercises1.md#strings)


### String Formatting

String formatting allows us to substitute the value of variables into strings without concatenating them all together with `+` signs.

```python
animal = "hippo"
print("My favorite animal is the {}.".format(animal))
animal2 = "giraffe"
print("My favorite animal is the {}.  The {} is also awesome.".format(animal, animal2))
```

You might also see this in older code:

```python
print("My favorite animal is the %s.  The %s is also awesome." % (animal, animal2))
```

[Exercise](python-exercises1.md#string-formatting)

## Types

We've used numeric values and strings.  Every value (including those stored in variables) has a type:


```python
type('abc')
type(123)
type(0.1)
```

Values of one type can be converted to other types with built-in functions.


```python
float(3)
float('3.2')
string(3.56)
```

But not all conversions are defined:

```python
int('1')
int('1.1')
```

Instead:

```python
x = float('1.1')
int(x)
```

Or, we could nest our function calls:

```python
int(float('1.1'))
```

Type matters when doing comparisons

```python
ten_int = 10
ten_string = '10'
ten_int == ten_string
ten_int == int(ten_string)
```

The `==` does a comparison, while `=` does an assignment.  

And operators behave differently for different types of data:

```python
ten = '10'
ten + ten
ten = int(ten)
ten + ten
```

And certain functions expect certain types of data.

There's a special type, `None`, that can be used to represent no value.

```python
x = None
x
print(x)
type(x)
```



## Lists

So how do we build up more complex structures?  Python has another fundamental type called a list.  A list is a collection of other values, other lists, or other objects (string, integers, lists, etc. are all objects, but packages (and you!) can define new objects too).

A list is created with `[]` (there's also `list()` that can be used to make an empty list or lists from something called an "iterable").  

```python
my_list = ['a', 'b', 'c', 'd']
my_list
```

The elements in a list don't have to be of the same type, but they usually are.

```python
my_mixed_list = [1, 'a', 2.3, [4, 5, 6]]
my_mixed_list
```

Lists are indexed, starting with 0.  List indices allow us to access the individual elements in a list or parts of the list.

```python
my_list[0]
my_list[2]
```

Note that you can use indices with strings too:

```python
string_var = 'abcde'
string_var[0]
```

And you can get their length with `len()`:

```python
len(my_list)
len(string_var)
```

Negative index numbers count from the end, with -1 being the last element:

```python
my_list[-1]
my_list[-2]
```

We can get multiple consecutive elements  with `start:end`.  End is exclusive.  This takes each integer value from start to end.

```python
my_list[0:3]
```

If we go over the end, we only get what's available:


```python
my_list[0:30]
```

We can do ranges with negative values too.  Smallest value goes first:

```python
my_list[-3:-1]
```

Why didn't we get "d" in the output?  The ending index in `start:end` is EXCLUSIVE (meaning it's not included in the output).

We can't mix negative and positive (or 0) numbers in `start:end` though.

We can leave out either half of the range (leave it blank):

```python
my_list[-3:]
my_list[:2]
my_list[2:]
```

or both:

```python
my_list[:]
```


When you have nested lists, you need a separate set of brackets for each list:

```python
nested_lists = [[2, 3, 5, 7, 11], [2, 4, 6, 8]]
len(nested_lists)
nested_lists[0]
nested_lists[0][1]
nested_lists[-1][-1]
```

You can join lists by adding them:

```python
primes = [2, 3, 5, 7, 11]
more_primes = [13, 17, 19]
primes + more_primes
```

This appends the elements of one list to the other list.  What if we just want to add a single value, not a whole list?

```python
primes + 39
```

You can add a single element to a list with `append()`.  THIS CHANGES THE LIST!

```python
primes
primes.append(13)
primes
```

You can also put a single value in a list and use `+`:

```python
primes + [39]
```

If you append a list, you get a nested list, because append adds an element to the first list, and an entire list can be an element in another list:

```python
primes.append(more_primes)
primes
```

To combine two lists in one list instead, use `extend()` (or `+` above)

```python
primes = [2, 3, 5, 7, 11]
more_primes = [13, 17, 19]
primes.extend(more_primes)
primes
```

Lists are mutable, meaning you can change the elements by assigning to them directly

```python
fruit = ['apple', 'banana', 'pear']
fruit[0] = 'fig'
fruit
```

Strings are immutable (not mutable).  The following gives you an error.

```python
my_name = 'Christina'
my_name[0] = 'c'
```

You can assign to slices of lists too

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
letters[2:5] = ['C', 'D', 'E']
letters
```

Be careful, since the replacement length doesn't need to match.  Replacement will go in the same spot in the list, but it can be longer or shorter.

```python
letters[2:5] = ['c']
letters
```

There are additional list functions that can change a list:

```python
list1 = ['x', 'g', 'v', 'a']
list1.sort()  
list1
```

The `in` operator lets you test whether a specific value is in your list (in it's entirety):

```python
'a' in list1
'b' in list1
'b' not in list1
list2 = ["apple", "banana"]
"a" in list2
```


[Exercise](python-exercises1.md#lists)




## Tuples

Tuples are immutable, (usually) short, list-type objects.  You define them with parentheses.  They are like a list, but once they are created, you can't change the elements in them:

```python
my_tuple = ("cat", "dog")
my_tuple
my_tuple[0]
my_tuple[0] = "fish"
my_tuple = ("fish", "dog")
my_tuple
```

You'll see tuples sometimes in the context of multiple assignment:

```python
animal1, animal2 = my_tuple
animal1
animal2
```

The values of the tuple are unpacked into individual variables.



## Dictionaries

Dictionaries hold key-value pairs.  Keys are labels you can use to look up the stored values associated with them.

Keys are usually strings, but they don't have to be.  Keys are unique.

Create a dictionary with `{}` (or an empty dictionary with `dict()`).


```python
ages = {'Casey': 41, 'Henry': 4, 'Madison': 2, 'Caroline': 0, 'Brian': 36}
ages
```

Instead of indexing with positions, we index with keys:

```python
ages['Casey']
ages['Madison']
```

What happens if we ask for a value not in the dictionary?

```python
ages['Denise']
```

Or we can use the `get()` function, which optionally lets us specify a default value if the key isn't present:

```python
ages.get('Brian')
ages.get('Denise')  # None is the default
ages.get('Denise', 50)
```

For dictionaries, `in` tests keys:

```python
'Madison' in ages
41 in ages
```

We can add a key and value pair to a dictionary by setting it:

```python
ages['Jessica'] = 35
ages['Jessica']
```

We can also change the value by assigning to it

```python
ages['Jessica'] = 37
ages['Jessica']
```

We can get all of the keys or values with functions:

```python
ages.keys()
ages.values()
```

We can get the keys and values together with `items()`

```python
ages.items()
```

These functions are most useful in combination with loops, which we'll get to later.

[Exercise](python-exercises1.md#dictionaries)



# Style Guide

[PEP 8](https://www.python.org/dev/peps/pep-0008/)
