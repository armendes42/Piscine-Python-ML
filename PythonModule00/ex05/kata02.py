kata = (2019, 9, 25, 3, 30)

result = ""
if len(str(kata[1])) == 1:
    result += '0'
result += str(kata[1])

result += '/'

if len(str(kata[2])) == 1:
    result += '0'
result += str(kata[2])

result += '/'

if len(str(kata[0])) < 4:
    for i in range(4 - len(kata[0])):
        result += '0'
result += str(kata[0])

result += ' '

if len(str(kata[3])) == 1:
    result += '0'
result += str(kata[3])

result += ':'

if len(str(kata[4])) == 1:
    result += '0'
result += str(kata[4])

print(result)