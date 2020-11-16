teststr = "GeeksForGeeks"

res = [char for char in teststr if char.isupper()]
tex = [char for char in teststr if char.islower()]

print (" the capital letters in the string are :"  + str(res))
print (" the lower case letters in the string are :"  + str(tex))

for char in teststr:
    if char.isupper():
        print(char.lower(),end="")
    if char.islower():
        print(char.upper(),end="")

