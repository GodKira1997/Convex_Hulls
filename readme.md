# Assignment 01

This assignment includes 2 python files namely "brute_force.py" & 
"graham_scan.py" and 1 report named "RunTimeAnalysis.pdf" which contains 
runtime analysis of  the algorithms used to create convex hulls for same input.

## Pre-requisites

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 
libraries (if required).

```bash
pip install sys
pip install time
pip install math
pip install matplotlib
```

## Usage
### For brute_force.py
```commandline
brute_force.py input.txt
```
### For graham_scan.py
```commandline
graham_scan.py input.txt
```

## Output
The output convex hull **takes into account collinear points**, which means 
that 
there will be points in the convex hull that are collinear with others, 
leading to a **higher number of points included** in the output convex hull.
Secondly, The output files are created in the same folder as the python files 
(execution folder).
### For brute_force.py
```markdown
"output_brute.txt" file is created and a plot is displayed on execution.
```
### For graham_scan.py
```markdown
"output_graham.txt" file is created and a plot is displayed on execution.
```
