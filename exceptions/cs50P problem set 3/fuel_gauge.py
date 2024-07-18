def main():    
    while(True):
        try:
            checkStatus(gettingFraction())
            break
        except (ValueError,ZeroDivisionError):
            pass

def gettingFraction():
    fraction = input('Fraction: ')
    a,b = fraction.split("/")
    percent = percentage(int(a),int(b))
    return percent

def checkStatus(p):
    if p >= 99:
         print('F')
    elif(p <= 1):
        print('E')
    else:
        print(f"{round(p)}%")   

def percentage(a,b):       
    return ((a)/(b)) * 100  
 
main()