months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
class invalidDate(Exception):
    pass

def main():
    while True:
        try:   
            date = input("Date: ").title()        

            if ("/" in date):
                x = dateWithSlash(date)
                print(x)
                break

            elif ("," in date):
                y = dateWithComma(date)
                print(y)
                break

        except (ValueError,invalidDate):
            pass
        except EOFError:
            break
        
def dateWithSlash(date):
    month,day,year = date.split("/")
    day = int(day)
    year = int(year)
    if (int(month) > 12) or (int(day) > 31):
        raise invalidDate
    else:
        return f"{int(year)}-{int(month):02}-{int(day):02}" 
    
def dateWithComma(date):
    monthDay, year = date.split(",")
    month,day = monthDay.split(" ")
    year = int(year)
    monthIndex = (months.index(f"{month}")+1)
     
    if (int(day) > 31):
        raise invalidDate
    else:
        return f'{int(year)}-{monthIndex:02}-{int(day):02}'



main()