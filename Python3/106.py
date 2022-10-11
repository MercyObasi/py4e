# Remove Outliers
def outliers_removed(data,num):
    val = sorted(data)
    for i in range(num):
        val.pop()
        val.pop(0)
    return val

def main():
    lost = []
    t = 0
    while t != -1:
        t = int(input("Enter your Value: "))
        lost.append(t)
    if len(lost) < 4:
        print("Incomplete Values")
    else:
        print("Your Result",outliers_removed(lost,2))
        print("Your Original Result,",lost)
main()
