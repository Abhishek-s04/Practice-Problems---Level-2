# Write a python function which accepts any number in the range of 1 to 4999 (both inclusive) and returns the equivalent roman numeral of it.
def convert_to_roman(num):
    # Define Roman numeral equivalents
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    
    result = ""
    
    # Loop through each symbol, subtracting from num and appending the symbol to the result
    for value, symbol in roman_numerals:
        while num >= value:
            result += symbol
            num -= value
            
    return result

# Testing the function for numbers from 1 to 4999
for num in range(1, 5000):
    print(num, ":", convert_to_roman(num))