import sys

if len(sys.argv) > 3 or len(sys.argv) == 2:
    print("Error: More than two arguments are provided")
elif len(sys.argv) == 3:

    if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        print("Error: One or both of the arguments aren't integers")
    else:

        first_num = int(sys.argv[1])
        second_num = int(sys.argv[2])
        print("Sum:        " + str(first_num + second_num))
        print("Difference: " + str(first_num - second_num))
        print("Product:    " + str(first_num * second_num))
        if second_num == 0:
            print("Quotient:   ERROR (division by zero)")
            print("Remainder:  ERROR (modulo by zero)")
        else:
            print("Quotient:   " + str(first_num / second_num))
            print("Remainder:  " + str(first_num % second_num))

