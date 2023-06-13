import sys
import string

def text_analyzer(text=None):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """    
    if text is None or len(text) == 0:
        text = input("What is the text to analyze?\n")

    if not isinstance(text, str):
        print("AssertionError: argument is not a string")
        return

    
    
    upper = 0
    lower = 0
    punct = 0
    space = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punct += 1
        elif char.isspace():
            space += 1
    print(f"The text contains {len(text)} character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punct} punctuation mark(s)")
    print(f"- {space} space(s)")


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("more than one argument are provided")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()