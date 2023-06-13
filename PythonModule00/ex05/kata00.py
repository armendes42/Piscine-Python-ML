kata = (19,42,21)

result = "The "
result += str(len(kata))
result += " numbers are: "

for index, element in enumerate(kata):
    result += str(element)
    if index != len(kata) - 1:
        result += ", "

print(result)