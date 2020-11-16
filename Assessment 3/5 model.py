count = 0
x = input()
y = input()
if len(x) == len(y) :
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1
        else:
            continue
    if count == 1:
        print("True")
    else:
        print("More than 1 letter differs.")
else:
    print("One string is longer.")