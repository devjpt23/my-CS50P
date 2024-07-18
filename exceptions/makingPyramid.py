
# n = 4
# for i in range(n+1):
#     print(" " * (n - i),end="")
#     print('#' * i)
def main():
    x = gettingIntOnly()
    makingPyramids(x)

def gettingIntOnly():
    while True:
        try:
           return int(input("Enter a number:"))
        except ValueError:
            pass

def makingPyramids(n):
    for i in range(n+1):
        print(" " * (n - i),end="")
        print('#' * i)

main()
