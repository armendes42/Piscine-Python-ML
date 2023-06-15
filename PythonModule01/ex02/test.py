from vector import Vector

try:
    v1 = Vector([[1.0, 3.0, 5.0, 7.0, 9.0]])
    v2 = Vector([[0.0], [2.0], [4.0], [6.0], [8.0]])
    v3 = Vector(5)
    v4 = Vector((10, 20))

    print("Test for __str__")
    print(v1)
    print()
    print(v2)
    print()
    print(v3)
    print()
    print(v4)
    print()

    print("Test for __repr__")
    print(repr(v1))
    print()
    print(repr(v2))
    print()
    print(repr(v3))
    print()
    print(repr(v4))
    print()

    # print("Error Addition")
    # v5 = v1 + v2
    # print(v5)
    # print()

    print("Addition")
    v5 = v2 + v3
    print(v5)
    print()

    v5 = v3 + v2
    print(v5)
    print()

    # print("Error Substraction")
    # v5 = v1 - v2
    # print(v5)
    # print()

    print("Substraction")
    v5 = v2 - v3
    print(v5)
    print()

    v5 = v3 - v2
    print(v5)
    print()

    # print("Error Division")
    # v5 = v2 / v3
    # print(v5)
    # print()

    print("Division")
    v5 = v2 / 2
    print(v5)
    print()

    v5 = v4 / 2
    print(v5)
    print()

    # print("Error Multiplication")
    # v5 = v1 * v2
    # print(v5)
    # print()

    print("Multiplication")
    v5 = v4 * 3
    print(v5)
    print()

    v5 = v3 * 3
    print(v5)
    print()

    # print("Error Dot()")
    # v5 = v1.dot(v2)
    # print(v5)
    # print()

    print("Dot()")
    v5 = v2.dot(v3)
    print(v5)
    print()

    print("T()")
    v5 = v2.T()
    print(v5)
    print(v2)
    print()

    print("T()")
    v5 = v1.T()
    print(v5)
    print(v1)
    print()

except ValueError as e:
    print(e)