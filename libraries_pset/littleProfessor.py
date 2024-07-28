import random
def main():
    generate_integer(get_level())

def get_level():
    # we can use a while loop
    while True:
        try:
            lvl = int(input("Level: "))
            if 1 <= lvl <= 3:
                return lvl
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
    questions = 10
    score = 0

    for _ in range(questions):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        
        triesPerQuestion = 0 
        while triesPerQuestion < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x+y):
                    score += 1
                    break
                else:
                    print("EEE")
                    triesPerQuestion += 1
            except ValueError:
                print("EEE")
                triesPerQuestion += 1

        if triesPerQuestion == 3:
            print(f"{x} + {y} = {x + y}")

    print(f'Score: {score}')

    

if __name__ == '__main__':
    main()