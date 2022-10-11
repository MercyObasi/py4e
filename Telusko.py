# While loop Telusko Assignment
# Print 1-100 skipping numbers divisible by 3 & 5

i = 1
while i <= 100:
    if i % 3 != 0 and i % 5 != 0:
        print(i, ",",end="")

    i += 1

# Printing Pattern
# P.s. there is something wrong with my range

for s in range(4):
    for j in range(s + 1):
        print('# ',end="")
    print()

for t in range(1,5):
    for y in range(t,5):
        print(y,end="")
    print()

Lst = ["A","B","C","D","P","Q","R" ]
for u in range(4):
    for g in Lst[0],[6]:
        print(g,end="")

    print()


# Print all the perfect number btw 1 and 500

for a in range(1,501):
    if a ** 2 <= 500:
        print(a ** 2,",", end="")

# Check if a number is a prime number

x = int(input("Enter a number: "))
if x % 2 != 0 and x % 3 != 0:
    print("Prime Number:", x)
else:
    print("Not A Prime Number")

# First 50  Fibonacci Numbers
def fib(k):

    fst = 0
    sst = 1
    print(fst)
    print(sst)
    if k == 1:
        print(fst)
    elif k <= 0:
        print("Invalid Input")
    try:
        int(k)
    except:
        print("Invalid Input")
    else:
        for bt in range(2, k):

            vrt = fst + sst
            fst = sst
            sst = vrt
            if vrt <= 100:
                print(vrt)

fib(k)