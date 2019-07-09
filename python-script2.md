# Python Session 2

## Getting Started

This is the second part of the Python workshop.  We'll be working in PyCharm, which is a Python IDE.  See [instructions for starting PyCharm](pycharm.md).

When you've opened your project (the folder with the files for this workshop) directly in PyCharm, you can see your files on the left.  On the bottom, there is a link to open a Python Console.  Click it, and it will open at the bottom.  This is a console like we were working in before.  In the console, type:

```python
import sys
sys.version
```

Make sure it says Python 3.7 (or at least 3.6).

We're going to start writing scripts -- where we combine multiple commands together in a file, and execute them all at once.  

## Packages, Documentation

### Importing

Above, we imported the `sys` package.  It is one of the built-in Python modules (aka package, library).  

### Documentation

[Python documentation for sys](https://docs.python.org/3/library/sys.html): https://docs.python.org/3/library/sys.html

### Installation

On Windows, click Start -> Anaconda3 -> Anaconda Prompt.

On Mac, Applications -> Utilities -> Terminal.

To practice installing packages, we're going to install the [Requests library](https://2.python-requests.org//en/master/).  It's used to make web requests and download web pages or get data from APIs.  

```
python --version
pip install requests
```

On a Mac, you may need to do the following first

```python
conda activate
```

### Let's Use It

Make a file called `test_requests.py`: 

```python
import requests

r = requests.get("https://nuitrcs.github.io/")
print(r.text)
```

Run it.  Right-click and choose Run 'test_requests.py' or from the Run menu at the top, choose the Run option without a file name listed (it's not the first option).

## Example Task

[PDB Files]("pdb/")

We're going to build up code to process these files.  What do we need to do?

* Figure out what files exist and take one at a time (loop)
* Open and process each file (files)
* Look at each line in a file (loop)
* If it has information we want, keep it (if statement)
* Extract compound name (work with strings)
* If it doesn't match our format, clean it up (if statement): see glycol vs. ammonia
* Write the output to a new file (files)

## For Loops

The first thing we want to do is get a list of the files.  Then we're going to write a loop to open each file.  The `os` library has functions for working with the file system.  The `listdir` function will list the files in a supplied directory.  When running code in PyCharm, the working directory defaults to where the file is.  (We'll look at Run Configurations.)  So we'll specify paths relative to that directory.

Make a file called `pdb_files.py`:

```python
import os

os.listdir("pdb/")
```

Did it do anything?  Why not?

```python
import os

print(os.listdir("pdb/"))
```

It gives us a list of file names in the directory.  We're going to want to process each of these files.  We'll need to loop through the values.


```python
import os

for filename in os.listdir("pdb/"):
    print(filename)
```

The indentation above matters!

See `examples/for_loops.py`

Open `exercises/forloop_exercise.py`.  


## If Statements

Back to processing the pdb files.  

We had a list of each of the files in the directory.  

```python
import os

for filename in os.listdir("pdb/"):
    print(filename)
```

It included some files that weren't .pdb files.  How do we select just the ones we want?  With an `if` statment.

```python
import os

for filename in os.listdir("pdb/"):
    if filename.endswith(".pdb"):
        print(filename)
```

This uses a string function `endswith()` that returns True if the string ends with the specified value.

```python
"flamingo".endswith("go")
"flamingo".endswith("g")
```

If statements take a condition that results in a single `True` or `False` value.  We can combine tests with `and` and `or` as well, and use `not`:

Open `examples/ifexample.py`.

Open `exercises/ifexercise.py`.

## Working with Files

Ok, we have a loop and are selecting just the files we want.  Now we need to open each one and read the lines in it.  We can use a `with` statement to open a file and let Python take care of closing it for us too!  

```python
import os

datadirectory = "pdb"

for filename in os.listdir(datadirectory):
    if filename.endswith(".pdb"):
        with open(os.path.join(datadirectory, filename)) as pdbfile:
            print(pdbfile.readlines())
```

Open `examples/file_example.py`

Open `exercises/file_exercise.py`

## Putting it together

Open `process_pdb.py`.


## Writing functions

When might we pull out code into a function?

* Repeating the same code with just slight changes
* It's a discrete process and the code will be clearer 
* We might want to reuse it or change a fixed value
* We'll need to use the same code again in a different process
* Isolate code for debugging

Open `examples/functions_example.py`

Open `exercises/functions_exercise.py`



See `process_pdb_function.py`


## Challenge Exercise

Modify `process_pdb_function.py` (or `process_pdb.py`) to also extract and save the author info and date from each file (include it in the output file).  The AUTHOR line has the author name and a date.  

Hint: Look at the `isdigit()` function of a string: https://docs.python.org/3/library/stdtypes.html#str.isdigit 

Advice: write out the steps you need to do first, then write the code to do those steps.  

For an answer (there are multiple ways to do this!), see `exercises/author_info_answer.py`





