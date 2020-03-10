# Filefixer

I wrote this simple script to edit files at runtime. replace_line.py contains a simple function Fix which will look for an exact match and replace this line with something different.

I wrote and tested this for python 2.7 under Linux, possibly it works for other versions too (not tested!). Some fixes could be needed to make it work under Windows.

## Demo
The main() in replace_line gives a demonstration of how this works:
* it will import Example.py and show the output of the function
* A line is then replaced with the Fix function (in memory)
* the edited file will then be written to disk
* the file is reloaded since it changed
* the function is executed and will show a different output

## Function parameters
Fix(fnd,rp,fn):
* fnd: this is the line to be found (exact match)
  * check  [this](https://docs.python.org/3/library/re.html#regular-expression-syntax) for the syntax you should use
* rp: this is the new line that will replace fnd
* fn: name of the file to be edited (take folder structure into account!)

## Example
    import Filefixer

    Filefixer.Fix("#import math","import math","math_thingy.py")
This hypothetical execution would replace _#import math_ with _import math_ in the file _math_thingy.py_

## Why?
I needed this to correct an error in a dependency, this allows me to **not** package the dependency with the applied fix, instead I will direct the user to the correct version of the dependency and correct the error on runtime.

This keeps it user-friendly and allows me to just use the broken dependency.

The Fix function will rewrite the file so the fix (basically replacing that line) will only be done once. (after fixing once, it won't find the line and leave the file as is).

## MultiFix
MultiFix allows to pass an array of fixes, for example:

    arrayofFixes = [["line1","line1replacement"],
    ["line2","line2replacement"],
    ["line3","line3replacement"]]

A correct function call would look like:

    import Filefixer
    Filefixer.MultiFix(arrayofFixes,"filename.py")

## Future
MultiFix is suboptimal, it will reopen, find and write for each array that is passed, this can be improved easily.
Fix is suboptimal too in a sense, best would be to join both functions in one and look at the parameters to determine what to do (multifix or one fix). Also it should be possible to edit just one line instead of reading the whole file to memory and then write to disk.
