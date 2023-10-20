import sys
if sys.hexversion < 50925040:
    print("Sorry python 3.9.13 or above is required for installation")
    print("")
    print("Press enter to continue, N to quit")
    input()
    exit()
from function import main

if __name__ == "__main__":
   (main.send())\
        .content()