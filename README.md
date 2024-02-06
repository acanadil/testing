# Calculator compiler

Simple compiler to convert source code to C3A code.

![example workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)

## Prerequisites
    · gcc
    · flex
    · bison

## Usage

### Build

```bash
make
```

### Execution

```bash
./acando_calculator.exe inputs/input.txt output.txt
```

You can use any input file you want, as long as it follows the gramatical an syntactical rules specified below.

I highly recommend to clean and build each for each execution, since symtab may store balues in between executions.

### Clean
```bash
make clean
```

### Output
Logs are printed out in the terminal where the command is being executed.
The C3A code resulting from the source code can be read in the output.txt file
```bash
cat output.txt
```

## Syntax

### Important file format
It is mandatory that the input file does NOT end with empty lines. The last line of the file must contain the HALT command. Otherwise, it will prompt an error

### Data Types
    Integers           3
    Floats             3.456
    Booleans           true
    
### Structures
We can define one dimensioned arrays of either Integer type or Float type, like this:
```bash
//create
array_name := array(array_size) of name_typ (eg. 'Integer' or 'Float')

//store
array_name[position] := value or variable

//load
variable := array_name[position]
```

### Arithmetic Operands
We have various available arithmetic operands. We can use them to operate with float and integer numeric values, but we can also add (and ONLY add) strings with other strings and strings with numeric values.

    Unary Addition     ++
    Unary Subtraction  --
    Addition           +
    Subtraction        -
    Multiplication     *
    Division           /
    Module             %
    Exponentiation     **
    Unary addition     -
    Unary subtraction  +
    Assignation        :=
    Parenthesis        ()
    
### Boolean operands
We can use boolean operands with boolean values or, when comparing values, with numeric values.

    And                AND
    Or                 OR
    Not                NOT
    Greater            >
    Greater or equal   >=
    Equal              ==
    Lower or equal     <=
    Lower              <
    Not equal          !=
    
### Conditional functionalities
### ·   If statement
```bash
if boolean_expression do
    code
fi
```
### ·   If/else statement
```bash
if boolean_expression do
    code
else
    code
fi
```
### ·   Switch statement
```bash
switch(integer_aritmetic_value)
    case constant_integer_aritmetic_value:
        code
        break;
    [...]
    default:
        code
        break;
fswitch
```

### Iterative functionalities
### ·   Repeat loop
```bash
repeat integer_expression do
    code
done
```
### ·   While loop
```bash
while boolean_expression do
    code
done
```
### ·   Do until loop
```bash
do 
    code
until boolean_expression
```
### ·   For range loop
```bash
for id in initial_aritmetic_value..final_aritmetic_value do
    code
done
```

### Other functionalities
We can also do casts between aritmetic values using the functions '(Integer)' and '(Float)' like this:
```
x := 3.0
y := (Integer) x
z := (Float) y
a := (Integer) (z**15 * 3.0)
```

### Comments
They can contain any character and can be declared in three ways:

    # comment1
    // comment2
    /* multiline
      comment
      example*/
    



## Author

[Albert Cañadilla Domingo](https://github.com/acanadil/)