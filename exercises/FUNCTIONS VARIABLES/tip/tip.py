def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    
    dollarSign = "$"
    if dollarSign in d:
        return float(d.replace(dollarSign," ").strip())

def percent_to_float(p):
    
    percentageSign = "%"
    if percentageSign in p:
        return float(p.replace(percentageSign," ")) / 100


main()
