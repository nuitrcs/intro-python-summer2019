# FILES exercise answers

# Remember: to run this in PyCharm, right-click and choose to run this file,
# or use the Run option at the top



# Create a file called colors.txt and write each color
# in the color list to the file, one on each line.
# Don't forget the \n newline character

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

with open("colors.txt", "w") as of:
    for color in colors:
        of.write(color+"\n")




# Now, open colors.txt to read in values.  Loop through the values
# that result from readlines().  If the color has more than 4 letters in the name,
# print it (strip whitespace first).

with open("colors.txt") as df:
    for line in df.readlines():
        if len(line.strip()):
            print(line.strip())



