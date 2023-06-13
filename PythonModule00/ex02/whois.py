import sys

try:
    assert len(sys.argv) > 1
    assert len(sys.argv) < 3, "AssertionError: more than one argument are provided"
    assert sys.argv[1].isdigit(), "AssertionError: argument is not an integer"
    
    num = int(sys.argv[1])

    if num == 0:
        print("I'm Zero.")
    elif num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as msg:
    print(msg)