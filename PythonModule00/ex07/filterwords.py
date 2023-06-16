import sys
import string

if len(sys.argv) != 3:
    print("Error: Wrong number of arguments")
elif not isinstance(sys.argv[1], str) or not sys.argv[2].isdigit():
    print("Error: One or both of the type of arguments is wrong")
else:
    new_str = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
    word_list = list(new_str.split(" "))
    new_word_list = [i for i in word_list if len(i) > int(sys.argv[2])]
    print(new_word_list)