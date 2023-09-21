############################################################################
# Program 1: Base Converter (Main Program)
# Liz Denson
# 2023-09-21
# The main program used to convert a given number from one base to another.
# Requires: number.py, input.txt, and output.txt
############################################################################

# import Number class from number.py
from number import Number

def main():
    # read lines from input.txt
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # open output.txt for writing
    with open("output.txt", "w") as outfile:
        for line in lines:
            value, current_base, target_base, max_bits = line.strip().split()            
            # initialize a Number object with the values from the line
            num = Number(value, int(current_base), int(target_base), int(max_bits))
            # write the converted number to output.txt
            outfile.write(num.convert() + '\n')

######
# MAIN
######
if __name__ == "__main__":
    main()


