def count_names():
    lst = range (5)
    n = 0
    for i in lst :
        x = input("Enter your name:")
        if len(x) > 5:
            n += 1
        else:
            continue
    return n
nam = count_names()
print("Names that are more than five:",nam)