password = input('Enter Password')

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

print(result)