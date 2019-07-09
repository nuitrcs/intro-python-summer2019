# make a package accessible
import os


# This file processes all *.pdb files in the specified directory
# and combines the data rows that start with ATOM together into one CSV file
# called combined_pdb.csv in the same directory


# where is the data we want to process
data_directory = "pdb/"


# pull out a function to turn text line into data cells
def process_line(line):

    # split line into components
    processed = line.split()

    # some files have   1.00  0.00 at the end of the data lines
    # remove these last two items because they aren't needed
    if line.endswith("  1.00  0.00\n"):
        return processed[:-2]

    return processed


def format_line(filename, molecule, data, sep=","):
    # quoting molecule name in case of comma in the name
    return filename + sep + '"' + molecule + '"' + sep + sep.join(data) + "\n"


with open(os.path.join(data_directory, 'combined_pdb.csv'), 'w') as outputfile:
    for pdbfilename in os.listdir(data_directory):
        if pdbfilename.endswith(".pdb"):  # only process *.pdb files
            with open(os.path.join(data_directory, pdbfilename)) as datafile:
                molecule_name = None
                for line in datafile.readlines():
                    if line.startswith("COMPND"):  # extract name of the molecule
                        molecule_name = line.replace("COMPND", "").strip()
                    elif line.startswith("ATOM"):  # good data lines

                        # call a function to separate text line into fields
                        processed = process_line(line)

                        # add the line to the output, comma separated
                        outputfile.write(format_line(pdbfilename, molecule_name, processed))
