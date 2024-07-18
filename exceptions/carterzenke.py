distances = {
    'voyager1': '163',
    'voyager2': '136',
    'Pioneer 10': '80 AU',
    'New Horizons': '58',
    'Pioneer 11': '44 AU',
}
def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except ValueError:        
        print( "cannot convert to float")
        return
    except KeyError:
        print('space craft not in the list')
        return
    
    m = convert(au)
    print(f"spacecraft is {m} metres away")

def convert(au):
    return au * 149597870

main()