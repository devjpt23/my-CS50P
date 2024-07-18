def main():
    x = get_int('what is x? ')
    y = get_int('what is y? ')
    print(f"value of x is {x}")
    print(f"value of y is {y}")

def get_int(name):
    while True:
        try:
            return int(input(name))
        except ValueError:
            pass
      
main()
