ws = input("Enter Hours: ")
at = input("Enter Rate: ")
try:
    z = int(ws)
    y = int(at)
    print(z+y)
except:
    print("Error, please enter numeric input")
    quit()