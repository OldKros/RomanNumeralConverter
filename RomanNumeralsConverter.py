# Command Line integer to roman numeral converter (Only works with numbers 1-3999!)
import sys

try:
    num = int(sys.argv[1])
except (IndexError, ValueError): # if there is no argument or it is not an integer we ask again and exit the application.
    # num = 1853
    print("Please enter a number from 1-3999 on the command line")
    exit(1)

if num <= 0 or num >= 4000: # only going up to 3999 for this excersize
    print("Please enter a number from 1-3999")
    exit(1)

outputStr = ""

# all the numerals in a dictionary with the corresponding keys
conversionTable = { 1000: "M",
                    900: "CM", 500: "D", 400: "CD", 100: "C",
                    90: "XC", 50: "L", 40: "XL",10: "X",
                    9: "IX", 5: "V", 4: "IV", 1: "I"
}

# seperate the thousands, hundreds, tens and ones
thousands = (num // 1000) * 1000
num %= 1000
hundreds = (num // 100) * 100
num %= 100
tens = (num // 10) * 10
num %= 10
ones = num // 1

# Deal with thousands
for i in range(thousands // 1000):
    outputStr += conversionTable.get(1000)

def convert_digit_to_numerals(n: int, conversionTable: dict):
    outputStr = ""
    # oht = ones_hundreds_or_thousands
    # base hundreds
    if n // 100 > 0:
        oht = 100
    # base tens
    elif n // 10 > 0:
        oht = 10
    # base ones
    else:
        oht = 1

    digit = int(str(n).rstrip("0")) if len(str(n)) > 1 else n

    # if the number * the base we are working with is in the table, add it
    if digit * oht in conversionTable.keys():
        outputStr += conversionTable.get(digit * oht)

    # if the digit is higher than 5 we need to add a 5 * base and add that and then deal with the rest of the digits
    elif digit >=  5:
        digit -= 5
        outputStr += conversionTable.get(oht * 5)
        for i in range(digit):
            outputStr += conversionTable.get(oht)

    # otherwise its less than 5 and not 4 so we can add the base, digit amount of times
    else:
        for i in range(digit):
            outputStr += conversionTable.get(oht)

    # return the string we made for the current base
    return outputStr

outputStr += convert_digit_to_numerals(hundreds, conversionTable)
outputStr += convert_digit_to_numerals(tens, conversionTable)
outputStr += convert_digit_to_numerals(ones, conversionTable)

print(outputStr)
