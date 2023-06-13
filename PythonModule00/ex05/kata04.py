kata = (0, 4, 132.42222, 10000, 12345.67)

result = "module_"
if len(str(kata[0])) == 1:
    result += '0'
result += str(kata[0])

result += ", ex_"

if len(str(kata[1])) == 1:
    result += '0'
result += str(kata[1])

result += " : "

if len(str(kata[2])) > 6:
    result += str(kata[2])[:6]
else:
    result += str(kata[2])

result += ", "

result += "{:.2e}".format(kata[3])

result += ", "

result += "{:.2e}".format(kata[4])

print(result)