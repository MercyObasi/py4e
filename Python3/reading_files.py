f = open("/Users/Mercy/Documents/Demo file.txt","a")
# or with open("/Users/Mercy/Documents/Demo file.txt") as f:
# r = read mode
# w = write mode
# a+ = append mode
file_data = f.read()
f.close()
print(file_data)