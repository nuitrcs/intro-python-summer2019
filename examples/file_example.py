# Remember: to run this in PyCharm, right-click and choose to run this file,
# or use the Run option at the top


import os

# working directory is where the file is

print("Reading the whole file")

with open("../pdb/ammonia.pdb") as datafile:
    print(datafile.read())

print("Files without with")

datafile = open("../pdb/ammonia.pdb")
print(datafile.read())
datafile.close()


print("Reading individual lines, changing the file alias")

with open("../pdb/ammonia.pdb") as df:
    print(df.readlines())

# The newlines stay on the end of the lines;

with open("../pdb/ammonia.pdb") as df:
    for line in df.readlines():
        print(line)

# strip the whitespace from the beginning and end of the lines:

with open("../pdb/ammonia.pdb") as df:
    for line in df.readlines():
        print(line.strip())


print("Working with file paths")
datadirectory = "../pdb"
print(os.path.join(datadirectory, "ammonia.pdb"))

with open(os.path.join(datadirectory, "ammonia.pdb")) as datafile:
    print(datafile.readlines())


print("Writing files: create a file")

with open("temp.txt", "w") as outputfile:
    outputfile.write("Hello!")


print("Overwrite the file")
with open("temp.txt", "w") as of:
    of.write("Goodbye!")


print("Append to the file instead")
with open("temp.txt", "a") as outputfile:
    outputfile.write("Hello again!")
