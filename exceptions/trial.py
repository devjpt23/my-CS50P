# we want to make sure that we can only enter integers, anything else should be errofied

while True:
    try:
        n = int(input("enter a number: "))
        break
    except ValueError:
        print("please only enter a number ")

print(f"the number is {n}")
