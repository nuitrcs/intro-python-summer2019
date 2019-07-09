# Before we looped through the elements in a list.  For example:

words = ["zebra", "lion", "giraffe"]
for word in words:
    print(word)


# You can't change the values in a list with the loop variable
for word in words:
    word = "hippo"
print(words)

# "word" above has a copy of the value.
# If we wanted to change the values (not always a great idea), we'd need to use the list index.

# If you want to loop through a sequence of integers instead of values in a list,
# use `range()` which returns something called an iterable:

for i in range(3):
    print(i)

print(range(3))

for i in range(2, 8):
    print(i)

# back to our list above:
words = ["zebra", "lion", "giraffe"]
for i in range(len(words)):
    words[i] = "hippo"
print(words)

# again, the above should be done with caution, and you should never change the
# length of a list while looping!

# when we loop through a dictionary, we usually loop through the keys,
# which is what's returned when we use a dict as the iterable in the loop
legs = {"human": 2, "fish": 0, "cat": 4, "tripod": 3}
for k in legs:
    print(k, legs[k])

