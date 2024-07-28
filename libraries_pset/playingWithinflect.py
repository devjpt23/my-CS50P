import inflect
p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break
    
mylist = p.join(names)
print(f'Adieu, adieu, to {mylist}')



