def hex_to_decimal(hex_value):
    decimal = 0

    for i, digit in enumerate(reversed(hex_value)):
        # need to add the base to int to account for all hex digits (1-f)
        decimal += int(digit, 16)*16**i 

    return decimal

if __name__ == '__main__':
    hex_num = input('Enter the hex value to convert: ')
    print(hex_to_decimal(hex_num))
