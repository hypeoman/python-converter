import sys

# values to meter dictionary

values_to_meter_dict = {
    "km" : 0.001, # kilometer
    "m" : 1, # meter
    "cm" : 100, # centimeter
    "mm" : 1000, # millimeter
    "um" : 1e+6, # micrometer
    "nm" : 1e+9, # nanometer
    "me" : 0.000621371, # mile
    "yd" : 1.09361, # yard
    "ft" : 3.28084, # foot
    "in" : 39.37008, # inch
    "sm" : 0.00053995682073434 # nautical (sea) mile
}

# meter to value dictionary

meter_to_values_dict = {
    "km" : 1000, # kilometer
    "m" : 1, # meter
    "cm" : 0.01, # centimeter
    "mm" : 0.001, # millimeter
    "um" : 1e-6, # micrometer
    "nm" : 1e-9, # nanometer
    "me" : 1609.34, # mile
    "yd" : 0.9144, # yard
    "ft" : 0.3048, # foot
    "in" : 0.0254, # inch
    "sm" : 1852 # nautical (sea) mile
}

# converter fucntion

def convert(inputUnit, outputUnit, inputValue): 
    outputValue = float(inputValue)  * meter_to_values_dict[inputUnit] * values_to_meter_dict[outputUnit]
    return outputValue 

# main function

def main():
    if len(sys.argv) < 4:
        print("Too few arguments")
    elif len(sys.argv) > 4:
        print("Too many arguments")
    else:
        print(convert(sys.argv[1], sys.argv[2], sys.argv[3]))



if __name__ == "__main__":
    main()