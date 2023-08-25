# PlotLang
A language for easily and effectively creating plots.

PlotLang makes use of PyMeta (a derivation of the OMeta language parser for Python 2.7) in order to create a language that takes in data and produces a corresponding plot.
All files written in PlotLang have a file ending of `.pll`

Developed with [Fardin Hoque](https://github.com/kfhfardin)

## Dependencies
- PyMeta can be downloaded [here](https://launchpad.net/pymeta)
- Python 2.7 must be installed, a link to download can be found [here](https://www.python.org/downloads/release/python-2718/)

## Setup and Install
- run `py -2 setup.py install` within the terminal to install PyMeta
- run `pip install numpy` in the terminal to install NumPy
- run the following in the terminal to install matplotlib:
```
python -m pip install -U pip
python -m pip install -U matplotlib
```

## To Run the Compiler
- Within `plotLangBootstrap.py`, write the desired `.pll` file name as the first parameter in `open()`
- Run `plotLangBootstrap.py` which generates executable Python code in `test_plotlang.py`
- Run `test_plotlang.py` to generate a plot

## Language Features and Syntax
### Assignment Statement
`<identifier> ::= <Input Data>`  
- the identifier represents a variable name and the input data is the data you want to be plotted
### Terminator
`;`  
- Each line must end with the above terminator
### White Space
`' ' | \n | \r | \t | <Cmt>`  
- Any of the above symbols/character combinations are considered white space by the parser
### Comment
`! <String> !`  
- Comments are formed by placing the desired comment between exclamation points
### Strings
`" <String> "`  
- PlotLang follows standard string syntax with the desired string text in between quotations

### Input Data
- Input data comes in a few forms and is formatted as so:  
`<identifier_data> ::= [(<List> | <Range>) : (<NumList> | <Range>)];`  
- Within the hard brackets, the x-values are placed to the left of the colon and y-values to the right
- x-values can either be a List or a Range
- y-values can either be a NumList or a Range, it must be a NumList instead of a List in order to quantify the data into a graph
- PlotLang assumes that each x-value has a corresponding y-value
### Lists
`[elem1, elem2, elem3 ...]`  
- Lists consist of elements written inside hard brackets separated by commas
- Numbers, characters, and strings are valid list values
### NumLists
`[Num1, Num2, Num3 ...]`
- NumLists are the same as lists but their elements must be numbers
### Ranges
- There are three types of ranges, each with a unique syntax:

`[Num1 .. Num2]`
- This range includes all integers from `Num1` to `Num2`, inclusive
- The two periods (`..`) tells the parser this is an iteration

`[Num1 .. Num2, Num3]`
- The addition of `Num3` following the comma can be used as a factor or multiplier to augment the basic iteration

`[Num1 .. Num2, function]`
- Instead of `Num3` as in the previous range, `function` is a basic function that can be mapped over the Range to augment it
- `function` **MUST be a string**

### Graph Calls
- Graph calls follow the following syntax:

`GraphType("Title", <identifier_data>);`
- where `GraphType` is the type of plot being made (i.e. Bar, Pie, Line, Scatter), `"Title"` is the title of the plot, and `<identifier_data>` is the data or the variable name that represents the data
- `GraphType` will always be in all uppercase letters
- This call may have additional parameters depending on the type of plot being made
### Bar Graph
`BAR("Title", "x-label", "y-label", <identifier_data>);`
- `x-label` and `y-label` represent the name for the x- and y-axes respectively
### Pie Graph
`PIE("Title", <identifier_data>);`
- pie graphs only include the title and data
### Line Graph
```
LINE("Title", "x-label", "y-label", <identifier_data>);
| LINE("Title", "x-label", "y-label", <identifier_data_1>, <identifier_data_2>);
```
- Line graphs can be plotted with one or two lines. Adding a second set of data allows for a second line to be plotted
### Scatter Plot
```
SCATTER("Title", "x-label", "y-label", <identifier_data>);
| SCATTER("Title", "x-label", "y-label", <identifier_data>, TRUE);
```
- Scatter plots can either be plotted as a simple scatter plot or be plotted with a line of best fit with the addition of `True` following `<identifier_data>`
