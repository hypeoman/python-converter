# python-converter

## Using the program

This program is designed to convert length units, convertible lengths are shown below.

Program Syntax: `python main.py <Input_Unit> <Output_Unit> <Input_Unit_Value>`
Examples:
`Input: python main.py m cm 1
Output: 100.0`

### Program supported units
1. km : kilometer
2. m : meter
3. cm : centimeter
4. mm : millimeter
5. um : micrometer
6. nm : nanometer
7. me : mile
8. yd : yard
9. ft : foot
10. in : inch
11. sm : nautical (sea) mile

## Creating a command for the terminal (command line)

For normal use of the program, you need to create an alias in the terminal or command line.

### Windows (Command line)

1. Сhange the converter.cmd file, instead of `/path/to/main.py` write your path to main.py file.
2. After changing converter.cmd file, you must be place him in the folder located in the PATH variable, for example `C:\Windows\System32`.
3. Use in CMD like : ` Input: converter cm m 100 Output: 1.0 ` 
