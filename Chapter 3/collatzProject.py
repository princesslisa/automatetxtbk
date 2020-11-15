def collatz(number):
    
    if number % 2 == 0:
        even = number // 2
        print(even)
        return even
    else:
        odd = 3 * number + 1
        print(odd)
        return odd

try:
    userNum = int(input("Enter a number: "))
except ValueError:
    print("Please enter an integer value")
    userNum = int(input())
while collatz(userNum) != 1 :
    try:
        userNum = int(input())
    except ValueError:
        print("Please enter an integer value")
        continue


print("Collatz sequence achieved.")



