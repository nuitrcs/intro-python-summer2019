# Remember: to run this in PyCharm, right-click and choose to run this file,
# or use the Run option at the top


age = 20
hometown = "Dayton"

print("age has value {}".format(age))
print("hometown has value {}".format(hometown))

print("Section 1")

# single test
if age >= 18:
    print("Go vote!")

print("Section 2")

if not age >= 18:
    print("Vote when you're 18!")

# Recap logical conditions
True and True
True and False
False and False
True or False
True and not False
not False or False


print("Section 3")

# multiple conditions with "and"
if age >= 18 and hometown != "Evanston":
    print("Vote absentee!")


print("Section 4")

if age > 5 and age < 19:
    print("Shouldn't you be in school?")


print("Section 5")

# Else condition
if age >= 18:
    print("Go vote!")
else:
    print("Register to vote when you're 18!")


print("Section 6")

# Chained together
if age >= 18:
    print("Go vote!")
elif age > 5:
    print("Shouldn't you be in school?")
else:
    print("Where are your parents?")


print("Section 7")

# What if we have multiple values?
# We need to loop!
ages = [18, 20, 24, 30, 12, 16]

for age in ages:
    if age >= 18:
        print("You're {}: Go Vote!".format(age))


