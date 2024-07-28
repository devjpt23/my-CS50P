import random

def main():
    while True:
        try:
            (guessingNumber(gettingRandomNumber(getLevel())))
            break
        except ValueError:
            pass

def getLevel():
    while True:
        n = int(input("Level: "))
        if n > 0:
            False
            return n
        
def gettingRandomNumber(upperlimit):
    randomNumber = random.randint(1,upperlimit)
    return randomNumber

def guessingNumber(choosenNumber):
    while True:
        userGuess = int(input("Guess: "))
        if (userGuess > 0) and (userGuess > choosenNumber):
            True
            print( 'Too large!')
        elif (userGuess > 0) and (userGuess < choosenNumber):
            True
            print( 'Too small!')
        elif (userGuess > 0) and (userGuess == choosenNumber):
            # True
            print( 'Just right')
            break
        else:
            True
            

              

if __name__=='__main__':
    main()
