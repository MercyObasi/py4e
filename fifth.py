num = 0
tot = 0.0
while True:
    str = input("Enter a number: ")
    if str == "done":
        break
    try:
        fstr = float(str)
    except:
        print("Invalid input")
        continue
    num = num + 1
    tot = tot + fstr
print(num,tot,tot/num)
