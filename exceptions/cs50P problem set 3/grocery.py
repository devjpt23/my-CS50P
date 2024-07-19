arr = []
empdict = {}
def main():
    while True:
        try:
            itemIntoDict(appeningItemIntoArr())            
        except EOFError:     
            gettingItemList(empdict)      
            break

def appeningItemIntoArr():
    itemName = input("").upper()
    arr.append(itemName)
    return arr

def itemIntoDict(array):
    for item in array:
        empdict[f'{item}'] = array.count(item)

def gettingItemList(dict):
    for key,value in sorted(dict.items()):
        print(f"{value} {key}")
main()