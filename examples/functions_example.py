# FUNCTIONS

# Remember: to run this in PyCharm, right-click and choose to run this file,
# or use the Run option at the top

# NOTE: Normally we'd put all of our function definitions up top together


# Here's the syntax to create a function with no input and no output;
def hello():
    print("hello")


# now call it (it has to be defined above before we can call it)
hello()


# We can have our function take inputs:
def hello2(name):
    print("Hello {}!".format(name))


hello2("Christina")

# We could also name the argument when calling the function
hello2(name="Marcia")


# Instead of doing something, let's have our function return output
def hello3(name):
    return "Hello again {}!".format(name)


# now the function doesn't print directly, but we can save it in a variable to use later.
# To see the output, we'll need to print it
x = hello3("Christina")
print(x)


# functions have access to variables outside of the function (that exist when the function is called)
def hello4():
    print("Hello 4 {}".format(name2))


name2 = "Ming"
hello4()


# but they will look first at local variables and function parameters (input)
def hello5(name2):
    print("Hello 5 {}".format(name2))


name2 = "Ming"
hello5("Adrian")


# functions can't change immutable inputs, but they can change mutable inputs,
# such as the individual elements of a list
def hello6(onename, names):
    onename = "Linda"
    print("Hola {}".format(onename))
    names = ["Abby", "Becky", "Carlos"]
    for name in names:
        print("Howdy {}!".format(name))

    # for good measure, also change an individual element
    names[0] = "Alistair"


name1 = "Bob"
names = ["Bob", "Frank", "John"]
hello6(name2, names)
print("name1 after the function has the value {}".format(name1))
print("names after the function has the value {}".format(names))


# now, instead of changing names completely, just change one element;
# this changes the names list!
def hello7(names):
    names[0] = "Grace"
    print("In the function hello7, names has values: ")
    print(names)


names = ["Bob", "Frank", "John"]
hello7(names)
print("names after the function hello7 has the value {}".format(names))


# We saw how to return values.  Returning a value ends the execution of the function.
def hello8(name):
    if name == "Casey":
        return "Good morning Casey!"
    return "Good morning person whose name isn't Casey."


print(hello8("Frank"))
print(hello8("Casey"))


# You might see a return statement without a value: it ends execution of the function
def hello9(name):
    if name == "Casey":
        print("Good morning Casey!")
        return
    print("Good morning person whose name isn't Casey.")


hello9("Frank")
hello9("Casey")


# We can set default values
# for our parameters too.
def increment(a, b=1):
    return a + b


print("Incrementing...")
print(increment(1))
print(increment(1, 2))
print(increment(1, b=5))

# we can switch order of arguments
print(increment(b=5, a=1))

# but we can't have named arguments before unnamed ones.  The below would give an error:
# SyntaxError: positional argument follows keyword argument
# print(increment(a=5, 2))


# We can return multiple values, and save the results with multiple assignment
def increment_both(a, b, step=5):
    return a + step, b + step


# Incrementing two values
x, y = increment_both(100, 200)
print(x, y)


# This is really creating and unpacking something called a tuple, which is basically an immutable list
z = increment_both(100, 200)
print(z)




