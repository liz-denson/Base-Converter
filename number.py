############################################################################
# Program 1: Base Converter (Number Class)
# Liz Denson
# 2023-09-21
# Source code used to convert a given number from one base to another.
############################################################################

# number class
class Number:
    
    # digits for bases up to 36
    BASE_DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # constructor to initialize the number object
    def __init__(self, value, current_base, target_base, max_bits):
        self.value = value
        self.current_base = current_base
        self.target_base = target_base
        self.max_bits = max_bits

    # convert the number to base 10
    def to_decimal(self):
        # string representation of value
        value_str = str(self.value)
        # initialize decimal_value at 0
        decimal_value = 0
        # loop through each digit in the value
        for index in range(len(value_str) - 1, -1, -1):
            # get the current digit from value_str
            current_digit = value_str[index]
            # find the index of the current digit in the base digits
            digit_index = Number.BASE_DIGITS.index(current_digit.upper())
            # determine the position of the current digit in the value
            position = len(value_str) - 1 - index
            # add to the decimal_value based on current digit & position
            decimal_value += digit_index * (self.current_base ** position)
        # return the decimal_value
        return decimal_value

    # convert the number in base 10 to the target base
    def from_decimal(self):
        # get the base 10 value
        decimal_value = self.to_decimal()
        # ref to base digits constant
        digits = Number.BASE_DIGITS
        # if the value in base 10 is 0,
        if decimal_value == 0:
            # return the first digit
            return digits[0]
        # initialize the target_value as an empty string
        target_value = ""
        # loop to convert the decimal value to the target value
        while decimal_value:
            # calculate the remainder
            remainder = decimal_value % self.target_base
            # get the quotient
            decimal_value = decimal_value // self.target_base
            # prepend the digit for the remainder to target_value
            target_value = digits[remainder] + target_value
        # return the target_value 
        return target_value

    # convert the number to the target base
    def convert(self):
        # get target value in target base
        target_value = self.from_decimal()
        # if the length of target_value is longer than max_bits,
        if len(target_value) > self.max_bits:
            # return OVERFLOW
            return "OVERFLOW"
        # while the length of target_value is less than max_bits,
        while len(target_value) < self.max_bits:
            # prepend a 0 to target_value
            target_value = '0' + target_value
        # return the target_value
        return target_value