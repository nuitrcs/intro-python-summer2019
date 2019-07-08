# IF exercise answers

# Remember: to run this in PyCharm, right-click and choose to run this file,
# or use the Run option at the top


# Remember the format of if statements
age = 20
if age >= 18:
    print("Go vote!")
elif age > 5:
    print("Shouldn't you be in school?")
else:
    print("Where are your parents?")


# Here's our color for loop from before.
# Change the loop to only print the color if the first letter is > "m".
# Hint: the if statement goes on the line after the for statement,
# and make sure to check the indentation on the print statement after that.

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
for color in colors:
    if color[0] > "m":
        print(color)


# Here are the lines of ammonia.pdb in a list
ammonialines = ["COMPND      Ammonia",
                "AUTHOR      DAVE WOODCOCK  97 10 31",
                "ATOM      1  N           1       0.257  -0.363   0.000",
                "ATOM      2  H           1       0.257   0.727   0.000",
                "ATOM      3  H           1       0.771  -0.727   0.890",
                "ATOM      4  H           1       0.771  -0.727  -0.890",
                "TER       5              1",
                "END"]

# We need to extract the compound name and data lines.
# Loop through each line in ammonialines.
# If the line starts with COMPND, save the line to
# the compound variable.
# If the line starts with ATOM, append it to datalines.
# Otherwise do nothing.
# Hint 1: line.startswith("COMPND")
# Hint 2: datalines.append(line)

compound = None
datalines = []

for line in ammonialines:
    if line.startswith("COMPND"):
        compound = line
    elif line.startswith("ATOM"):
        datalines.append(line)



# look at what we saved
print("The compound line is:", compound)
# the below is a way to concatenate elements of a list
# in a string with a separator - the syntax is a little odd
print("Data lines:")
print("\n".join(datalines))


