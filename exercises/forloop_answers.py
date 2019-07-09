# FOR LOOP exercise answers

# Remember: to run this in PyCharm, right-click and choose to run this file,
# or use the Run option at the top


# defining a list with some values
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# Here's a for loop example
for color in colors:
    print(color, "is a great color!")

# add some of your favorite words to the list below
fav_words = ["flamingo", "awesome", "shredded"]

# write a loop to print each word in your list as
# part of a sentence "The word ____ starts with the letter __."
# Remember that you can index the characters in words like you do lists
# Hint: you might want to use the string format function
# to substitute the variables into the string.
for word in fav_words:
    print("The word {} starts with the letter {}.".format(word, word[0]))

# Another way to print:
for word in fav_words:
    print("The word " + word + " starts with the letter " + word[0] + ".")


# Now write a loop that uses range to print the following output:
# *
# **
# ***
# ****
# *****
# Hint: you can print a string multiple times by multiplying it!
# example:
print("a" * 3)
print("a" * 3 + "b")  # string multiplication and addition!


# write your loop here:
for i in range(1, 6):
    print("*" * i)


# EXTRA: Remember how to make a string uppercase?  There's also a
# function called title that you can call on a string
# # that will capitalize just the first
# letter.  Modify the color loop above to capitalize the first letter
# of each color word when printing
for color in colors:
    print(color.title(), "is a great color!")



# CHALLENGE: Write a nested for loop (one for loop inside another)
# to print each of your favorite words on a diagonal, like:

# fav_words = ["bingo", "cat"]

# Output:
# b
#  i
#   n
#    g
#     o
# c
#  a
#   t

# Hint: you'll need to use the length (len())
# of each word in the inner loop

for word in fav_words:
    for i in range(len(word)):
        print(" " * i + word[i])
