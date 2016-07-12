from random import randint
def guessingnum():
    numb = randint(1, 10)
    print numb
    print "Welocme to the number guessing game!"
    print "I have my number..."
    guenum = impnum()
    while not guenum.isdigit():
        print "Please input a legal number!"
        guenum = impnum()
    guenum = int(guenum)
    while guenum!=numb:
        if guenum > numb:
            print "That's too high. Try again!"
            guenum = int(impnum())
        elif guenum < numb:
            print "That's too low. Try again!"
            guenum = int(impnum())
    print "You got it! Thanks for playing! MemeDa"


def impnum():
    guenumber = raw_input("What is your guess [1-10]?  ")
    return guenumber
