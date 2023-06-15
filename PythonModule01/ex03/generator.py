import sys
import random

def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    option_list = ["shuffle", "unique", "ordered"]
    if not isinstance(text, str) or option != None and option not in option_list:
        print("ERROR")
        sys.exit(1)
    substrings = text.split(sep)
    if option == "shuffle":
        random.shuffle(substrings)
    if option == "unique":
        substrings = list(set(substrings))
    if option == "ordered":
        substrings.sort()
    for elem in substrings:
        yield elem