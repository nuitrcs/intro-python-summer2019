# ANSWER TO CHALLENGE EXERCISE

# Modify process_pdb.py to also extract and save the author info and date from each file
# (include it in the output file).

# NOTE: This modifies process_pdb_function.py, but you
# could change the version without functions instead.

# Remember: to run this in PyCharm, right-click and choose to run this file,
# or use the Run option at the top

import os
import datetime

# changing the file path below because PyCharm defaults working directory to where this file is
data_directory = "../pdb/"

def process_line(line):
    processed = line.split()
    # deal with lines in other format
    if line.endswith("  1.00  0.00\n"):
        processed = processed[:-2]
    return processed


# changing this function to output author info too
def format_line(output, sep=","):
    # check each value to see if it contains the sep character: if so, quote the value
    # NOTE: this actually changes the values in the list passed in!
    # But we're ok with that in this case
    for i in range(len(output)):
        # we're going to index into the list here instead of looping through the
        # elements directly so that we can change the values of the list.
        if sep in output[i]:
            output[i] = '"' + output[i] + '"'
    return sep.join(output) + "\n"


def get_author_info(line):
    # do basic line cleanup first
    authorinfo = line.replace("AUTHOR", "").strip()
    # split it into pieces on the spaces, so we can check each piece of info
    authorinfo = authorinfo.split()

    # set initial values
    authorname = None
    dates = []

    # examine each piece of the author info
    for chunk in authorinfo:
        if chunk.isdigit():  # part of the date
            dates.append(chunk)
        else:  # part of the name
            if authorname is None:  # found first part of name
                authorname = chunk
            else:  # found a middle or last name, so add a space in
                authorname += " " + chunk

    # add in some basic error checking to make sure we're doing this right
    if len(dates) != 3:
        print("ERROR!  Don't have the right number of dates: " + dates)
        return

    # make the date a nicer format for the future
    file_date = "19{}-{}-{}".format(dates[0], dates[1], dates[2])
    return authorname, file_date


# changing the file path below because PyCharm defaults working directory to where this file is
with open(os.path.join(data_directory, 'combined_pdb_author.csv'), 'w') as outputfile:
    for pdbfilename in os.listdir(data_directory):
        if pdbfilename.endswith(".pdb"):
            with open(os.path.join(data_directory, pdbfilename)) as datafile:
                molecule_name = None
                author = None
                file_date = None
                for line in datafile.readlines():
                    if line.startswith("COMPND"):
                        molecule_name = line.replace("COMPND", "").strip()
                    # extract author name and date using function above
                    elif line.startswith("AUTHOR"):
                        author, file_date = get_author_info(line)
                    elif line.startswith("ATOM"):  # good data lines
                        processed = process_line(line)
                        # make sure to change this and the function to also output the info
                        # I made this a little nicer by putting inputs together in a single list
                        output = [pdbfilename, molecule_name, author, file_date] + processed
                        outputfile.write(format_line(output))



