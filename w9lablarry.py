#problem1
while 0 == 0:
    print("infinite")

#problem2
l=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
def sumTo(aBound):
    "Loop until"
theSum = 0
aBound = 10
aNumber = 1
while aNumber <= aBound:
    print(l)
    theSum = theSum + aNumber
    aNumber = aNumber + 1
print(sumTo(10))


#problem3

def sumTo(aBound):
    "Loop until"
theSum = 0
aBound = 100
aNumber = 0
n = input("type a number")
while aNumber <= aBound:
    print(n)
    theSum = theSum + aNumber
    aNumber = aNumber + n
print(sumTo(100))

#problem4

def sumTo(aBound):
    "Loop until"
theSum = 0
aBound = 50
aNumber = 0

if aNumber == 10:
    print("divisible by 10")
else:
    print(aNumber)

if aNumber == 20:
    print("divisible by 10")
else:
    print(aNumber)

if aNumber == 30:
    print("divisible by 10")
else:
    print(aNumber)

if aNumber == 40:
    print("divisible by 10")
else:
    print(aNumber)

if aNumber == 50:
    print("divisible by 10")
else:
    print(aNumber)

while aNumber <= aBound:
    theSum = theSum + aNumber
    aNumber = aNumber + 1
    print(aNumber)

print(sumTo(50))

