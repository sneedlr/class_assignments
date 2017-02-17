def primeFind(n):
    dividend = 2
    while dividend < n:
        if n%dividend == 0:
            return False
        dividend+=1
    return True
testNum=2
while testNum <= 100:
    if primeFind(testNum):
        print(testNum, "is a prime number.")
    testNum = testNum + 1
primeFind()