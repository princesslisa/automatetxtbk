def primes(n): 
    primeN = []
    for ANum in range(2,n):
        Prime = True
        for num in range (2,ANum):
            if ANum % num == 0:
                Prime = False
        if Prime:
            primeN.append(ANum)
    print(primeN)

try:
    primes(int(input("Enter a number: ")))
except ValueError :
    primes(100)
