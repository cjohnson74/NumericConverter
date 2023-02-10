
def print_menu():
    print('Decoding Menu\n'
          '-------------\n'
          '1. Decode hexadecimal\n'
          '2. Decode binary\n'
          '3. Convert binary to hexadecimal\n'
          '4. Quit\n')

def hex_char_decode(hex_char):
    char_values = {
        'A': 10,
        'a': 10,
        'B': 11,
        'b': 11,
        'C': 12,
        'c': 12,
        'D': 13,
        'd': 13,
        'E': 14,
        'e': 14,
        'F': 15,
        'f': 15
    }

    if hex_char in 'ABCDEFabcdef':
        return char_values[hex_char]
    else:
        return int(hex_char)


def hex_string_decode(hex_string):
    converted_decimal = 0

    if (hex_string[1] == 'x') or (hex_string[1] == 'b'):
        hex_string = hex_string[2:]

    for i in range(0, len(hex_string)):
        hex_char = hex_string[i]
        converted_decimal += hex_char_decode(hex_char) * (16 ** abs(i-len(hex_string)+1))

    return converted_decimal

def decode_hex():
    hex_string = input('Please enter the numeric string to convert: ')
    return hex_string_decode(hex_string)

def binary_string_decode(binary_string):
    converted_decimal = 0

    if (binary_string[1] == 'x') or (binary_string[1] == 'b'):
        binary_string = binary_string[2:]

    for i in range(0, len(binary_string)):
        binary_char = binary_string[i]
        converted_decimal += int(binary_char) * (2 ** abs(i-len(binary_string)+1))

    return converted_decimal

def decode_binary():
    binary_string = input('Please enter the numeric string to convert: ')
    return binary_string_decode(binary_string)

def decimal_to_hex(decimal_string):
    char_values = {
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
    }

    if decimal_string in '123456789':
        return decimal_string
    else:
        return char_values[decimal_string]


def binary_to_hex(binary_string):
    converted_decimal = ''

    while len(binary_string) > 0:
        four_binary_digit_set = binary_string[:4]
        converted_decimal += decimal_to_hex(str(binary_string_decode(four_binary_digit_set)))
        binary_string = binary_string[4:]

    return converted_decimal

def convert_binary_to_hex():
    binary_string = input('Please enter the numeric string to convert: ')
    return binary_to_hex(binary_string)


def hex_or_binary_to_dec():
    converter_on = True

    while converter_on:
        print_menu()
        option = input('Please enter an option: ')

        if option == '1':
            converted_decimal = decode_hex()
            print(f'Result: {converted_decimal}\n')
        elif option == '2':
            converted_decimal = decode_binary()
            print(f'Result: {converted_decimal}\n')
        elif option == '3':
            converted_hex = convert_binary_to_hex()
            print(f'Result: {converted_hex}\n')
        else:
            print('Goodbye!')
            converter_on = False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hex_or_binary_to_dec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
