
greet = lambda: print("Hello" + __name__)
# If a user starts for the first time , you print the code below.
# In a case where you want to import the first module for another program
# without printing the fxn greet
if __name__ == "__main__":
    greet()

print("Hi, I'm Siri", __name__)


# This is basically for identifying the first code
