import sys

CHARS_TO_MORSE_CODE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}

is_error = False
for arg in sys.argv[1:]:
    for char in arg:
        if not char.isalnum() and not char.isspace():
            is_error = True

if is_error:
    print("ERROR")
elif sys.argv != 1:
    new_str = " ".join(sys.argv[1:])
    new_str = new_str.upper()
    print(new_str)
    result = ""
    for char in new_str:
        if char == ' ':
            result += '/'
        else:
            result += CHARS_TO_MORSE_CODE_MAPPING[char]
        result += ' '
    print(result)