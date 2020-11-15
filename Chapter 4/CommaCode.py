
def com():
    spam = []
    while True:
        print("Enter your list values: (Type . at the end of the list)")
        code = input()
        if code == ".":
            break
        spam = spam + [code]
    print("This is your list\n")
    for code in spam[0:len(spam)-1]:
        print(code, end = ", ")
    print("and " + spam[len(spam)-1])

com()